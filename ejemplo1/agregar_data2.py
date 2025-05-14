import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine
import pandas as pd

Session = sessionmaker(bind = engine)
session = Session()

#Leer el archivo csv

df = pd.read_csv("./data/saludos_mundo.csv", sep='|')

# Insertar cada fila como un objeto Saludo2

for _, fila in df.iterrows():
    saludo = Saludo2(
        mensaje=fila['mensaje'],
        tipo=fila['tipo'],
        origen=fila['origen']
    )
    session.add(saludo)

session.commit()

print("Datos insertados correctamente.")