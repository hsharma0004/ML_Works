import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('D:\\VS STUDIO\\GUI\\Streamlit\\House_Price_Prediction_Model.pkl','rb'))

st.header('Banglore House price Predictor')
data = pd.read_csv('D:\\VS STUDIO\\GUI\\Streamlit\\Cleaned_data.csv')
loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter total Square feet')
beds = st.number_input('Enter the No bedrooms')
bal = st.number_input('Enter the No number balconies')
bath = st.number_input('Enter the No number bathrooms')

input = pd.DataFrame([[loc,sqft,bath,bal,beds]],columns=['location','total_sqft','bath','balcony','bedrooms'])

if st.button("Predict Price"):
    output = model.predict(input)
    out_str = 'Price of the house is: ₹' + str(round(output[0]*100000, 2))
    st.success(out_str)  # ✅ Displaying the result
