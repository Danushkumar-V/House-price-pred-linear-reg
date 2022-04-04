import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import pickle
import requests

model = pickle.load(open('house-linear.pkl','rb'))

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def dataframe(head):
    b=pd.DataFrame(head, columns= ['bedrooms','bathrooms','sqft_living','sqft_lot'])
    return b



lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_fhg0ro2p.json")

st.title('House price prediction `Linear regression`')

st_lottie(
        lottie_hello,
        speed=1,
        reverse=True,
        loop=True,
        quality="low", # medium ; high# canvas
        height=400,
        width=400,
        key=None,
    )

st.write(
    """
    # Let's predict !
    """
)
#[['bedrooms','bathrooms','sqft_living','sqft_lot']]
bedrooms = st.text_input('Enter the number of bedrooms:',0.0)
bathrooms = st.text_input('Enter the number of bathrooms:',0.0)
sqft_living = st.text_input('Enter the sqft of living:',0)
sqft_lot = st.text_input('Enter the sqft_lot:',0)

data = [[bedrooms,bathrooms,sqft_living,sqft_lot]]
newdf = dataframe(data)

predict_value = model.predict(newdf)
result = st.button("Predict")

st.subheader(predict_value[0])