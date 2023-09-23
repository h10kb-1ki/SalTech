import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image

img = Image.open('logo.png')
st.image(img, use_column_width=True)

st.title('VRCZ解析')

dose1 = st.slider('１日投与量①', 0, 600, step=50)
conc1 = st.slider('血中濃度①', 0.0, 10.0, step=0.01)
dose2 = st.slider('１日投与量②', 0, 600, step=50)
conc2 = st.slider('血中濃度②', 0.0, 10.0, step=0.01)

def conc_calc(Km, Vmax, dose):
    return Km*dose/(Vmax-dose)

btn = st.button('解析')
if btn:
    # Lineweaver–Burk plot
    # 傾き：Km/Vmax　y切片：1/Vmax　x切片：-1/Km
    y = [1/dose1, 1/dose2]   # y軸：1/V 投与速度の逆数
    x = [1/conc1, 1/conc2]   # x軸：1/Cp 血中濃度の逆数
    slope, intercept = np.polyfit(x, y, 1)
    Vmax = 1/intercept
    Km = slope * Vmax
    
    if (Vmax<=0) or (Km<=0):
        st.write('解析不可')
    else:
        dose_list = np.arange(0, 600, 10)
        conc_list = []
        for i in dose_list:
            conc = conc_calc(Km, Vmax, i)
            conc_list.append(conc)
        #最大量を計算（conc=4）
        limit_dose = Vmax*4/(Km+4)
        
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
        rule = (alt.Chart().mark_rule(strokeDash=[5, 5], 
                                        size=1, color='red'
                                        ).encode(y=alt.datum(4)))
        rule2 = (alt.Chart().mark_rule(strokeDash=[5, 5], 
                                       size=1, color='red'
                                       ).encode(x=alt.datum(limit_dose)))
        st.altair_chart(scatter + rule + rule2, theme=None)
        st.write(f'Km = {Km:.2f}(μg/mL)  \n'
                    + f'Vmax = {Vmax:.2f}(mg/d)  \n'
                    + f'最大投与量 = {limit_dose:.1f}(mg/d)'
                    )
