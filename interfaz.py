import streamlit as st
import pandas as pd
import plotly.express as px

# Cargamos el dataframe desde un CSV
dfDatos = pd.read_csv('download.csv')  # Cambia la URL al archivo correcto
dfExport= pd.read_csv("export.csv")
dfImport = pd.read_csv("import.csv")

# Definimos los parámetros de configuración de la aplicación
st.set_page_config(
    page_title="Análisis de Comercio en venezuela",  # Título de la página
    page_icon="📈",  # Ícono
    layout="wide",  # Forma de layout ancho o compacto
    initial_sidebar_state="expanded"  # Sidebar expandido
)

# Declaramos los parámetros en la barra lateral
with st.sidebar:
    parAno = st.selectbox('Año', options=dfDatos['Year'].unique(), index=0)  # Cambia 'Year' según tu dataset
    parPais = st.multiselect('País', options=dfExport['Country'].unique())  # Cambia 'Country' según tu dataset

# Aplicamos los filtros
if parAno:
    dfDatoss = dfDatos[dfDatos['Year'] == parAno]

if len(parPais) > 0:
    dfExport = dfExport[dfExport['Country'].isin(parPais)]
    dfImport = dfImport[dfImport['Year'] == parAno]


# Título principal
st.header("Proyecto FAVFIX")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Análisis de Comercio Internacional en venezuela</h1>", unsafe_allow_html=True)


st.markdown("<h2 style='text-align: center; color: #555;'>Bienvenido a la Aplicación</h2>", unsafe_allow_html=True)

# Descripción
st.markdown("<h3 style='text-align: center; color: #777;'>Explora los datos de comercio por año y sección</h3>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #4CAF50;'>", unsafe_allow_html=True)

# Métricas
c1, c2 = st.columns(2)
with c1:
    total_comercio = dfDatoss['Trade Value'].sum()  # Cambia 'Trade Value' según tu dataset
    st.metric("Valor Total de Comercio", f'US$ {total_comercio:,.0f}')

with c2:
    total_paises = dfExport['Country'].nunique()  # Cambia 'Country' según tu dataset
    st.metric("Número de Países que comercian con venezuela",f'{total_paises}')
    


# Gráficos
st.subheader('Evolución del Comercio del 2002 al 2022')
fig = px.line(dfDatos.groupby('Year').agg({'Trade Value': 'sum'}).reset_index(), x='Year', y='Trade Value', title='Evolución del Comercio', labels={'Trade Value': 'Valor del Comercio', 'Year': 'Año'})
st.plotly_chart(fig, use_container_width=True)

df_analisis_seccion = dfDatoss.groupby('Section').agg({'Trade Value': 'sum'}).reset_index()

st.subheader('gasto de seccion en el año')
# Crear la gráfica usando Plotly
fig = px.bar(df_analisis_seccion, x='Section', y='Trade Value', title=f'Análisis de Comercio por Sección en {parAno}', 
             labels={'Trade Value': 'Valor del Comercio', 'Section': 'Sección'}, 
             color='Trade Value', 
             text='Trade Value')

# Mostrar la gráfica
st.plotly_chart(fig, use_container_width=True)

# Gráfico de comercio por país
st.subheader('Exportaciones e Importaciones por País')
fig_pais = px.bar(dfExport.groupby('Country').agg({'Trade Value': 'sum'}).reset_index(), x='Country', y='Trade Value', title='Comercio por País', color='Country', text_auto=',.0f', labels={'Trade Value': 'Valor del Comercio', 'Country': 'Pais'})
st.plotly_chart(fig_pais, use_container_width=True)



st.subheader('Importaciones por País')
# Agrupar por sección y sumar Trade Value para importaciones
df_analisis_seccion_import = dfImport.groupby('Country').agg({'Trade Value': 'sum'}).reset_index()

# Crear la gráfica usando Plotly para importaciones
fig_import = px.bar(df_analisis_seccion_import, x='Country', y='Trade Value', title=f'Análisis de Importaciones por Sección en {parAno}', 
                     color='Country', text_auto=',.0f', labels={'Trade Value': 'Valor del Comercio', 'Country': 'Pais'})

# Mostrar la gráfica
st.plotly_chart(fig_import, use_container_width=True)

# Mostramos las tablas de top de secciones
c1, c2 = st.columns(2)

# Agrupar por sección y sumar Trade Value
dfSeccionesVentas = dfDatoss.groupby('Section').agg({'Trade Value': 'sum'}).reset_index()

with c1:    
    st.subheader('Top 10 secciones con mayor ganancia')
    st.table(dfSeccionesVentas.sort_values(by='Trade Value', ascending=False).head(10)[['Section', 'Trade Value']].reset_index())

with c2:    
    st.subheader('Top 10 secciones con menor ganancia')    
    st.table(dfSeccionesVentas.sort_values(by='Trade Value').head(10)[['Section', 'Trade Value']].reset_index())
    
# Agrupar por sección y sumar Trade Value
dfSeccionesVentas = dfDatos.groupby('Section').agg({'Trade Value': 'sum'}).reset_index()

with c1:    
    st.subheader('Top 10 secciones con mayor ganancia de todos los tiempos')
    st.table(dfSeccionesVentas.sort_values(by='Trade Value', ascending=False).head(10)[['Section', 'Trade Value']].reset_index())

with c2:    
    st.subheader('Top 10 secciones con menor ganancia de todos los tiempos')    
    st.table(dfSeccionesVentas.sort_values(by='Trade Value').head(10)[['Section', 'Trade Value']].reset_index())
    
# Mostramos las tablas de top de países
c1, c2 = st.columns(2)

# Agrupar por país y sumar Trade Value para exportaciones
dfPaisesExport = dfExport.groupby('Country').agg({'Trade Value': 'sum'}).reset_index()

with c1:    
    st.subheader('Top 10 países con mayor exportación')
    st.table(dfPaisesExport.sort_values(by='Trade Value', ascending=False).head(10)[['Country', 'Trade Value']].reset_index())

with c2:    
    st.subheader('Top 10 países con menor exportación')    
    st.table(dfPaisesExport.sort_values(by='Trade Value').head(10)[['Country', 'Trade Value']].reset_index())
    
    
# Mostramos las tablas de top de países
c1, c2 = st.columns(2)

# Agrupar por país y sumar Trade Value para exportaciones
dfPaisesImport = dfImport.groupby('Country').agg({'Trade Value': 'sum'}).reset_index()

with c1:    
    st.subheader('Top 10 países con mayor importación')
    st.table(dfPaisesImport.sort_values(by='Trade Value', ascending=False).head(10)[['Country', 'Trade Value']].reset_index())

with c2:    
    st.subheader('Top 10 países con menor importación')    
    st.table(dfPaisesImport.sort_values(by='Trade Value').head(10)[['Country', 'Trade Value']].reset_index())




analisis_por_año = dfDatos.groupby('Year')['Trade Value'].agg([
    ('Total', 'sum'),
    ('Promedio', 'mean'),
    ('Cantidad_Registros', 'count')
]).round(2)

analisis_por_seccion = dfDatos.groupby('Section')['Trade Value'].agg([
    ('Total', 'sum'),
    ('Promedio', 'mean'),
    ('Cantidad_Registros', 'count')
]).round(2)
    
# Estadísticas generales
st.subheader("Estadísticas Generales")

# Año con mayor comercio
año_mayor_comercio = analisis_por_año['Total'].idxmax()
valor_mayor_comercio = analisis_por_año['Total'].max()

# Año con menor comercio
año_menor_comercio = analisis_por_año['Total'].idxmin()
valor_menor_comercio = analisis_por_año['Total'].min()

# Sección con mayor comercio
seccion_mayor_comercio = analisis_por_seccion['Total'].idxmax()
valor_seccion_mayor_comercio = analisis_por_seccion['Total'].max()

# Sección con menor comercio
seccion_menor_comercio = analisis_por_seccion['Total'].idxmin()
valor_seccion_menor_comercio = analisis_por_seccion['Total'].min()

# Mostrar las métricas
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Año con Mayor Comercio", value=f"{año_mayor_comercio} (${valor_mayor_comercio:,.2f})")

with col2:
    st.metric(label="Año con Menor Comercio", value=f"{año_menor_comercio} (${valor_menor_comercio:,.2f})")

col3, col4 = st.columns(2)

with col3:
    st.metric(label="Sección con Mayor Comercio", value=f"{seccion_mayor_comercio} (${valor_seccion_mayor_comercio:,.2f})")

with col4:
    st.metric(label="Sección con Menor Comercio", value=f"{seccion_menor_comercio} (${valor_seccion_menor_comercio:,.2f})")
    

# 3. Heatmap de comercio por año y las top 5 secciones
top_5_secciones = analisis_por_seccion.nlargest(5, 'Total').index.tolist()  # Cambia a .index para obtener las secciones
datos_heatmap = dfDatos[dfDatos['Section'].isin(top_5_secciones)]

# Crear la tabla dinámica
pivot_table = datos_heatmap.pivot_table(
    values='Trade Value', 
    index='Year',
    columns='Section',
    aggfunc='sum'
).fillna(0)  # Rellenar NaN con 0 para evitar problemas en el heatmap

# Crear el heatmap usando Plotly
fig_heatmap = px.imshow(
    pivot_table,
    labels=dict(x="Sección", y="Año", color="Valor del Comercio"),
    x=pivot_table.columns,
    y=pivot_table.index,
    color_continuous_scale='YlOrRd',
    title='Heatmap de Comercio: Top 5 Secciones por Año'
)

# Mostrar el heatmap en Streamlit
st.plotly_chart(fig_heatmap, use_container_width=True)
