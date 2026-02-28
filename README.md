# Dashboard Interactivo — La Liga 2021-22

Aplicación web interactiva para explorar estadísticas de jugadores de La Liga española 
en la temporada 2021-22. Construida con Python y Streamlit.

## 🔗 Demo en vivo
[Ver dashboard](https://dashboardlaliga-avuyyuzyxysorjmszpqx7v.streamlit.app/)

## ¿Qué puedes explorar?

- **Plantilla por equipo**: filtra cualquier equipo de La Liga y ve todos sus jugadores 
  con sus estadísticas completas
- **Métricas clave**: resumen de goles, asistencias y tiros medios por equipo
- **Top goleadores**: ranking de los jugadores más goleadores por 90 minutos 
  del equipo seleccionado
- **Comparativa entre equipos**: compara cualquier métrica entre dos equipos 
  de forma visual

## Datos

Dataset de estadísticas de jugadores de las 5 grandes ligas europeas 2021-22, 
obtenido de Kaggle. 617 jugadores de La Liga con 25 variables seleccionadas 
sobre rendimiento ofensivo, defensivo y disciplinario.

## Tecnologías

- Python
- Pandas
- Matplotlib / Seaborn
- Streamlit

## Ejecutar en local
```bash
pip install -r requirements.txt
streamlit run app.py
```
