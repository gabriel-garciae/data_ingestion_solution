from datasource.api import APICollector
from contracts.schema import CompraSchema
import schedule
import time

import sys
import os
from aws.client import S3Client
# Adicionando o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

schema = CompraSchema
aws = S3Client()

def apiCollector(schema, aws, repeat):
    response = APICollector(schema, aws).start(repeat)
    print("Executei")
    return

schedule.every(1).minute.do(apiCollector, schema, aws, 10)

while True:
    schedule.run_pending()
    time.sleep(10)