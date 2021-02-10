from .configuration import cache_twenty_minutes


def save_to_cache(scan_id):
    cache_twenty_minutes[scan_id] = 1


def is_cached(scan_id):
    print(f'{scan_id}')
    try:
        return cache_twenty_minutes.get(scan_id) is 1
    except KeyError:
        print(KeyError)
        return False
