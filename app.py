import streamlit as st
import pickle
import numpy as np

pipe=pickle.load(open('pipe.pkl','rb'))
data=pickle.load(open('data.pkl','rb'))


st.title("Laptop Predictor")

company=st.selectbox('Brand',data['Company'].unique())

type=st.selectbox('Type',data['TypeName'].unique())

ram=st.selectbox('Ram',[2,4,6,8,12,16,24,32,64])

weight=st.number_input('Weight')

touchscreen=st.selectbox('Touch screen',['No','Yes'])

ips=st.selectbox('IPS',['No','Yes'])

screen_size=st.number_input('Screen size')

resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x1800','2560x1600','2560x1440','2304x1440'])

cpu=st.selectbox('CPU',data['Cpu Brand'].unique())

hdd=st.selectbox('HDD',[128,256,512,1024,2048])

ssd=st.selectbox('SSD',[0,8,128,256,512,1024])

gpu=st.selectbox('GPU',data['Gpu Brand'].unique())

os=st.selectbox('OS',data['os'].unique())

if st.button('Predict Price'):
    
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
    X_Res=int(resolution.split('x')[0])
    Y_Res=int(resolution.split('x')[1])
    ppi=(((X_Res**2)+(Y_Res**2))**0.5)/screen_size
    query=np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query=query.reshape(1,12)
    st.title("The predicted price is :")
    st.title(int(np.exp(pipe.predict(query)[0])))