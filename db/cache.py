from .configuration import cache_twenty_minutes


def save_to_cache(scan_id):
    cache_twenty_minutes[scan_id] = 1


def is_cached(scan_id):
    try:
        return scan_id in cache_twenty_minutes
    except KeyError:
        print(KeyError)
        return False
