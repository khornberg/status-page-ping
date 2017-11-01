from datetime import datetime
from ping import get, make_408


class TestPing():

    def test_ping(self):
        results = get()
        result = results[0]
        assert result['status'] == 200
        assert result['reason'] == 'OK'
        assert result['url'] == 'http://python.org'
        assert abs(0.3 - result['elasped']) < 1
        assert abs(datetime.utcnow().timestamp() - result['dtg']) < 6

    def test_ping_multiple(self):
        results = get(['http://python.org', 'https://pypi.org', 'https://khornberg.github.io'])
        result = results[0]
        assert result['status'] == 200
        assert result['reason'] == 'OK'
        assert result['url'] == 'http://python.org'
        assert abs(0.3 - result['elasped']) < 0.3
        result = results[1]
        assert result['status'] == 200
        assert result['reason'] == 'OK'
        assert result['url'] == 'https://pypi.org'
        assert abs(0.1 - result['elasped']) < 0.5
        result = results[2]
        assert result['status'] == 200
        assert result['reason'] == 'OK'
        assert result['url'] == 'https://khornberg.github.io'
        assert abs(0.1 - result['elasped']) < 0.3

    def test_ping_404(self):
        results = get(['http://example.com/404'])
        result = results[0]
        assert result['status'] == 404
        assert result['reason'] == 'Not Found'
        assert result['url'] == 'http://example.com/404'
        assert result['elasped'] < 4

    def test_making_408_timeout_response(self):
        result = make_408('http://example.com/timeout')
        assert result.status == 408
        assert result.reason == 'Request Timeout'
        assert result.url == 'http://example.com/timeout'
        assert result.headers.get('Date')
