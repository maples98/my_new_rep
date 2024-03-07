import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')         
     fig = px.histogram(car_data, x="odometer")    
     st.plotly_chart(fig, use_container_width=True)

hist_button_2 = st.button('Construir gráfico de dispersión') # crear un botón

if hist_button_2: # al hacer clic en el botón
     st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')      
     fig = px.scatter(car_data, x="odometer", y="price")   
     st.plotly_chart(fig, use_container_width=True)