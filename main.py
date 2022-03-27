import streamlit as st
st.set_page_config( layout='wide')
from pages import home,Education,Marital_Status,Age



padding = 0
st.markdown(f""" <style>.reportview-container .main .block-container{{padding-top: {padding}rem;padding-bottom: {padding}rem;}}</style> """, unsafe_allow_html=True)
st.markdown(""" <style>#MainMenu {visibility: hidden;}</style>""", unsafe_allow_html=True)




Title_html = """
    <style>
        .title h1{
          font-size: 95px;
          font_family:'Britannic Bold';
          color: white;
          background-image: url("https://i.postimg.cc/J4y2tM2t/customer.jpg");
          height:280px;}        
    </style> 
    <div class="title">
        <h1 align='center'>Customer Analysis</h1>
    </div>
    """
st.markdown(Title_html, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',unsafe_allow_html=True,)
query_params = st.experimental_get_query_params()
tabs = ["Home"," "," ","Education"," "," ","Marital_Status"," "," "," ", "Age"]
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "Home"
if active_tab not in tabs:
    st.experimental_set_query_params(tab="Home")
    active_tab = "Home"
li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
    </li>
    """
    for t in tabs)
tabs_html = f"""
    <ul class="nav nav-tabs">
    {li_items}
    </ul>"""
st.markdown(tabs_html, unsafe_allow_html=True)


#Menu
"""if active#_tab == "Home":
    home.write()
elif active_tab == "Education":
    Education.write()
elif active_tab == "Marital_Status":
    Marital_Status.write()
elif active_tab == "Age":
    Age.write()

else:
    st.error("Something has gone terribly wrong.")"""
