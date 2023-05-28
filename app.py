import streamlit as st
import pickle
import sklearn
import xgboost
import numpy as np



# import the model
pipe=pickle.load(open('pipe.pkl','rb'))
car_data=pickle.load(open('car_data.pkl','rb'))

st.title('Used car price predictor')

# brand name
brand=st.selectbox(' Car Brand',car_data['car_name'].unique())
Model=st.selectbox('Model',car_data['model_name'].unique())
no_of_owner=st.selectbox('No of Owner',car_data['no_of_owner'].unique())
kms_driven=st.number_input('KMS driven')
mfg_year=st.number_input('Manufacturing Year')
colour=st.selectbox('Colour',['Beige', 'Black', 'Blue', 'Bronze', 'Brown', 'Gold', 'Green',
       'Grey', 'Maroon', 'Orange', 'Others', 'Purple', 'Red', 'Silver',
       'White'])
seating_capacity=st.selectbox('Seating Capacity',car_data['seating_capacity'].unique())
milage=st.number_input('Milage')
cng_car=st.selectbox('CNG car',[0,1])
Diesel_car=st.selectbox('Diesel car',[0,1])
Petrol_car=st.selectbox('Petrol car',[0,1])
Electric_car=st.selectbox('Electric car',[0,1])

if st.button('predict Price'):
    if colour =='Beige':
        colour=0
    elif colour=='Black':
        colour=1
    elif colour=='Blue':
        colour=2
    elif colour=='Bronze':
        colour=3
    elif colour=='Brown':
        colour=4
    elif colour=='Gold':
        colour=5
    elif colour=='Green':
        colour=6
    elif colour=='Grey':
        colour=7
    elif colour=='Maroon':
        colour=8
    elif colour=='Orange':
        colour=9
    elif colour=='Others':
        colour=10
    elif colour=='Purple':
        colour=11
    elif colour=='Red':
        colour==12
    elif colour=='Silver':
        colour=13
    elif colour=='White':
        colour=14
    else:
        colour=15
    query=np.array([brand,Model,no_of_owner,kms_driven,mfg_year,colour,seating_capacity,
                milage,cng_car,Diesel_car,Petrol_car,Electric_car],dtype=object)
    query=query.reshape(1,12)
    st.title(round(float(pipe.predict(query)),2))


