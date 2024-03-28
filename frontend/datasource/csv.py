import streamlit as st
import openpyxl
import pandas as pd
from pydantic import ValidationError



class CSVCollector:
    def __init__(self, schema, aws, cell_range):
        self._schema = schema
        self._aws = aws
        self._buffer = None
        self.cell_range = cell_range
        return
    
    def start(self):
        getData = self.getData()
        if getData is not None:
            extractData = self.extractData(getData)
            return extractData
    
    def getData(self):
        dados_excel = st.file_uploader("Insira o arquivo Excel", type=".xlsx")
        return dados_excel
    
    def extractData(self, dados_excel):
        '''openyxl está sendo usado apenas para pegar o range da aba'''
        workbook = openpyxl.load_workbook(dados_excel)
        sheet = workbook.active #active é a primeira aba
        range_cell = sheet[self.cell_range] #range da aba

        #pegando o meu índice 0, que é o cabeçalho
        headers = [cell.value for cell in range_cell[0]]
        
        data = []
        for row in range_cell[1:]:
            data.append([cell.value for cell in row])

        df = pd.DataFrame(data, columns=headers)
        return df    
    
    def transformDf(self, dados_excel):
        pass