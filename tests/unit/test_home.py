from API import set_flask_environment


def test_set_flask_environment():
    flask_env = set_flask_environment()
    assert type(flask_env) is str
    assert flask_env in ['development', 'production', 'test']


def test_home(client):
    resp = client.get('/api/v1')
    assert resp.status_code == 200


def test_home_bad_http_method(client):
    resp = client.post('/api/v1')
    assert resp.status_code == 405
