import requests


def _parse_duration(directions_dict):
    return directions_dict['routes'][0]['legs'][0]['duration']['value']


def get_duration(base_url, config):
    r = requests.get(base_url, params=config)
    duration = _parse_duration(r.json())
    return duration
