# Copyright (C) 2015 Dirk Fortmeier, Oskar Maier
#
# !TODO: licence
#
# author Dirk Fortmeier, Oskar Maier
# version d0.0.1
# since 2015-03-21
# status development

# build-in modules
from functools import wraps

# third-party modules
from werkzeug.wrappers import Request, Response
from jsonrpc import JSONRPCResponseManager, dispatcher

# own modules
from authorization import check_auth, get_playerid_by_authname
import json

# constants

# code
#####################
# default responses #
#####################
def authenticate():
    r"""
    Sends a 401 response that enables basic auth,
    """
    return Response(
                    'Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})

#####################
# provided services #
#####################
# Note: All provided services must take as first argument the player-id, which will be set by the request handler.
@dispatcher.add_method
def hold(playerid, territory):
    r"""
    Service method to register a command of type 'hold'.
    
    Parameters
    ----------
    playerid : int
        The internal id of the requesting player.
    territory : name
        Short or long name of the territory for which to execute the command.
        
    Returns
    -------
    command : string
        Complete, default-formatted command. E.g. 'A swe -> nor'
    """
    return 'player {} strives to hold in {}'.format(playerid, territory)

###################
# request handler #
###################
@Request.application
def application(request):
    # check authentication and retrieve associated player-id
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
    playerid = get_playerid_by_authname(auth.username)
    
    # modify request to contain player-id as first parameter
    request_dic = json.loads(request.data)
    request_dic['params'] = [playerid] + request_dic['params']
    request.data = json.dumps(request_dic)
    
    # parse request
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')
