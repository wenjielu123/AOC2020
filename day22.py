# %% Import data
from collections import deque
from re import match
from utils.io_util import read_file_raw

# inputs = read_file_raw('inputs/day22_test.txt')
# inputs = read_file_raw('inputs/day22_test2.txt')
inputs = read_file_raw('inputs/day22.txt')

p1_input, p2_input = inputs.split('\n\n')
p1_cards = [int(n) for n in p1_input.split('\n')[1:]]
p2_cards = [int(n) for n in p2_input.split('\n')[1:]]

class Player:
    def __init__(self, id:int, cards:list):
        self.id = id
        self.cards = cards

    def play(self):
        return self.cards.pop(0)

    def take(self, card_hi, card_lo):
        self.cards.append(card_hi)
        self.cards.append(card_lo)

    def get_score(self):
        score = 0
        for i, card in enumerate(reversed(self.cards)):
            score += (i+1) * card
        return score

    def print(self):
        print(f'Player {self.id}\'s deck: {self.cards}')

    def __len__(self):
        return len(self.cards)

def part1(player1, player2):
    while len(player1) and len(player2):
        card1 = player1.play()
        card2 = player2.play()
        if card1 > card2:
            player1.take(card1, card2)
        elif card1 < card2:
            player2.take(card2, card1)
        else:
            print('Meet equal hands! I don\'t know what to do...')

    print(player1.get_score())
    print(player2.get_score())

player1 = Player(1, p1_cards)
player2 = Player(2, p2_cards)
part1(player1, player2)

# %% Part 2
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_memory = set()
        self.p2_memory = set()
        self.winner = None

    def play(self):
        while len(self.p1) > 0 and len(self.p2) > 0:
            if tuple(self.p1.cards) in self.p1_memory or tuple(self.p2.cards) in self.p2_memory:
                return 1

            self.p1_memory.add(tuple(self.p1.cards))
            self.p2_memory.add(tuple(self.p2.cards))

            card1 = self.p1.play()
            card2 = self.p2.play()

            if len(self.p1) >= card1 and len(self.p2) >= card2:
                p1_sub = Player(1, self.p1.cards[:card1])
                p2_sub = Player(1, self.p2.cards[:card2])
                subgame = Game(p1_sub, p2_sub)
                if subgame.play() == 1:
                    self.p1.take(card1, card2)
                else:
                    self.p2.take(card2, card1)
            else:
                if card1 > card2:
                    self.p1.take(card1, card2)
                else:
                    self.p2.take(card2, card1)
        
        return 1 if len(self.p2) == 0 else 2

player1 = Player(1, p1_cards)
player2 = Player(2, p2_cards)
game = Game(player1, player2)
winner = game.play()
print(f'Player {winner} wins the Game!')
player1.print()
player2.print()
print(player1.get_score())
print(player2.get_score())

# %% 