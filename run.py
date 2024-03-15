import random 

class Card():
    """
    Class to represent card values that can be used when playing to determine the value of the hand
    """

    #initializing card rank (e.g. King) and suit (e.g. Hearts)
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    #represents the card in a string
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    @property
    def value(self):
        #Aces have the initial value of 11 
        if self.rank == "Ace":
            value = 11
        else:
            try:
                #value of the card equals the rank
                value = int(self.rank)
            except:
                #if unable to convert rank to int for face cards then the value is 10
                value = 10
        return value
    
class Deck():
    """
    Class representing a deck of cards that the user and dealer will draw from to create hands and when they decide to hit
    """

    #initializes deck list
    def __init__(self):
        self.cards = []

    #loops through all ranks and suits to create a deck of cards 
    def add_cards(self):
        SUITS = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in SUITS:
            for rank in RANKS:
                card = Card(rank, suit)
                self.cards.append(card)
    
    #returns the length of the deck of cards (will be used in the future for calculating the true could of the cards)
    def __len__(self):
        return len(self.cards)
    
class Player():
    """
    Class representing the player that stores the players name, current hand, and current score
    """

    #initializes player variables
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    #returns printable representation of player's name, hand, and score 
    def __repr__(self):
        return f"{self.name}'s hand is {self.hand} with their current score being {self.score}"

class Game():
    """
    Game class for the main game
    """

    #initializes a list of players for 
    def __init__(self):
        self.players = []
        
    #adds the player to the list players (used in the future to add multiple players)
    def add_player(self, player):
        self.players.append(player)

    def game_setup(self):
        #initializes the deck
        deck = Deck()
        #adds a full deck of cards to the 
        deck.add_cards()

        random.shuffle(deck.cards)

        #loops through all players and adds 2 cards to their hands from teh randomized deck
        if len(self.players) > 0:
            for _ in range(2):
                for player in self.players:
                    player.hand.append(deck.cards.pop(0))
        else:
            print("Add players to start game!")


# card = Card("8", "Diamonds")
# print(card)

# deck = Deck()
# deck.add_cards()
# print(deck.cards)

# random.shuffle(deck.cards)
# print(deck.cards)

# print(len(deck.cards))

# player = Player("Callum")
# print(player)

# game = Game(player)
# game.add_player(player)
# print(game.players)

#start game here
player1 = Player("Callum")
player2 = Player("Ella")

game = Game()
game.add_player(player1)
game.add_player(player2)

game.game_setup()

print(f"{player1.name} has hand {player1.hand}")
print(f"{player2.name} has hand {player2.hand}")