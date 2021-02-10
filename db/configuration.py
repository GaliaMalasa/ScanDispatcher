from expiringdict import ExpiringDict

TASKS_TABLE_NAME = "django_celery_results_taskresult"
cache_twenty_minutes = ExpiringDict(max_len=100, max_age_seconds=1200)
