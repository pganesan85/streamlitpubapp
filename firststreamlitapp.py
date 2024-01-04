import pandas as pd 
import streamlit as st 
#import matplotlib.pyplot as plt
#import seaborn as sns


st.title ('welcome to streamlit')

if st.button('click me'):
  st.write('Button was clicked')

st.write('success')

uploaded_file = st.file_uploader("Truck.csv", type = ["CSV"])

if uploaded_file is not None :
  data = pd.read_csv(uploaded_file)
  st.write(data)
  st.write("statistics")
  st.write(data.describe())
  #st.subheader("histogram visualization")
  selected_columns = st.selectbox("select a colum for histogram",data.columns)
  #plt.figure(figsize = (8,6))
  #st.set_option('deprecation.showPyplotGlobalUse', False)
  #sns.histplot(data[selected_columns], kde=bool(123))
  #fig, ax = plt.subplots()
  #ax.scatter(data["name"], data[selected_columns])
  #st.pyplot(fig)

