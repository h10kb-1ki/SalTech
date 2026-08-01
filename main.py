import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime
from PIL import Image
import io
import re
#from pandas_datareader import data  #requirements.txtからも削除
import pandas as pd
#from dateutil.relativedelta import relativedelta  #Python 3.12以降では distutils が削除された
import mplfinance as mpf
import altair as alt
import openpyxl as xl
import seaborn as sns
import matplotlib.pyplot as plt
#import japanize_matplotlib

st.set_page_config(layout="wide")

img = Image.open('logo.png')
st.image(img)

st.write('-----------------------------------------------------')
traffic = st.checkbox('交通情報')
if traffic:
    st.write('■東海道本線[豊橋～米原]')
    url = 'https://transit.yahoo.co.jp/traininfo/detail/192/193/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    statusJ = soup.find('dd', class_='normal')
    if statusJ:
        st.write(statusJ.text)
    else:
        st.write('***遅延あり***')
    st.write('▶[JR運行情報](https://traininfo.jr-central.co.jp/zairaisen/status_detail.html?line=10001&lang=ja)')
    st.write('')

    st.write('■名鉄名古屋本線')
    url = 'https://transit.yahoo.co.jp/traininfo/detail/208/0/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    statusM = soup.find('dd', class_='normal')
    if statusM:
        st.write(statusM.text)
    else:
        st.write('***遅延あり***')

    st.write('▶[名鉄（本線）運行情報](https://top.meitetsu.co.jp/em/)')
    st.write('')
    st.write('')

    st.write('▶[名鉄バス（安城駅発 更生病院行）](https://navi.meitetsu-bus.co.jp/mb/DepQR.aspx?p=320103000)')
    st.write('▶[乗り換え案内](https://www.jorudan.co.jp/norikae/)')


st.write('-----------------------------------------------------')
weather = st.checkbox('天気')
if weather:
    st.write('▶[雨雲レーダー](https://tenki.jp/radar/map/)')

st.write('-----------------------------------------------------')
news = st.checkbox('ニュース')
if news:
    yahoo = st.checkbox('Yahoo! ニュース トピックス')
    if yahoo == True:
        url = 'https://www.yahoo.co.jp/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        elems = soup.find_all(href = re.compile('news.yahoo.co.jp/pickup'))
        for i in range(0, len(elems)):
            # titleを取得
            title = elems[i].text
            # linkを取得
            link = elems[i].attrs['href']
            st.write(f'・[{title}]({link})')

    seiyaku = st.checkbox('製薬業界ニュース')
    if seiyaku ==True:
        url = 'https://answers.ten-navi.com/pharmanews/pharma_category/1/'
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        titles = soup.find_all('h2')
        tag = soup.find_all(class_='tag')
        ref = soup.find_all('a', class_='clearfix')

        for i in range(0, len(titles)):
            if tag[i].text == 'ニュース解説':
                title = titles[i].text
                link = ref[i].attrs['href']
                st.write(f'・[{title}]({link})')
