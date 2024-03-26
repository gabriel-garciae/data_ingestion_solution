from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random



app = FastAPI()
fake = Faker()


file_name = 'backend/fakeapi/nova_base.csv'
df = pd.read_csv(file_name, sep=';')
df['indice'] = range(1, len(df) +1)
df.set_index('indice', inplace=True)


@app.get("/gerar_compra")
async def gerar_compra():
    index = random.randint(1, len(df)-1)
    tuple = df.iloc[index]
    return [{
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product_name": tuple["Produto"],
            "ean": int(tuple["EAN"]),
            "price": tuple["Preco"],
            "clientePosition": fake.location_on_land(),
            "store": 11,
            "dateTime": fake.iso8601()
    }]

@app.get("/gerar_compra/{numero_registros}")
async def gerar_compra(numero_registros: int):
    
    if numero_registros < 1:
        return {"Error": "O número deve ser maior que 1"}
    
    respostas = []
    for i in range(numero_registros):
        index = random.randint(1, len(df)-1)
        tuple = df.iloc[index]
        compra = {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product_name": tuple["Produto"],
            "ean": int(tuple["EAN"]),
            "price": tuple["Preco"],
            "clientePosition": fake.location_on_land(),
            "store": 11,
            "dateTime": fake.iso8601()
             }
        respostas.append(compra)

    return respostas