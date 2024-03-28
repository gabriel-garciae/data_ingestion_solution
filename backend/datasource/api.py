import sys
import os
import requests
import pandas as pd
import datetime
import pyarrow.parquet as pq
from io import BytesIO
from contracts.schema import GenericSchema, CompraSchema
from typing import List

# Adicionando o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class APICollector:
    def __init__(self, schema, aws):
        self._schema = schema
        self._aws = aws
        self._buffer = None
        return
    
    def start(self, param):
        '''Está fazendo o getData e o resultado está passando o extractData para validar'''
        response = self.getData(param)
        response = self.extractData(response)
        response = self.transformDf(response)
        response = self.convertToParquet(response)

        if self._buffer is not None:
            file_name = self.fileName()
            print(file_name)
            self._aws.upload_file(response, file_name)
            return True
        
        return False
    
    def getData(self, param):
        '''Extração dos dados'''
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
    
    def transformDf(self, response):
        '''Preparação dos dados como um dataframe (mais legível para inserção em um banco)'''
        result = pd.DataFrame(response)
        return result
    
    def convertToParquet(self, response):
        self._buffer = BytesIO()
        try:
            response.to_parquet(self._buffer)
            return self._buffer
            # return response.to_parquet('exemplo.parquet', compression='snappy')
        except:
            print("Erro ao transformar o DF em parquet")
            self._buffer = None
    
    def fileName(self):
        data_atual = datetime.datetime.now().isoformat()
        match = data_atual.split(".")
        return f"api/api-response-compra{match[0]}.parquet"