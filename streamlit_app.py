import streamlit as st
import pandas as pd

st.markdown("### Элементы отображения — веб-приложение на Python. Урок Streamlit 3.")


table = ({"Column 1":[1,2,3,4,5],
		  "Column 2":[6,7,8,9,10]})

#таблица с помощью streamlit (только отобразить)
st.table(table)
st.dataframe(table)

#таблица с помощью pandas (до таго как отобразить можно настроить)
df = pd.DataFrame(table)
df = df[df["Column 1"] > 2]  #условия 
st.dataframe(df)  #отобразить

st.metric(label='Win Speed',
		  value='70ms', delta='5.7')

st.markdown("Текст с эмодзи! :joy:")  #эмодзи
