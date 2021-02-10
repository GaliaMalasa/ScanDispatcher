from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .scan_processor import Process
from utilities.utils import Utils
import time


@shared_task(bind=True)
def initiate_scan(self, scan_extra_details):
    """ the task is forward to the process unit
    task state would be updated by the process unit """

    self.update_state(state='PENDING')  # to simulate long waiting
    # process_task = scan_processing(scan_extra_details)
    # if process_task == "FAILURE":
    time.sleep(20)
    self.update_state(state='FAILURE', meta={'exc': "Error"})
    raise Exception("Scanning went wrong")
