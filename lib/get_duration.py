import requests


def _parse_duration(directions_dict):
    key = 'travelDurationTraffic'
    return directions_dict['resourceSets'][0]['resources'][0][key]


def _request_duration(base_url, config):
    payload = {'wp.0': config['origin'],
               'wp.1': config['destination'],
               'avoid': 'minimizeTolls',
               'key': config['directions_api_key']}
    r = requests.get(base_url, params=payload)
    if r.status_code is not 200:
        details = 'unavailable'
        try:
            details = r.json()['errorDetails'][0]
        except:
            pass
        message = 'Could not get data from API: Status code: {}. Details: {}'
        formatted_message = message.format(r.status_code, details)
        raise Exception(formatted_message)
    return r.json()


def get_duration(base_url, config):
    '''throws if data unavailable'''
    duration_raw = _request_duration(base_url, config)
    print(duration_raw)
    duration = _parse_duration(duration_raw)
    return duration
