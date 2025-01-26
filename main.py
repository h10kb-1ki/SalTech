import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime
from PIL import Image
import io
import re
from pandas_datareader import data
import pandas as pd
from dateutil.relativedelta import relativedelta
import mplfinance as mpf
import altair as alt
import openpyxl as xl
import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib

st.set_page_config(layout="wide")

img = Image.open('logo.png')
st.image(img)

st.write('-----------------------------------------------------')
traffic = st.checkbox('Traffic')
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
weather = st.checkbox('Weather')
if weather:
    st.write('▶[雨雲レーダー](https://tenki.jp/radar/map/)')

st.write('-----------------------------------------------------')
news = st.checkbox('NEWS')
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

st.write('-----------------------------------------------------')
LINE = st.checkbox('LINE')
if LINE:
    msg = st.text_input('メッセージを入力')
    pwd = st.text_input('パスワードを入力')
    btn = st.button('送信')
    if btn:
        TOKEN = 'z3URXwam5ZTJGzT40xNF64f6gFwDkjd5GJlH4h9D79'
        api_url = 'https://notify-api.line.me/api/notify'

        TOKEN_dic = {'Authorization': 'Bearer'+' '+TOKEN + pwd}
        send_dic = {'message': msg}
        res = requests.post(api_url, headers=TOKEN_dic, data=send_dic)

        if res.status_code == 200:
            st.write('送信完了')
            st.balloons()
        else:
            st.write('送信に失敗しました')

st.write('-----------------------------------------------------')                
Finance = st.checkbox('Finance')
if Finance:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    dic = {'サントリー': '2587.JP',
      'アサヒ': '2502.JP',
      'キリン': '2503.JP',
      'サッポロ': '2501.JP',
      'タケダ': '4502.JP',
      'アステラス': '4503.JP',
      '大塚': '4578.JP',
      '第一三共': '4568.JP',
      'エーザイ': '4523.JP',
      '中外': '4519.JP',
      '大日本住友': '4506.JP',
      '塩野義': '4507.JP',
      '協和キリン': '4151.JP',
      '小野薬品': '4528.JP'}
    name = list(dic.keys())
    today = datetime.datetime.now()
    start_point = st.selectbox('開始', ('1ヶ月前', '3ヶ月前', '半年前', '1年前', '任意'), index=2)
    if start_point == '1ヶ月前':
        start = today - relativedelta(months=1)
    elif start_point == '3ヶ月前':
        start = today - relativedelta(months=3)
    elif start_point == '半年前':
        start = today - relativedelta(months=6)
    elif start_point == '1年前':
        start = today - relativedelta(months=12) 
    else:
        start = st.date_input('開始')

    end = st.date_input('終了')
    company_name = st.selectbox('銘柄', name, index=11)
    company_code = dic[company_name]

    df = data.DataReader(company_code, 'stooq', start, end)
    df = df.sort_values('Date', ascending=True)

    cs  = mpf.make_mpf_style(gridcolor="lightgray", facecolor="white", edgecolor="#202426", figcolor="white", 
            rc={"xtick.color":"black", "xtick.labelsize":12, 
                "ytick.color":"black", "ytick.labelsize":12, 
                "axes.labelsize":15, "axes.labelcolor":"black"})
    fig = mpf.plot(df, type='candle', volume=True, mav=(5, 25, 50), figratio=(12,4), style=cs)
    st.pyplot(fig)


st.write('-----------------------------------------------------')  
hobby = st.checkbox('Hobby & Health')
if hobby:
    st.write('▶[Pep Up](https://pepup.life/home)')

st.write('-----------------------------------------------------')                
MyLib = st.checkbox('Library')
if MyLib:
    st.write('▶[一郎の部屋](https://sites.google.com/view/tdmichiro/%E3%83%9B%E3%83%BC%E3%83%A0)')
    st.write('▶[DIサイト](https://ajdididi-di-search-aydtef.streamlit.app/)')