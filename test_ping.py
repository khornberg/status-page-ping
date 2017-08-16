from datetime import datetime
from ping import get


class TestPing():

    def test_ping(self):
        results = get()
        result = results[0]
        assert result['status'] == 200
        assert result['reason'] == 'OK'
        assert result['url'] == 'http://python.org'
        assert abs(0.3 - result['elasped']) < 1
        assert abs(datetime.utcnow().timestamp() - result['dtg']) < 1

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
