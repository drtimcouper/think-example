import json

from nose.tools import assert_equal, assert_raises, assert_true
from unittest.mock import patch, Mock

import example.client.main as main
from example.client.exceptions import NoActorError


def test_get_actor_ok():
    d = {'actor': {'url': 'http://my-actor-url'}
        }
    res = main.get_actor(d)
    assert_equal(res, 'http://my-actor-url')

'''
def test_get_actor_fails_with_no_actor_key():
    with assert_raises(KeyError):
        main.get_actor({})


def test_get_actor_fails_with_no_url_key():
    d = {'actor': {}}
    with assert_raises(KeyError):
        main.get_actor(d)


def test_get_latest_actor_from_url_ok():
    with patch.object(main, 'requests') as requests:
        with patch.object(main, 'get_actor') as get_actor:
            response = Mock()
            response.text = json.dumps([{'actor': 'my actor'}])
            requests.get.return_value = response
            main.get_latest_actor_from_url()
            assert_true(get_actor.called)


def test_get_latest_actor_from_url_fails():
    with patch.object(main, 'requests') as requests:
            response = Mock()
            response.text = json.dumps([{}])
            requests.get.return_value = response
            with assert_raises(NoActorError):
                main.get_latest_actor_from_url()


# rework the above as a test class:

class Test_get_latest_actor_from_url:

    def setup(self):
        self.p_requests = patch.object(main, 'requests')
        self.requests = self.p_requests.start()

    def teardown(self):
        self.p_requests.stop()

    def test_get_latest_actor_from_url_ok(self):
        with patch.object(main, 'get_actor') as get_actor:   # could patch this in setup, too
            response = Mock()
            response.text = json.dumps([{'actor': 'my actor'}])
            self.requests.get.return_value = response
            main.get_latest_actor_from_url()
            assert_true(get_actor.called)

    def test_get_latest_actor_from_url_fails(self):
            response = Mock()
            response.text = json.dumps([{}])
            self.requests.get.return_value = response
            with assert_raises(NoActorError):
                main.get_latest_actor_from_url()
'''
