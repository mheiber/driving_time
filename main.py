import json
from time import sleep
from time import time
from lib.get_duration import get_duration
from lib.persist import persist

BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json'
OUT_FILE = 'record.csv'
INTERVAL_SECONDS = 5 * 60


def main(base_url, config):

    while True:
        duration = get_duration(base_url, config)
        persist(time(), duration, OUT_FILE)
        sleep(INTERVAL_SECONDS)


if __name__ == '__main__':
    config = {}
    with open('config.json', 'r') as f:
        config = json.load(f)

    main(BASE_URL, config)
