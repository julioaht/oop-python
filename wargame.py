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


# GAME LOGIC    
#game setup

#while game_on
    #while at_war   

#create players
player_one =Player("one")
player_two=Player('two')

#create new deck
new_deck = Deck()
new_deck.shuffle()

# there are 52 cards in the deck. we use 26 bc we are giving two cards at the time. 26*2=52
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one()) 

#very important lets us now if someone won or the game continues
game_on = True  

#counter to know how many rounds have been played
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')
    
    if len(player_one.all_cards) == 0:
        print('Player one is out of cards! Plater TWO WINS!')
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print('Player two is out of cards! Plater ONE WINS!')
        game_on = False
        break
        
    #start a new round
    #current cards in play. not all cards
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    