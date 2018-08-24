#!/usr/bin/env python

import random

class Card(object)
    # TODO: refactor this
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):
        """FIXME: Move this out"""
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

    def __add__(self, other):
        """Docstring."""
        # TODO: Something
        # TODO: Something else that's really rather long and will go on to the
        # TODO2: next line
        return self.value + other.value
