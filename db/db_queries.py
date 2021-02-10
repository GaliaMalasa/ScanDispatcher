from django.db import connection
from . import configuration


def execute_get_query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def get_scan_status_by_id(scan_id):
    if scan_id:
        query = """
                SELECT {field_name} FROM {table}  
                WHERE 
                    task_id = '{task}'
                """.format(field_name="status", table=configuration.TASKS_TABLE_NAME, task=scan_id)
        return execute_get_query(query)
