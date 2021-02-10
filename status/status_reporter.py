from db.db_queries import get_scan_status_by_id
from utilities.utils import Utils
from db.cache import is_cached


# check status endpoint
class Status:
    @staticmethod
    def get_scan_status(scan_id):
        scan_status_from_db = get_scan_status_by_id(scan_id)

        if scan_status_from_db:
            current_status = Utils.convert_scan_status(scan_status_from_db[0][0])
        else:  # Check if task is cached for 20 minutes
            if is_cached(scan_id):
                current_status = Utils.convert_scan_status("PENDING")
            else:
                current_status = Utils.convert_scan_status("NOT_FOUND")
        return current_status
