import streamlit as st
import pandas as pd
import time

#localhost and 127.0.0.1 are the same thing
#streamlit ka ye advantage hai ki code mai koi changes karte ho toh automatic reflect ho jata hai
#ye react ka feature hai

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('And I am loving it')
st.text("This is a normal text")
st.markdown("""
- Race 3
- Humshakals
- Housefull
""")
st.code("""
def foo(input):
    return foo**2

x= foo(2)        
        """)
st.latex('x^2 + y^2 +2 =0')

df=pd.DataFrame({
    'name': ["Shraddha","Bhakti","Unkown"],
    'marks': [60,70,80],
    'package': [10,12,14]
})

st.dataframe(df)
st.metric('Revenue','Rs 3L','3%')
st.json({
    'name': ["Shraddha","Bhakti","Unkown"],
    'marks': [60,70,80],
    'package': [10,12,14]
})
#st.image('IMG_6353.JPG')
st.sidebar.title("Love you")

#col1, col2 = st.columns(3)

#with col1:
    #st.image("IMG_6353.JPG")

#with col2:
    #st.image("IMG_6353.JPG")

st.error("Login Failed")
st.success("Login Successfully")
st.info("This is streamlit, use wisely")
st.warning("God helps those who helps themselves")
bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter Email')
number = st.number_input('Enter Age')
st.date_input('Enter registration date')
