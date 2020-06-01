"""
--------------------------------------
 -*- coding: utf-8 -*-
 @author: yangyd
 @file: playing_cards.py
 @time: 2019/11/27 14:35 
--------------------------------------
"""

from collections import namedtuple


Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


deck = FrenchDeck()
# for i in deck:
#     print(i)
# print([i for i in deck])
print(deck[0:5])
