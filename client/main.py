import requests
import json
from .exceptions import NoActorError


URL = 'https://api.github.com/events'

"""
This will return a list of dictionary items, each of the form (but not all keys are always present):

payload: {u'size': 1,
                u'head': u'31690aa2e2b1c2167fe2919bb138a0e4a8f6d61b',
                u'commits': [{u'distinct': True,
                                      u'sha': u'31690aa2e2b1c2167fe2919bb138a0e4a8f6d61b',
                                      u'message': u'add typescript fmt\n\nfixed typo\n\nreordered packages\n\nmade formatting off by the default',
                                      u'url': u'https://api.github.com/repos/JAremko/spacemacs-pr/commits/31690aa2e2b1c2167fe2919bb138a0e4a8f6d61b',
                                      u'author': {u'email': u'w3techplayground@gmail.com',
                                                        u'name': u'JAremko'}}],
                u'distinct_size': 1,
                u'push_id': 963473093,
                u'ref': u'refs/heads/ts-fmt',
                u'before': u'1718b87877e0029f31e7f1ad2f511d9f5f35d534'}
created_at: 2016-02-04T09:32:19Z
actor: {u'url': u'https://api.github.com/users/JAremko',
            u'login': u'JAremko',
            u'avatar_url': u'https://avatars.githubusercontent.com/u/1898905?',
            u'id': 1898905,
            u'gravatar_id': u''}
id: 3606061968
repo: {u'url': u'https://api.github.com/repos/JAremko/spacemacs-pr',
           u'id': 50198025, u'name': u'JAremko/spacemacs-pr'}
type: PushEvent
public: True

"""

def get_latest_actor_from_url():
    response =  requests.get(URL)
    data =  json.loads(response.text)
    for d in data:
        if 'actor' in d:
            return get_actor(d)
    raise NoActorError(data)


def get_actor(d):
    return d['actor']['url']
