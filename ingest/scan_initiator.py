from process.tasks import initiate_scan
from db.cache import save_to_cache


class Ingest:
    @staticmethod
    def create_scan_task(scan_extra_details):
        try:
            current_task = initiate_scan.delay(scan_extra_details)
            if current_task is not None:
                save_to_cache(current_task.task_id)
                return f'Scan task accepted! please check status with id {current_task.task_id}'
        except IOError:  # or any other optional errors
            print("ERROR, task was not was created")
