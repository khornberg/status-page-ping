ping
====

### Setup

1. Clone this repo
1. Install the `npm` modules
1. Install the `pip` packages
1. Edit the URL(s) you want to ping in [ping.py](ping.py) or pass a list of them in [handler.py](handler.py).

### Deploy

Deploy this to a serverless provider. By default this is set up for AWS via [serverless](https://serverless.com/).

### Request

Send GET requests to get the results of the "ping" for each of the urls you have specified.

### Response

The response looks like

```
[
    {
        "elasped": 0.2628006935119629, // in seconds
        "reason": "OK",
        "status": 200,
        "url": "http://python.org"
    } // an object is returned for each url
]
```

### Testing

1. Install the requirements from [requirements-test.txt](requirements-test.txt)
1. Run with `pytest`


Part of [status-page](https://github.com/khornberg/status-page)

