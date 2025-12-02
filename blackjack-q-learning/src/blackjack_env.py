import random

DECK_AMOUNT = 1

def create_deck(number_of_decks):
    suits = ["s", "h", "c", "d"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for _ in range(0, number_of_decks):
        deck = [value + suit for suit in suits for value in values]
        random.shuffle(deck)
    return deck

def get_card_value(card):
    value = card[:-1] # Quitamos la letra
    
    if value in ["J", "Q", "K"]:
        return 10
    elif value == "A":
        return 11
    else:
        return int(value)

def calculate_hand_value(hand):
    value = 0
    aces = 0
    
    for card in hand:
        val = get_card_value(card)
        value += val
        if val == 11:
            aces += 1
            
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
        
    return value

def has_blackjack(hand):
    if len(hand) == 2 and calculate_hand_value(hand) == 21:
        return True
    return False

def has_busted(hand):
    if calculate_hand_value(hand) > 21:
        return True
    return False

def draw_card(deck):
    return deck.pop()

def get_initial_hand(deck):
    player_card1 = draw_card(deck)
    player_card2 = draw_card(deck)
    return [player_card1, player_card2]
    
def show_player_status(player_cards):
    print("Tus cartas: ", player_cards, "Tu suma: ", calculate_hand_value(player_cards))

def check_deck(deck, number_of_decks):
    if len(deck) < 15:
        return create_deck(number_of_decks)
    return deck

class BlackjackEnvironment:
    def __init__(self):
        self.deck = create_deck(DECK_AMOUNT)
        self.player_hand = []
        self.dealer_hand = []
    
    def reset(self):
        self.deck = check_deck(self.deck, DECK_AMOUNT)
        self.player_hand = get_initial_hand(self.deck)
        self.dealer_hand = get_initial_hand(self.deck)

        return self._get_state()
    
    def _get_state(self):
        player_sum = calculate_hand_value(self.player_hand)
        dealer_card_val = get_card_value(self.dealer_hand[0])

        return (player_sum, dealer_card_val)
    
    def step(self, action):
        # La AI ejecuta una acción

        if action == 1: # Pedir
            self.player_hand.append(draw_card(self.deck))
            if has_busted(self.player_hand):
                return self._get_state(), -1, True # Pierde así que le castigamos
            return self._get_state(), 0, False # Sigue

        elif action == 0: # Plantarse
            # Turno dealer
            while calculate_hand_value(self.dealer_hand) < 17:
                self.dealer_hand.append(draw_card(self.deck))
            
            player_sum = calculate_hand_value(self.player_hand)
            dealer_sum = calculate_hand_value(self.dealer_hand)

            if has_busted(self.dealer_hand):
                return self._get_state(), 1, True # Gana así que le recompensamos
            elif player_sum > dealer_sum:
                return self._get_state(), 1, True # Gana
            elif player_sum == dealer_sum:
                return self._get_state(), 0, True # Empata así que no hay recompensa ni castigo
            else:
                return self._get_state(), -1, True # Pierde
        
        # Aquí no debería de llegar pero por si acaso la reseteamos
        return self._get_state(), 0, True

def play_manually():
    env = BlackjackEnvironment()
    state = env.reset()
    done = False
    
    print("Nuevo Juego")
    print(f"Tu mano: {env.player_hand} ({state[0]}) | Dealer muestra: {env.dealer_hand[0]}")

    while not done:
        action = int(input("0: Quedarse, 1: Pedir -> "))
        state, reward, done = env.step(action)
        print(f"Tu mano: {env.player_hand} ({state[0]})")
        
        if done:
            print(f"Juego terminado. Recompensa: {reward}")
            print(f"Mano Dealer final: {env.dealer_hand} ({calculate_hand_value(env.dealer_hand)})")

if __name__ == "__main__":
    play_manually()