# ScanDispatcher
Dispatching Cyber scans system

A python dispatching cyber scans system for initiating cyber scan tasks on demand.
The system consists of three four main parts:
1. Ingest – for receiving multiple requests in parallel to initiate cyber scans. With a relevant id returns for each scan request by this unit, caller can tack request's status.
 
2. Process – for processing requests one by one, with option for concurrency task process
 
3. Status - for checking the status of a scan using the unique scan-id received from the ingestion system.
 
 
Implementation made with python and its following dependencies:
• django - mainly used for building the project and using Sqlite offered by it and as a web framework in the future(creating web application)
• django-celery-results- for storing celery scan tasks result ,using it in the status unit
• celery – used as a task queue (also manager) for initiate the scan tasks and process them.
• expiringdict - used to save id of scan requests for 20 minutes.

Celery allows create tasks in asynchronous way to achieve concurrency, and different thread for processing those tasks called "worker" (can be many for processing those tasks in parallel - efficiency)
I used rabbitMQ as a task queue & broker so I installed and ran it in my machine and did not used as dependency.




# To initiate a new task & process it, need to activate rabbitMQ, 
start a worker by running the command - "celery -A scan_dispatcher worker -l info --pool=solo" (if we wnat to have concurrency, then we nee to remove the --pool=solo part).
> run the main.python file (can start multiple task in parallel)
> to check for status, open python shell ans run the "Status.get_scan_status()" command.
 
