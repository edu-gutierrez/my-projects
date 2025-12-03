import random
import pickle
from blackjack_env import BlackjackEnvironment

# La Q-Table es el "cerebro" de la AI
q_table = {}

def get_q_values(state):
    if state not in q_table:
        q_table[state] = [0.0, 0.0, 0.0] # [Quedarse, Pedir, Doblar]
    return q_table[state]

def choose_action(state, epsilon):
    if random.random() < epsilon:
        return random.choice([0, 1, 2])
    
    values = get_q_values(state)
    if values[0] > values[1] and values[0] > values[2]:
        return 0 # Mejor quedarse
    elif values[2] > values[0] and values[2] > values[1]:
        return 2 # Mejor doblar
    else:
        return 1 # Mejor pedir 

def train():
    total_episodes = 100000000
    learning_rate = 0.01
    discount_factor = 0.99
    epsilon = 1.0
    epsilon_decay = 0.9999999
    min_epsilon = 0.01
    env = BlackjackEnvironment()

    print("Iniciando entrenamiento...")

    for episode in range(total_episodes):
        state = env.reset()
        done = False
        
        while not done:
            action = choose_action(state, epsilon)
            
            next_state, reward, done = env.step(action)
            
            current_q_values = get_q_values(state)
            old_value = current_q_values[action]
            
            if done:
                max_future_q = 0 # No hay futuro si el juego acabó
            else:
                max_future_q = max(get_q_values(next_state))
                
            # Equación de Bellman
            new_value = old_value + learning_rate * (reward + (discount_factor * max_future_q) - old_value)
            # Actualizamos la Q-Table
            q_table[state][action] = new_value
            
            # Avanzamos al siguiente estado
            state = next_state

        # Reducimos exploración
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
        
        if episode % 1000000 == 0:
            print(f"Episodio {episode} completado")

    print("Entrenamiento finalizado")

    with open("blackjack_brain.pkl", "wb") as f:
        pickle.dump(q_table, f)
        
    print("Cerebro guardado en 'blackjack_brain.pkl'")

if __name__ == "__main__":
    train()