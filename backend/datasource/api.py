import sys
import os
import requests
from contracts.schema import GenericSchema, CompraSchema
from typing import List

# Adicionando o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# O restante do seu código



class APICollector:
    def __init__(self, schema):
        self._schema = schema
        self._aws = None
        self._buffer = None
        return
    
    def start(self, param):
        '''Está fazendo o getData e o resultado está passando o extractData para validar'''
        response = self.getData(param)
        resp = self.extractData(response)
        return resp
    
    def getData(self, param):
        response = None
        if param > 1:
            response = requests.get(f'http://127.0.0.1:8000/gerar_compra/{param}').json()
        else:
            response = requests.get(f'http://127.0.0.1:8000/gerar_compra').json()
        return response
    
    def extractData(self, response):
        '''Validar se os dados estão sendo coletados corretamente, de acordo com o passado em contracts schema'''
        result: List[GenericSchema] = []
        for item in response:
            index = {}
            for key, value in self._schema.items():
                if type(item.get(key)) == value:
                    index[key] = item[key]
                else:
                    index[key] = None
            result.append(index)
        return result
    
    def transformDf(self):
        return