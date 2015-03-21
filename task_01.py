#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK8 synthesizing task 01 - game simulator."""


def get_matches(players):
    """Creating a list of versus matchups for players in a game.

    Args:
        list = A list of player names.
    Returns:
        tuple = A list of the potential match-ups.

    Examples:
    >>> get_matches(['Harry', 'Howard', 'Hugh'])
    [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    >>> get_matches(['Markus', 'Atalya', 'Russell', 'AJ'])
    [('Atalya', 'AJ'), ('Atalya', 'Russell'), ('Markus', 'AJ'),
    ('Markus', 'Atalya'), ('Markus', 'Russell'), ('Russell', 'AJ')]

    """

    matchups = []
    player_list = list(enumerate(players))
    for first in player_list:
        for second in player_list:
            if first[0] < second[0]:
                matchups.append((first[1], second[1]))
    return sorted(matchups)
