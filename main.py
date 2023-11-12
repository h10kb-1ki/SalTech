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
st.image(img, use_column_width=True)

st.write('-----------------------------------------------------')
traffic = st.checkbox('Traffic')
if traffic:
    '''
    #### 東海道本線[豊橋～米原]
    '''
    url = 'https://transit.yahoo.co.jp/traininfo/detail/192/193/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    statusJ = soup.find('dd', class_='normal')
    if statusJ:
        st.write(statusJ.text)
        st.write('▶[JR運行情報](https://traininfo.jr-central.co.jp/zairaisen/status_detail.html?line=10001&lang=ja)')
    else:
        st.write('***遅延あり***  \n▶[JR運行情報](https://traininfo.jr-central.co.jp/zairaisen/status_detail.html?line=10001&lang=ja)')
    
    #st.write('▶[JR運行情報](https://traininfo.jr-central.co.jp/zairaisen/status_detail.html?line=10001&lang=ja)')
    
    #st.markdown('https://traininfo.jr-central.co.jp/zairaisen/status_detail.html?line=10001&lang=ja', unsafe_allow_html=True)
    st.write('')
    '''
    #### 名鉄名古屋本線
    '''
    url = 'https://transit.yahoo.co.jp/traininfo/detail/208/0/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    statusM = soup.find('dd', class_='normal')
    if statusM:
        st.write(statusM.text)
    else:
        st.write('***遅延あり***')
    '''
    ###### ▶名鉄（本線）運行情報
    '''
    st.markdown('https://top.meitetsu.co.jp/em/', unsafe_allow_html=True)
    st.write('')
    st.write('')
    
    '''
    ###### ▶名鉄バス（安城駅発 更生病院行）
    '''
    st.markdown('https://navi.meitetsu-bus.co.jp/mb/DepQR.aspx?p=320103000', unsafe_allow_html=True)

    '''
    ###### ▶乗り換え案内
    '''
    st.markdown('https://www.jorudan.co.jp/norikae/', unsafe_allow_html=True)

st.write('-----------------------------------------------------')
weather = st.checkbox('Weather')
if weather:
    nagoya = st.checkbox('名古屋市の天気')
    if nagoya == True:
        url = 'https://weathernews.jp/onebox/35.152529/136.914405/q=%E6%84%9B%E7%9F%A5%E7%9C%8C%E5%90%8D%E5%8F%A4%E5%B1%8B%E5%B8%82&v=ba36a0768da9ec39827acda9415897ef0bccf54cffef6b80c06e56abca48ad88&temp=c&lang=ja'
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        day_ = soup.find_all(class_='wTable__item')
        today = day_[5].text
        tomorrow = day_[10].text
        data = soup.find_all(class_='text wTable__item')
        data_list = []
        for i in range(0, 8):
            kakuritu_kion = data[i].text
            data_list.append(kakuritu_kion)
        icon = soup.find_all(class_='day2Table__item weather')
        icon_today = 'https:' + icon[0].find('img').get('src')
        icon_tomorrow = 'https:' + icon[1].find('img').get('src')
        title = soup.find(class_='tit-02').text
        info = soup.find(class_='comment no-ja')
        comment = info.text
        comment = comment.split('\n')[2]

        st.write(title)
        st.write(comment)
        st.write('■ '+ today)
        st.image(icon_today)
        st.write('最高気温:'+ data_list[0] +'　最低気温:'+ data_list[1])
        st.write('午前：'+ data_list[2] +'　午後：'+ data_list[3])

        st.write('■'+ tomorrow)
        st.image(icon_tomorrow)
        st.write('最高気温:'+ data_list[4] +'　最低気温:'+ data_list[5])
        st.write('午前：'+ data_list[6] +'　午後：'+ data_list[7])

    anjo = st.checkbox('安城市の天気')
    if anjo == True:
        url = 'https://weathernews.jp/onebox/34.941939/137.086575/q=%E6%84%9B%E7%9F%A5%E7%9C%8C%E5%AE%89%E5%9F%8E%E5%B8%82%E5%AE%89%E5%9F%8E%E7%94%BA&v=f76c962ed76dfb70c19ac3765fa855ccf555678b4df6046c50cd0ddda9c76c6b&temp=c&lang=ja'
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        day_ = soup.find_all(class_='wTable__item')
        today = day_[5].text
        tomorrow = day_[10].text
        data = soup.find_all(class_='text wTable__item')
        data_list = []
        for i in range(0, 8):
            kakuritu_kion = data[i].text
            data_list.append(kakuritu_kion)
        icon = soup.find_all(class_='day2Table__item weather')
        icon_today = 'https:' + icon[0].find('img').get('src')
        icon_tomorrow = 'https:' + icon[1].find('img').get('src')
        title = soup.find(class_='tit-02').text
        info = soup.find(class_='comment no-ja')
        comment = info.text
        comment = comment.split('\n')[2]

        st.write(title)
        st.write(comment)
        st.write('■ '+ today)
        st.image(icon_today)
        st.write('最高気温:'+ data_list[0] +'　最低気温:'+ data_list[1])
        st.write('午前：'+ data_list[2] +'　午後：'+ data_list[3])

        st.write('■'+ tomorrow)
        st.image(icon_tomorrow)
        st.write('最高気温:'+ data_list[4] +'　最低気温:'+ data_list[5])
        st.write('午前：'+ data_list[6] +'　午後：'+ data_list[7])
    '''
    ###### ▶雨雲レーダー
    '''
    st.markdown('https://tenki.jp/radar/map/', unsafe_allow_html=True)

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
            st.write(f'{title}  \n'
                    + f'{link}'
                    )
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
                st.write(f'{title}  \n'
                        + f'{link}'
                        )
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
    '''
    ###### ▶Pep Up
    '''
    st.markdown('https://pepup.life/home', unsafe_allow_html=True)

st.write('-----------------------------------------------------')                
MyLib = st.checkbox('Library')
if MyLib:
    '''
    ###### ▶一郎の部屋
    '''
    st.markdown('https://sites.google.com/view/tdmichiro/%E3%83%9B%E3%83%BC%E3%83%A0', unsafe_allow_html=True)
    
    kampo = st.checkbox('漢方比較')
    if kampo == True:
        wb = xl.load_workbook('kampo.xlsx')
        ws = []
        for i in wb.worksheets:
            ws.append(i.title)

        df = pd.read_excel('kampo.xlsx', sheet_name=ws[0], header=0, index_col=0)
        for j in range(1, len(ws)):
            df_sheet = pd.read_excel('kampo.xlsx', sheet_name=ws[j], header=0, index_col=0)
            df = df.merge(df_sheet, how='outer', left_index=True, right_index=True)

        st.title('漢方：含有生薬の比較')
        st.write('1日量（ツムラ製品、通常量）中の生薬含有量を表示')
        kampo_list = sorted(df.columns)
        selection = st.multiselect('漢方を選択', kampo_list)

        df = df[selection]
        df.dropna(subset=selection, how='all', inplace=True)
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        ax = sns.heatmap(df, annot=True, fmt='.1f', cmap='Blues', vmax=10, vmin=0, ax=ax)

        btn = st.button('表示')

        if btn == True:
            st.pyplot(fig)
