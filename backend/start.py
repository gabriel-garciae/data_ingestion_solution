from datasource.api import APICollector
from contracts.schema import CompraSchema

schema = CompraSchema

minha_classe = APICollector(schema).start(3)

print(minha_classe)