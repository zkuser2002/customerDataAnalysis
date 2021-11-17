import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go


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
            </style>""",unsafe_allow_html=True)


    options = st.multiselect('What Features you want to compare?',['Purchase','Education','Costs', 'Income', 'users_day'])




    if  'Income' in options:
        fig = px.bar(data, x='Marital_Status', y='Income', color='Education')
        fig.update_layout(title_text='Realation between Marital_Status and Education with Income', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if  'Costs' in options:
        fig=px.bar(data,x='Marital_Status',y='Costs',color='Education')
        fig.update_layout(title_text='Realation between Marital_Status and Education with Costs', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if  'Purchase' in options:
        fig=px.bar(data,x='Marital_Status',y='Purchase',color='Education')
        fig.update_layout(title_text='Realation between Marital_Status and Education with Purchase', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if  'users_day' in options:
        fig = px.bar(data, x='Marital_Status', y='users_day', color='Education')
        fig.update_layout(title_text='Realation between Marital_Status and Education with Users Day', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if  'Education' in options:
            chart2 = alt.Chart(data).mark_bar().encode(alt.X("Marital_Status"),y="count()",color='Education', tooltip='count()'
            ).properties(title='Realation between Marital Status and Education')
            st.altair_chart(chart2, use_container_width=True)
    labels = ['Single', 'Relationship']
    values = [796, 1444]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.write(fig)


