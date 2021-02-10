from ingest.scan_initiator import Ingest
from db.cache import is_cached

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(1):
        print(Ingest.create_scan_task('rul'))