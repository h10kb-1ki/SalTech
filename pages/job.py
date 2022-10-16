import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup

img = Image.open('logo.png')
st.image(img, use_column_width=True)

def yasumi_data():
    url = 'https://drive.google.com/embeddedfolderview?id=1e-VJXFiRLtIqlTr15VvifmyjJFFbjwp0#list'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    refs =soup.find_all('a')
    ref_list =[]
    for i in range(0, len(refs)):
        ref = refs[i].get('href')
        ref_list.append(ref)    
    titles =soup.find_all(class_='flip-entry-title')
    title_list = []
    for i in range(0, len(titles)):
        title = titles[i].get_text()
        title_list.append(title)
    yasumi = ''
    for i in range(0, len(title_list)):
        if '休暇' in title_list[i]:
            yasumi_ref = '■'+title_list[i]+'\n '+ref_list[i] + ' \n'
            yasumi = yasumi + yasumi_ref
    return yasumi
            
def monthly_data():
    url = 'https://drive.google.com/embeddedfolderview?id=1e-VJXFiRLtIqlTr15VvifmyjJFFbjwp0#list'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    refs =soup.find_all('a')
    ref_list =[]
    for i in range(0, len(refs)):
        ref = refs[i].get('href')
        ref_list.append(ref)    
    titles =soup.find_all(class_='flip-entry-title')
    title_list = []
    for i in range(0, len(titles)):
        title = titles[i].get_text()
        title_list.append(title)            
    monthly = ''
    for i in range(0, len(title_list)):
        if '勤務' in title_list[i]:
            if '週間' not in title_list[i]:
                kinmu = '■'+title_list[i]+'\n '+ref_list[i] + ' \n'
                monthly = monthly + kinmu
    return monthly
    
def weekly_data():
    url = 'https://drive.google.com/embeddedfolderview?id=1e-VJXFiRLtIqlTr15VvifmyjJFFbjwp0#list'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    refs =soup.find_all('a')
    ref_list =[]
    for i in range(0, len(refs)):
        ref = refs[i].get('href')
        ref_list.append(ref)    
    titles =soup.find_all(class_='flip-entry-title')
    title_list = []
    for i in range(0, len(titles)):
        title = titles[i].get_text()
        title_list.append(title)
    weekly = ''
    for i in range(0, len(title_list)):
        if '週間' in title_list[i]:
            kinmu = '■'+title_list[i]+'\n '+ref_list[i] + ' \n'
            weekly = weekly + kinmu
    return weekly

st.title('業務')
weekly = st.checkbox('週間業務')
if weekly:
    weekly = weekly_data()
    st.write(weekly)

monthly = st.checkbox('月間業務')
if monthly:
    monthly = monthly_data()
    st.write(monthly)
    
yasumi = st.checkbox('休暇表')
if yasumi:
    yasumi = yasumi_data()
    st.write(yasumi)