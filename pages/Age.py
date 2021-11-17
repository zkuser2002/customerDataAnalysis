import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
data = pd.read_csv('data/Education/data.csv')
data=pd.DataFrame(data)
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
                    </style>""", unsafe_allow_html=True)
    chart1 = alt.Chart(data).mark_bar().encode(alt.X("Age"), y="count()", color='Education',tooltip='count()'
                                               ).properties(title='Realation between Age and Education')
    st.altair_chart(chart1, use_container_width=True)

    chart2 = alt.Chart(data).mark_bar().encode(alt.X("Age"), y="count()", color='Marital_Status', tooltip='count()'
                                               ).properties(title='Realation between Age and Marital_Status')
    st.altair_chart(chart2, use_container_width=True)

    fig = px.bar(data, x='Age', y='Income', color='Education')
    fig.update_layout(title_text='Realation between Age and Education with Income', title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(data, x='Age', y='Costs', color='Education')
    fig.update_layout(title_text='Realation between Age and Education with Costs', title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)



