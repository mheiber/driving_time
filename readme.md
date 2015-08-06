# Drive Time #

Records driving travel time between two points every five minutes.
I plan to use this to time my commute so I miss the worst traffic.

## Instructions ##

1. Get a Bing Directions API key
2. Edit `config.json` to include:
    - Your API key
    - Origin
    - Destination
3. Run like this: `python3 main.py`

> This requires Python 3

4. View output in `records.csv` (created automatically)

> The format of `records.csv` is | seconds since 1970 | Travel duration in seconds |


