import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
playing = True
#Class Player


#Class Def
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit
#Deck class
class Deck:
    
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
            deck_card = " "
            for card in self.deck:
                deck_card += " \n" + card.__str__()
            return "The deck has " + deck_card
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card
    
#Hand Class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def ace_adjust(self):
        while self.value > 21 and self.aces:
            self.value = self.value - 10
            self.aces = self.aces - 1

#Chips Class
class Chips:
    def __init__(self):

        self.totalchips = 100
        self.betchips = 0

    def win_bet(self):
        self.totalchips += self.betchips

    def lose_bet(self):
        self.totalchips -= self.betchips

#Taking a bet definition
def take_bet(chips):
    while True:
        try:
            chips.betchips = int(input("Please type how many chips you would like too bet:"))
        except:
            print("Please type a correct number of chips")
        else:
            if chips.betchips > chips.totalchips:
                print("Sorry you dont have the total chips for that! You have ", chips.player_chips)
            else:
                break

#Taking a hit def
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.ace_adjust()
    

def hit_or_stand(deck,hand):
    global playing 
    while True:
        h_s = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if h_s[0].lower() == 'h':
            hit(deck,hand)  

        elif h_s[0].lower() == 's':
            print("Player is standing, onto dealers turn.")
            playing = False

        else:
            print("Sorry! Incorrect input please try again")
            continue
        break

        


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" Card Hidden")
    print("",dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print(f"Value of your hand is: {player_hand.value}")
    
    
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n " )
    print(f"Dealers value is: {dealer_hand.value}")
    print("\nPlayer's Hand:", *player.cards, sep="\n " )
    print(f"Players value is: {player_hand.value}")
   

def player_busts(player,dealer,chips):
    print(f"Player has gone bust - your total value is {player_hand.value}")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print (f"You have won this hand! You had a value of {player_hand.value} and the dealer had {dealer_hand.value}")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print(f"Dealer has gone bust! He had a value of {dealer_hand.value}")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print(f"Dealer has won this hand! His hand had the value of {dealer_hand.value} while you had {player_hand.value}")
    chips.lose_bet()

def push(player,dealer):
    print ("Its a tie!!")



name = input("Please type your name: ")
print(f"Welcome to BlackJack {name}! The rules of the game are simple! Dont let the total value of your hand exceed 21!\n\
Aces are set to 11 unless your value exceeds 21 then will be set to 1! Enjoy and best of luck!")
while True:
    bust = False
    new_deck = Deck()
    new_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())
    player_chips = Chips()
    print(f"\n You have {player_chips.totalchips} chips")

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)
    while playing:

        hit_or_stand(new_deck,player_hand)

        show_some(player_hand,dealer_hand)
 
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            bust = True

        
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(new_deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)
    if bust == False:
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value == dealer_hand.value:
            push(player_hand,dealer_hand)

    print(f"Your chips now is {player_chips.totalchips}")
    again = input("Would you like to play again? Please type y or n")
    if again[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thank you for playing! Have a good day")
        break





        
