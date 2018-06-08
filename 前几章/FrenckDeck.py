import collections
from random import choice

Card=collections.namedtuple(typename='Card',field_names=['rank','suit'])

class FrenckDeck:
    ranks=[str(n) for n in range(2,11)]+ list('JQKA')
    suits='spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card=[Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

beer_card=Card('7','diamonds')
print(beer_card)

deck=FrenckDeck()
print(len(deck))

print(choice(deck))

# 实现 __getitem__ 方法，该类变为可迭代形式
# for card in deck:
#     print(card)

print(Card('7','hearts') in deck)
print(Card('7','beasts') in deck)

print('扑克排序')
suit_values=dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    print(card.rank)
    rank_value=FrenckDeck.ranks.index(card.rank)
    print(rank_value)
    return rank_value*len(suit_values)+suit_values[card.suit]

# Return a new list containing all items from the iterable in ascending order.
for card in sorted(deck,key=spades_high):
    print(card)