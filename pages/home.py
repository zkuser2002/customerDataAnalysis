import streamlit as st
import pandas as pd
df = pd.read_csv('data/Home/data.csv')
def write():
    st.markdown("""<style >
            .home {
                  font-size: 23px;
                  font-family:Microsoft JhengHei Light;
                  line-height: 1.6;
                  text-align: justify;
                  background:black;
                  -webkit-background-clip: text;}
            h1{
                  text-align: center;
                   font-family:Microsoft JhengHei Light;
            }
            </style>""",unsafe_allow_html=True)

    st.markdown("<h6 class='home'>Customer classification means that the product market can be divided into separate groups of customers. In this way, customer management will be easier and as a result, customer needs can be better met. In this data set, 2240 customers with 29 features are available. The first step is to examine the data and graphical graphs of the data are shown to achieve an acceptable understanding of the data. The required preprocessions are then performed on the data to select useful features for categorizing customers from a set of available features, and in this step, graphical diagrams are provided. In the next step, using the silhouette method, the number of clusters for the model is obtained and finally the model is created. According to the output of the model and the obtained diagrams, the desired results are presented for categorizing customers.</h6>",unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.dataframe(df)

