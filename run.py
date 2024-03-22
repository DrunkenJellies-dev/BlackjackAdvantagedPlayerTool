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

    #initializes a list of players, current scores and the deck
    def __init__(self):
        self.players = []
        self.scores = []
        self.deck = []
        
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

        #Update deck within the game instance
            self.deck = deck.cards

        #Adjusting the score of the players cards due to special case scenario
        for player in self.players:
            #If the player gets drawn 2 aces
            if player.score == 22:
                #Sets the first ace to a 1 
                #(blackjack aces can be either have a value of 1 or 11 depending if the player has gone over 21)
                player.hand[0].rank = "Ace-1"
                #sets the players score to 12 
                #(One Ace having the value of 1 and the second ace having the value of 11)
                player.score = 12
            self.scores.append(player.score)

    def next_card(self, player):
        #remove a card from the top of the deck 
        card = self.deck.cards.pop(0)
        player.hand.append(card)
        player.score += card.value

        #checks if the player has gone over 
        if player.score > 21:
            #loops through all the cards in the players hand
            for card in player.hand:
                #checks if the players hasa hard ace in their hand
                if card.rank == 'Ace':
                    #changes the hard ace to a soft ace
                    card.rank = 'Ace-1'
                    player.score -= 10
                    break


class Display():
    """
    Class Display used for displaying information to the user at the beginning of the game when setting up  
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
        #getting the number of players from the user
        player_count = None
        while True:
            print("Please enter the number of players. (There can only be between 1-6 players)")
            print("The amount of players will alter the strategy suggested.")
            #takes the users input
            player_count = input("Enter the player count here: \n")

            #making sure the information that the player has given is within the correct parameters
            if validate_data(player_count):
                #letting the players know the amount they have selected
                print(f"You have selected: {player_count}.")
                #breaking out of the true while loop as the information is correct
                break
            
        #storing the amount of players as an integer
        player_count = int(player_count)

        #initializing the list of players 
        list_players = []

        #loops through each player and allows them to enter a name
        for player in range(player_count):
            name = input(f"Player { player + 1 } please enter your name: ")
            #adds the newly created player to the list 
            list_players.append(Player(name))

        #returns the list of players
        return list_players
    
    def play_game(self, list_players):
        #starting the instance of the game
        game = Game()
        #Adding the players
        for player in list_players:
            game.add_player(player)

        #Play the first round
        game.game_setup()

        #Show hand for each player
        for player in game.players:
            print(f"{player.name} has a {player.hand[0]} and a {player.hand[1]}\nTheir score is currently {player.score}")
        
        


#start game
display = Display()

#Add players
list_players = display.add_players()

#play the first round
display.play_game(list_players)