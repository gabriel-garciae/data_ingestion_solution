import streamlit as st
import sys
import os
from aws.client import S3Client
from datasource.csv import CSVCollector
from contract.catalogo import Catalogo

# Adicionando o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.title("Essa é uma página de portal de dados")


aws_instancia = S3Client()
catalogo_de_produto = CSVCollector(Catalogo, aws_instancia, "C11:I211")
catalogo_de_produto.start()