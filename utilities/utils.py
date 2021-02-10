class Utils:
    @staticmethod
    def convert_scan_status(status):
        return {
            "PENDING": "Accepted",
            "STARTED": "Running",
            "FAILURE": "Error",
            "SUCCESS": "Complete",
            "NOT_FOUND": "Not-Found"
        }[status]
