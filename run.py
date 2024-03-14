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
    




card = Card("8", "Diamonds")
print(card.value)