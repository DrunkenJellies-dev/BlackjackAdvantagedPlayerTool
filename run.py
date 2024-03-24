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
    def __init__(self, name, starting_credits=100):
        self.name = name
        self.hand = []
        self.score = 0
        self.credits = starting_credits
        self.bet = 0

    #returns printable representation of player's name, hand, and score 
    def __repr__(self):
        return f"{self.name}'s hand is {self.hand} with their current score being {self.score} | Credits: {self.credits}"
    
    # method to place a bet
    def place_bet(self, amount):
        if amount in [10, 25, 50, 100]:
            if amount <= self.credits:
                self.bet += amount
                self.credits -= amount
                print(f"{self.name} placed a bet of {amount} credits.")
            else:
                print("Insufficient credits. Please place a lower bet.")
        else:
            print("Invalid bet amount. Please choose from 10, 25, 50, or 100 credits.")

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

    def next_card(self, player, split = False):
        #remove a card from the top of the deck 
        card = self.deck.pop(0)

        if split:
            player.split_hand.append(card)
            player.split_score += card.value
        else:
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

        # Check for split hand and adjust score accordingly
        if split and player.split_score > 21:
            for card in player.split_hand:
                if card.rank == 'Ace':
                    card.rank = 'Ace-1'
                    player.score -= 10
                    break

    def split_cards(self, player):
        """
        Allows a player to split their cards if they have two cards of the same rank.
        """
        # Check if the player has exactly two cards and they are of the same rank
        if len(player.hand) == 2 and player.hand[0].rank == player.hand[1].rank:
            while True:
                choice = input(f"{player.name}, are you sure you want to split your cards? (y/n): ").lower()
                if choice == 'y' or choice == 'yes':
                    # Create a new hand for the split
                    split_hand = [player.hand.pop(1)]
                    player.split_score = split_hand[0].value
                    player.score -= split_hand[0].value  # Subtract the value of the split card from the original hand
                    player.split_hand = split_hand
                    # Draw a new card for each hand
                    self.next_card(player)
                    self.next_card(player, split=True)  # For the split hand
                    print(f"{player.name} has split their cards.")
                    break
                elif choice == 'n' or choice == 'no':
                    break
                else:
                    print("Invalid choice. Please enter 'y' or 'n'.")
        else:
            print(f"Sorry {player.name}, your unable to split your cards. You need two cards of the same rank.")


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

        #Adding the dealer
        list_players.append(Player('Dealer'))

        # ask players to place bets
        for player in list_players[:-1]:  # Excluding the dealer
            while True:
                try: 
                    bet_amount = int(input(f"{player.name}, please place your bet (10, 25, 50, or 100): "))
                    current_bet = player.credits
                    player.place_bet(bet_amount)
                    if player.credits < current_bet:
                        break
                    else:
                        print(f"{player.name} entered an invalid betting amount. Please enter a valid betting amount.")
                except ValueError as e:
                    print(f"Invalid data: {e}, please try again.\n")

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

        num_players_without_dealer = len(game.players) - 1

        #Show hand for each player
        for player_num in range(num_players_without_dealer):
            print(f"{game.players[player_num].name} has a {game.players[player_num].hand[0]} and a {game.players[player_num].hand[1]}\nTheir score is currently {game.players[player_num].score}")

        #Print statement for the dealer as the players aren't normally able ot see their second card until the dealer starts playing
        print(f"{game.players[-1].name} has a {game.players[-1].hand[0]} and X.\nTheir score is currently {game.players[-1].score - game.players[-1].hand[1].value}")
        
        #ask if the player wants to hit or stand
        player_want_cards = num_players_without_dealer #removing 1 player due to the dealer now being a member of the players

        #game stops if all players stand
        while player_want_cards > 0:
            for player in game.players[0 : -1]:
                valid = 1
                while valid == 1:
                    if player.score > 21:
                        answer = 's'
                    else:
                        answer = input(f"{player.name} would you like to (h)it, (s)tand, (d)ouble or (sp)lit?").lower()
                        print()
                    if answer == 'h' or answer == 'hit':
                        game.next_card(player)
                        valid = 0
                        print(f"{player.name} received a {player.hand[-1]}.\nYour score is now {player.score}.")
                    elif answer == 's' or answer == 'stand':
                        valid = 0
                        player_want_cards -= 1
                    elif answer == 'd' or answer == 'double':
                        if player.credits >= player.bet:  # Can only double on initial hand with enough credits
                            player.place_bet(player.bet)  # Double the bet
                            game.next_card(player)
                            valid = 0
                            player_want_cards -= 1
                            print(f"{player.name} doubled down and received a {player.hand[-1]}.\nYour score is now {player.score}.")
                        else:
                            print("You cannot double down at this time.")
                    elif answer == 'sp' or answer == 'split':
                        game.split_cards(player)

                        if not hasattr(player, 'split_hand'):
                            valid = 1
                        else:
                            valid = 0

                        while hasattr(player, 'split_hand'):
                            choice = input(f"{player.name}, do you want to hit or stand for your split hand? (h/s): ").lower()
                            if choice == 'h' or choice == 'hit':
                                game.next_card(player, split=True)
                                print(f"{player.name} received a {player.split_hand[-1]} for their split hand.\nYour split score is now {player.split_score}.")
                            elif choice == 's' or choice == 'stand':
                                break
                            else:
                                print("Invalid choice. Please enter 'h' or 's'.")
                    else:
                        valid = 1

        #revealed the dealers second card
        print(f"{game.players[-1].name} reveals their second card which was a {game.players[-1].hand[1]}.\nTheir score is now {game.players[-1].score}.")

        #The dealer plays cards in accordance to standard blackjack rules (dealer keeps 'hitting' until their score is 17 or greater)
        while game.players[-1].score < 17:
            #Adds card to the dealers hand
            game.next_card(game.players[-1])
            print(f"{game.players[-1].name} has drawn a {game.players[-1].hand[-1]}.\nTheir score is now {game.players[-1].score}")
            if game.players[-1].score >= 17:
                print(f"{game.players[-1].name} now stands.")

        #Decides the winner for the round 
        for player in game.players[0 : -1]:
            if player.score > 21:
                print(f"{player.name} is bust with the score {player.score}.")
                player.bet = 0  # Player loses their bet
            elif game.players[-1].score > 21:
                print(f"{player.name} wins with score {player.score}.\n{game.players[-1].name} is bust with score {game.players[-1].score}.")
                player.credits += 2 * player.bet  # Player wins double the bet
                player.bet = 0
            elif player.score > game.players[-1].score:
                print(f"{player.name} wins with score {player.score}.\n{game.players[-1].name} has score {game.players[-1].score}.")
                player.credits += 2 * player.bet  # Player wins double the bet
                player.bet = 0
            elif player.score == game.players[-1].score:
                print(f"{player.name} draws with score {player.score}.\n{game.players[-1].name} has score {game.players[-1].score}.")
                player.credits += player.bet  # Player gets back their bet
                player.bet = 0
            else:
                print(f"{player.name} has lost with score {player.score}.\n{game.players[-1].name} has score {game.players[-1].score}.")
                player.bet = 0  # Player loses their bet

            # Determine outcome for split hand
            if hasattr(player, 'split_hand'):
                if player.split_score > 21:
                    print(f"{player.name}'s split hand is bust with the score {player.split_score}.")
                    player.bet = 0  # Player loses their split bet
                elif game.players[-1].score > 21:
                    print(f"{player.name}'s split hand wins with score {player.split_score}.\n{game.players[-1].name} is bust with score {game.players[-1].score}.")
                    player.credits += 2 * player.bet  # Player wins double the split bet
                elif player.split_score > game.players[-1].score:
                    print(f"{player.name}'s split hand wins with score {player.split_score}.\n{game.players[-1].name} has score {game.players[-1].score}.")
                    player.credits += 2 * player.bet  # Player wins double the split bet
                elif player.split_score == game.players[-1].score:
                    print(f"{player.name}'s split hand draws with score {player.split_score}.\n{game.players[-1].name} has score {game.players[-1].score}.")
                    player.credits += player.bet  # Player gets back their split bet
                else:
                    print(f"{player.name}'s split hand has lost with score {player.split_score}.\n{game.players[-1].name} has score {game.players[-1].score}.")
                    player.bet = 0  # Player loses their split bet

        for player in game.players[0 : -1]:
            print(f"{player.name} ended with {player.credits} credits.")

            
                    

                

#start game
display = Display()

#Add players
list_players = display.add_players()

#play the first round
display.play_game(list_players)
