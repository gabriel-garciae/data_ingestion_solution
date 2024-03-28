from datasource.api import APICollector
from contracts.schema import CompraSchema
from aws import S3Client

import schedule
import time

schema = CompraSchema
aws = S3Client()

def apiCollector(schema, aws, repeat):
    response = APICollector(schema, aws).start(repeat)
    print("Executei")
    return

schedule.every(1).minute.do(apiCollector, schema, aws, 50)

while True:
    schedule.run_pending()
    time.sleep(1)