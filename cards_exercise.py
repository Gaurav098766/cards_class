from random import shuffle as sh 

class Card:

    value_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    def __init__(self,value,suits):
        self.value = value
        self.suits = suits

    def __repr__(self) -> str:
        return f"{self.value} of {self.suits}"
    
class Deck:

    def __init__(self):
        suits = ['Hearts','Diamonds','Clubs', 'Spades']
        value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(v,suit) for suit in suits for v in value]

    def count(self):
        return len(self.cards)
    
    def __repr__(self) -> str:
        return f"Deck of {self.count()} cards"
    
    def _deal(self,number):
        if self.cards==0:
            raise ValueError(f"All cards have been dealt.")
        for i in range(0,min(number,self.count())):
            self.cards.pop()
        return self.cards
    
    def shuffle(self):
        if self.count()<52:
            raise ValueError(f"Only full deck of cards can be shuffled")
        sh(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,hand_size):
        return self._deal(hand_size)
    

d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(hand)
card3 = d.deal_card()
print(card3)

    
        

