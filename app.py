import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard La Liga 2021-2022")
st.write("Análisis interactivo de estadísticas de jugadores de La Liga 2021-2022")

df = pd.read_csv("2021-2022 Football Player Stats.csv", sep=";", encoding="latin-1")

laliga = df[df.Comp == "La Liga"].copy()

columnas = [
    "Player",
    "Nation",
    "Pos",
    "Squad",
    "Age",
    "MP",
    "Starts",
    "Min",
    "Goals",
    "Assists",
    "Shots",
    "SoT",
    "SoT%",
    "G/Sh",
    "PasTotCmp%",
    "PasProg",
    "Press",
    "Tkl",
    "Int",
    "DriSucc",
    "DriAtt",
    "DriSucc%",
    "CrdY",
    "CrdR",
    "AerWon%",
]

laliga = laliga[columnas]

equipos = sorted(laliga["Squad"].unique().tolist())
equipo_seleccionado = st.selectbox("Selecciona un equipo", equipos)

df_equipo = laliga[laliga.Squad == equipo_seleccionado]

st.write(f"Jugadores en plantilla: {len(df_equipo)}")
st.dataframe(df_equipo)

st.subheader(f"Top goladores de {equipo_seleccionado}")
top_goleadores = (
    df_equipo[df_equipo.Min >= 900].sort_values("Goals", ascending=False).head(10)
)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=top_goleadores, x="Goals", y="Player", palette="viridis", ax=ax)
ax.set_title(f"Goles por 90 min — {equipo_seleccionado}")
ax.set_xlabel("Goles por 90 min")
ax.set_ylabel("")
st.pyplot(fig)
plt.close()


st.subheader(f"Estadísticas medias de {equipo_seleccionado}")
col1, col2, col3, col4 = st.columns(4)

jugadores_titular = df_equipo[df_equipo.Min >= 500]
col1.metric("Jugaodores con 500+ min", len(jugadores_titular))
col2.metric("Media de goles/90", round(jugadores_titular.Goals.mean(), 2))
col3.metric("Media de asistencias/90", round(jugadores_titular.Assists.mean(), 2))
col4.metric("Media de tiros/90", round(jugadores_titular.Shots.mean(), 2))


st.subheader("Comparativa entre equipos")
col1, col2 = st.columns(2)
equipo1 = col1.selectbox("Equipo 1", equipos, index=0)
equipo2 = col2.selectbox("Equipo 2", equipos, index=1)

metrica = st.selectbox(
    "Métrica a comparar", ["Goals", "Assists", "Shots", "SoT", "Tkl", "Int", "Press"]
)

df1 = laliga[(laliga.Squad == equipo1) & (laliga.Min >= 900)]
df2 = laliga[(laliga.Squad == equipo2) & (laliga.Min >= 900)]

comparativa = pd.DataFrame(
    {
        "Equipo": [equipo1, equipo2],
        "Valor": [df1[metrica].mean().round(2), df2[metrica].mean().round(2)],
    }
)

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=comparativa, x="Equipo", y="Valor", palette="coolwarm", ax=ax)
ax.set_title(f"Comparativa: {metrica} por 90 min")
ax.set_ylabel(f"Media {metrica}/90")
st.pyplot(fig)
plt.close()
