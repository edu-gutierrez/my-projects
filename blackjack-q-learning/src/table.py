import pickle
import os

def load_table():
    if not os.path.exists("blackjack_brain.pkl"):
        print(f"Error: No encuentro blackjack_brain.pkl")
        exit()
        
    with open("blackjack_brain.pkl", "rb") as f:
        return pickle.load(f)

def get_action(values):
    # values = [Stand, Hit, Double]
    best = values.index(max(values))
    
    if best == 0: return "\033[91m S \033[0m"
    if best == 1: return "\033[92m H \033[0m"
    if best == 2: return "\033[93m D \033[0m"
    return " ? " # Aqui no debería llegar

def print_table(q_table, usable_ace, title):
    print(f"\n\033[94m---------------{title}---------------\033[0m")
    print("     2   3   4   5   6   7   8   9  10   A")
    print("-------------------------------------------")

    start = 21
    if usable_ace:
        end = 11
    else:
        end = 7
    
    for player_val in range(start, end, -1):
        if player_val > 9:
            row = f"{player_val} |"
        else:
            row = f" {player_val} |"
        
        for dealer_val in range(2, 12):
            state = (player_val, dealer_val, usable_ace, True)
            
            if state in q_table:
                row += f"{get_action(q_table[state])} "
            else:
                row += " -  " 
        
        print(row)

if __name__ == "__main__":
    q_table = load_table()

    print(f"LEYENDA: \033[91mS=Stand\033[0m | \033[92mH=Hit\033[0m | \033[93mD=Double\033[0m")

    print_table(q_table, usable_ace=False, title="-MANOS DURAS-")
    print_table(q_table, usable_ace=True,  title="MANOS BLANDAS")