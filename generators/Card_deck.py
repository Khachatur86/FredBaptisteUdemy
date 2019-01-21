from collections import namedtuple

Card = namedtuple("Card", "rank suit")
SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
RANKS = tuple(range(1, 11)) + tuple("JQKA")

def card_gen():
  for i in range(len(SUITS) * len(RANKS)):
    suit = SUITS[i // len(RANKS)]
    rank = RANKS[i % len(RANKS)]
    card = Card(rank, suit)
    yield card

# a = card_gen()
# for card in a:
#   print(card)

# print(list(a))

class CardDeck:
  SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
  RANKS = tuple(range(1, 11)) + tuple("JQKA")

  def __iter__(self):
    return CardDeck.card_gen()
  
  def __reversed__(self):
    return CardDeck.reversed_card_gen()

  @staticmethod
  def card_gen():
    for suit in CardDeck.SUITS:
      for rank in CardDeck.RANKS:
        yield Card(rank, suit)
  
  @staticmethod
  def reversed_card_gen():
    for suit in reversed(CardDeck.SUITS):
      for rank in reversed(CardDeck.RANKS):
        yield CardDeck(rank, suit)

deck = CardDeck()

print(list(deck))
print(list(deck))