import json
from time import sleep
from time import time
from lib.get_duration import get_duration
from lib.persist import persist
from lib.log import log

BASE_URL = 'http://dev.virtualearth.net/REST/V1/Routes/Driving'
OUT_FILE = 'record.csv'
INTERVAL_SECONDS = 4 * 60


def main(base_url, config):

    while True:
        try:
            duration = get_duration(base_url, config)
            persist(time(), duration, OUT_FILE)
        except Exception as e:
            log(e)
        sleep(INTERVAL_SECONDS)


if __name__ == '__main__':
    config = {}
    with open('config.json', 'r') as f:
        config = json.load(f)

    main(BASE_URL, config)
