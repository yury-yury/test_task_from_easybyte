from typing import Optional

import redis

from change_currency.parser import update_values_rate


def get_rate(name_currency: str) -> Optional[float]:
    conn = redis.Redis()

    rate = conn.get(name_currency)

    if rate is None:
        exist_rates = update_values_rate()
        rate = exist_rates.get(name_currency, None)

    return rate


if __name__ == '__main__':
    get_rate('1')
