import pickle
from blackjack_env import BlackjackEnvironment, calculate_hand_value

q_table = {}

try:
    with open("blackjack_brain.pkl", "rb") as f:
        q_table = pickle.load(f)
    print("Cerebro cargado")
except FileNotFoundError:
    print("Error: No se encuentra 'blackjack_brain.pkl'")
    exit()

def get_ai_advice(state):
    if state not in q_table:
        return "NO LO SÉ :<"
    
    values = q_table[state]
    q_stay = values[0]
    q_hit = values[1]
    q_double = values[2]
    
    if q_hit > q_stay and q_hit > q_double:
        advice = "PEDIR (HIT)"
        better_val = q_hit
    elif q_double > q_hit and q_double > q_stay:
        advice = "DOBLAR (DOUBLE)"
        better_val = q_double
    else:
        advice = "QUEDARSE (STAND)"
        better_val = q_stay
        
    return f"La IA recomienda: \033[93m{advice}\033[0m (Valor Q: {better_val:.2f})"

def play_interactive():
    env = BlackjackEnvironment()
    
    while True:
        state = env.reset()
        done = False
        print("")
        print("="*20)
        print("NUEVA MANO")
        print("="*20)
        
        while not done:
            print(f"\nDealer muestra: [{env.dealer_hand[0]}]")
            print(f"Tus cartas:     {env.player_hand} -> Suma: {calculate_hand_value(env.player_hand)}")
            print(f"{get_ai_advice(state)}")
            
            action = -1
            while action not in [0, 1, 2]:
                try:
                    inp = input("Tu acción [0=Quedarse, 1=Pedir, 2=Doblar]: ")
                    action = int(inp)
                except ValueError:
                    pass
            
            state, reward, done = env.step(action)
            
            if done:
                print("-" * 20)
                print(f"Mano final Dealer: {env.dealer_hand} -> Suma: {calculate_hand_value(env.dealer_hand)}")
                print(f"Tus cartas: {env.player_hand} -> Suma: {calculate_hand_value(env.player_hand)}")
                
                if reward > 0:
                    print("\nResult: \033[92mVICTORIA\033[0m")
                elif reward < 0:
                    print("\nResult: \033[91mDERROTA\033[0m")
                else:
                    print("\nResult: \033[93mEMPATE\033[0m")
                    
        if input("\n¿Jugar otra? (Enter=Sí, n=No): ") == 'n':
            break

if __name__ == "__main__":
    play_interactive()