import redis
import requests

# response = requests.get(
#         "https://openexchangerates.org/api/latest.json?app_id=a3858beadb2347b8bfb2bcd326d4316a")
# if response.status_code == 200:
#         dict_rates = response.json()['rates']
#         print(type(dict_rates))
#         print(dict_rates['USD'])


def update_values_rate() -> dict:
    response = requests.get(
        "https://openexchangerates.org/api/latest.json?app_id=a3858beadb2347b8bfb2bcd326d4316a")
    if response.status_code == 200:
        dict_rates = response.json()['rates']

        conn = redis.Redis()

        for key, value in dict_rates.items():
            conn.set(key, value)

        return dict_rates
