#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK8 synthesizing task 02 - password authentication."""

import authentication
import getpass


def login(username, maxattempts=1):
    """Implementing something that resembles the structure of a login or
    authentication screen.

    Args:
        str: A string representing the username of the user attempting to
        log in.

        int (optional): An integer represent the maximum number of
        prompted attempts before the function returns False.

    Returns:
        Returns True if the user has successfully authenticated before hitting
        the maximum number of attempts or False if they exceed that maximum
        number of failed attempts.

    Examples:



    """
    authenticated = False
    prompt = 'Please enter your password: '
    response = 'Incorrect username or password. You have {} attempts left.'
    i = 1
    while i <= maxattempts:
        password = getpass.getpass(prompt)
        if authentication.authenticate(username, password):
            authenticated = True
            break
        else:
            print response.format(maxattempts - i)
            i += 1
    return authenticated
