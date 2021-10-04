import random

#card
#suit, rank, Value(int)
#deck
#players
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    #initialize
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
     
    #this a string method if a want to be abble to print out the card   
    def __str__(self): 
        return self.rank + " of " + self.suit



#Deck CLASS

#Create all 52 Card objs
#hold as a list of Card objs
#shuffle deck through a methos call - Random library shuffle() function
#deal Cards from the Deck object - pop method from card list

class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    #shuffle from deck            
    def shuffle(self):
        
        random.shuffle(self.all_cards)
    
    #Pop method for cardlist    
    def deal_one(self):
        
        return self.all_cards.pop()


#Player Class

class Player():
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
        
    def add_cards(self, new_cards):
        # List of multiple cards objects
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            #for a single Card Object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'