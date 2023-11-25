import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image

img = Image.open('logo.png')
st.image(img, use_column_width=True)

st.title('VRCZ解析')

def non_linear(doseList, concList):
    # Lineweaver–Burk plot
    # 傾き：Km/Vmax　y切片：1/Vmax　x切片：-1/Km
    y = []
    for i in doseList:
        y.append(1/i)  # y軸：1/V 投与速度の逆数
    x = []
    for i in concList:
        x.append(1/i)  # x軸：1/Cp 血中濃度の逆数
    slope, intercept = np.polyfit(x, y, 1)
    Vmax = 1/intercept
    Km = slope * Vmax
    
    # Michaelis-Menten
    dose_list = np.arange(0, 600, 1)
    conc_list = []
    for i in dose_list:
        conc = Km*i/(Vmax-i)
        conc_list.append(conc)
    
    source = pd.DataFrame({
        'dose (mg/d)': dose_list, 
        'VRCZ conc': conc_list
        })
    #queryで 0<VRCZ conc<10 の範囲のみへ
    source = source.query("`VRCZ conc` <= 10 and `VRCZ conc` >= 0")  #列名にスペースを含む場合はバッククオートで囲む
    scatter = alt.Chart(source).mark_line().encode(
                x='dose (mg/d)', 
                y='VRCZ conc', 
                )
    #実測ポイントをプロット
    laboData = pd.DataFrame({
                            'dose (mg/d)': doseList,
                            'VRCZ conc': concList
                            })
    points = alt.Chart(laboData).mark_point(filled=True, size=50).encode(
                x=alt.X('dose (mg/d):Q',
                        scale=alt.Scale(domain=[0,600])),
                y=alt.Y('VRCZ conc:Q',
                        scale=alt.Scale(domain=[0,10])),
                )
    return Vmax, Km, scatter, points

radio = st.sidebar.radio('データ入力', ['スライダー（2ポイント）', '直接入力', 'データ upload'], 
                        #horizontal=True
                        )

if radio == 'スライダー（2ポイント）':
    st.write('-----------------')
    dose1 = st.slider('１日投与量①', 0, 600, step=50)
    conc1 = st.slider('血中濃度①', 0.0, 10.0, step=0.01)
    st.write('-----------------')
    dose2 = st.slider('１日投与量②', 0, 600, step=50)
    conc2 = st.slider('血中濃度②', 0.0, 10.0, step=0.01)
    doseList = [dose1, dose2]
    concList = [conc1, conc2]
    st.write('-----------------')
    
    btn = st.button('解析')
    if btn:
        Vmax, Km, scatter, points = non_linear(doseList, concList)
        st.altair_chart(scatter + points, theme=None)
        st.write(f'Km = {Km:.2f}(μg/mL)  \n'
                + f'Vmax = {Vmax:.2f}(mg/d)  \n'
                )

elif radio == '直接入力':
    if 'num' not in st.session_state:
        st.session_state.num = ''
    num = int(st.number_input('採血ポイント数', min_value=2, step=1))
    st.write('-----------------')
    doseList = []
    concList = []
    col1, col2 = st.columns(2)
    for i in range(num):
        with col1:
            d = st.number_input(f'投与量{i+1}(mg/d)')
            doseList.append(d)
        with col2:
            c = st.number_input(f'血中濃度{i+1}(μg/mL)')
            concList.append(c)
    st.write('-----------------')
    btn = st.button('解析')
    if btn:
        Vmax, Km, scatter, points = non_linear(doseList, concList)
        col3, col4 = st.columns([3, 2])
        with col3:
            st.altair_chart(scatter + points, theme=None)
        with col4:
            st.write(f'Km = {Km:.2f}(μg/mL)  \n'
                    + f'Vmax = {Vmax:.2f}(mg/d)  \n'
                    + '  \n')
        for i in range(num):
            st.write(f'データ{i+1}：{doseList[i]}(mg/d)、{concList[i]}(μg/mL)')
        
elif radio == 'データ upload':
    st.write('＝＝＝＝＝＝＝＝')
    st.write('作成中。。。')
    st.write('＝＝＝＝＝＝＝＝')
