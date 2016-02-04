from nose.tools import assert_true

import example.client.main as main


def test_get_latest_actor_from_url_ok():
    res = main.get_latest_actor_from_url()
    assert_true(res.startswith('http'))
