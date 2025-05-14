import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine
import pandas as pd

Session = sessionmaker(bind = engine)
session = Session()


df = pd.read_csv("./data/saludos_mundo.csv")
print("Archivo leido correctamente")

print(type(df))