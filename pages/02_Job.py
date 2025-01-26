import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup

img = Image.open('logo.png')
st.image(img)

def shift_data():
    url = 'https://drive.google.com/embeddedfolderview?id=12Zb899YTrxKT15XXixmuMUXe7s3xQi0x#list'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    titles =soup.find_all(class_='flip-entry-title')
    title_list = []
    for i in range(0, len(titles)):
        title = titles[i].get_text()
        title_list.append(title)
    refs =soup.find_all('a')
    ref_list =[]
    for i in range(0, len(refs)):
        ref = refs[i].get('href')
        ref_list.append(ref)    

    return title_list, ref_list

st.title('シフト・休暇')
weekly = st.checkbox('週間業務表')
if weekly:
    title_list, ref_list = shift_data()
    for i in range(0, len(title_list)):
        if '週間' in title_list[i]:
            st.write(f'■[{title_list[i]}]({ref_list[i]})')

monthly = st.checkbox('月間勤務表')
if monthly:
    title_list, ref_list = shift_data()
    for i in range(0, len(title_list)):
        if '勤務' in title_list[i]:
            if not '週間' in title_list[i]:
                st.write(f'■[{title_list[i]}]({ref_list[i]})')
    
yasumi = st.checkbox('休暇表')
if yasumi:
    title_list, ref_list = shift_data()
    for i in range(0, len(title_list)):
        if '休' in title_list[i]:
            st.write(f'■[{title_list[i]}]({ref_list[i]})')