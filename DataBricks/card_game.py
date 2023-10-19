from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

deck = [f"{str(value).zfill(2)}{suit}" for value in range(1, 14) for suit in ['c', 'd', 'h', 's']]
random.shuffle(deck)
banker_wins = 0
player_wins = 0
shuffle = False

@app.route('/')
def index():
    return render_template('index.html', banker_value='', player_value='', banker_wins=banker_wins, player_wins=player_wins)

@app.route('/shuffle', methods=['POST'])
def shuffle():
    global deck, banker_wins, player_wins
    deck = [f"{str(value).zfill(2)}{suit}" for value in range(1, 14) for suit in ['c', 'd', 'h', 's']]
    random.shuffle(deck)
    banker_wins = 0
    player_wins = 0
    return 'Deck shuffled and counters reset.'

@app.route('/play', methods=['POST'])
def play():
    global deck, banker_wins, player_wins

    if len(deck) <= 0:
       return 'Shuffle the deck first, finished all cards.'
    else:
        banker_cards = [deck.pop(), deck.pop()]
        player_cards = [deck.pop(), deck.pop()]

        result = determine_winner(banker_cards, player_cards)
        banker_value = calculate_hand_value(banker_cards)
        player_value = calculate_hand_value(player_cards)

        if result == 'Banker wins!':
            banker_wins += 1
        elif result == 'Player wins!':
            player_wins += 1

    response_data = {
        "result": result,
        "bankerCards": banker_cards,
        "playerCards": player_cards,
        "bankerValue": banker_value,
        "playerValue": player_value,
        "bankerWins": banker_wins,
        "playerWins": player_wins
    }

    return jsonify(response_data)

def determine_winner(banker_cards, player_cards):
    banker_value = calculate_hand_value(banker_cards)
    player_value = calculate_hand_value(player_cards)

    if banker_value > player_value:
        return 'Banker wins!'
    elif player_value > banker_value:
        return 'Player wins!'
    else:
        return 'It\'s a draw!'

def calculate_hand_value(cards):
    values = {'01': 1, '02': 2, '03': 3, '04': 4, '05': 5, '06': 6, '07': 7, '08': 8, '09': 9, '10': 10, '11': 10, '12': 10, '13': 10}
    hand_value = sum(values[card[:-1]] for card in cards)
    return hand_value % 10

if __name__ == '__main__':
    app.run()




