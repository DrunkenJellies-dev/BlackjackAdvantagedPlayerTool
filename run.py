import random 

def validate_data(value):
    """
    Used to validate the data of the amount of players
    The amount of players needs to be an integer
    The amount of players also need to be between 1 and 6
    """
    try:
        if not (1 <= int(value) <= 6):
            raise ValueError(
                f"The integer has to be between 1 and 6, you provided {value}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


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
        self.scores = []
        
    #adds the player to the list players (used in the future to add multiple players)
    def add_player(self, player):
        self.players.append(player)

    def game_setup(self):
        #initializes the deck
        deck = Deck()
        #adds a full deck of cards to the deck
        deck.add_cards()

        #shuffles the deck of cards
        random.shuffle(deck.cards)

        #loops through all players and adds 2 cards to their hands from the shuffled deck
        if len(self.players) > 0:
            #using a loop like this will deal the cards in a way that is standard at a real black jack table (Not two cards for each player at a time)
            for _ in range(2):
                for player in self.players:
                    #stores and removes the first card from the shuffled deck
                    card = deck.cards.pop(0)
                    #adds the card to the current players hand
                    player.hand.append(card)
                    #adds the value of the card drawn to the players hand
                    player.score += card.value
        else:
            #Error validation if there are no players
            print("Add players to start game!")

        #Adjusting the score of the players cards due to special case scenario
        for player in self.players:
            #If the player gets drawn 2 aces
            if player.score == 22:
                #Sets the first ace to a 1 
                #(blackjack aces can be either have a value of 1 or 11 depending if the player has gone over 21)
                player.hand[0].rank = "1"
                #sets the players score to 12 
                #(One Ace having the value of 1 and the second ace having the value of 11)
                player.score = 12
            self.scores.append(player.score)

class Display():
    """
    Class Display creating the menu screen and adds the amount of players that are playing 
    """
    def __init__(self):
        print("""
                 .-~~-.           /\        _     _            _    _            _             /\        .-~~~-__-~~~-.
                {      }        .'  `.     | |   | |          | |  (_)          | |          .'  `.     {              }
             .-~-.    .-~-.    '      `.   | |__ | | __ _  ___| | ___  __ _  ___| | __      '      `.    `.          .'
            {              } <          >  | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /   .'          `.    `.      .'
             `.__.'||`.__.'   `.      .'   | |_) | | (_| | (__|   <| | (_| | (__|   <   {              }     `.  .'
                   ||           `.  .'     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\   ~-...-||-...-~        \/
                  '--`            \/                              _/ |                         ||
                                                                 |__/                         '--`
            """)
        
    def add_players(self):
        #getting the number of players
        player_count = None
        while True:
            print("Please enter the number of players. (There can only be between 1-6 players)")
            print("The amount of players will alter the strategy suggested.")
            player_count = input("Enter the player count here: \n")

            if validate_data(player_count):
                print(f"You have selected: {player_count}.")
                break
            
        player_count = int(player_count)

        

                
                




        

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

# print(f"{player1.name} has hand {player1.hand}")
# print(f"{player2.name} has hand {player2.hand}")

for player in game.players:
    print(f"{player.name} has hand {player.hand}.\n This gives score {player.score}")