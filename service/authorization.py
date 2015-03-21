# Copyright (C) 2015 Dirk Fortmeier, Oskar Maier
#
# !TODO: licence
#
# author Dirk Fortmeier, Oskar Maier
# version d0.0.1
# since 2015-03-21
# status development

# build-in modules

# third-party modules

# own modules

# constants
PLAYERS = {
           'loli': 
                {'playerid': 0,
                 'nation': "France",
                 'password': "loli"},
           'forstschneider':
                {'playerid': 1,
                 'nation': "Germany",
                 'password': "forstschneider"}
           }

# code
def check_auth(username, password):
    r"""
    Check for a valid username-password combination.
    """
    return username in PLAYERS and PLAYERS[username]['password'] == password

def get_playerid_by_authname(username):
    r"""
    Return the player-id associated with a username.
    """
    return PLAYERS[username]['playerid']