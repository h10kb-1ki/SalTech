import streamlit as st
import pandas as pd
from PIL import Image

img = Image.open('logo.png')
st.image(img, use_column_width=True)

st.title('TPN組成計算')

df = pd.read_excel('Nutrition.xlsx', sheet_name='Sheet2')
df.set_index('products', inplace=True)

products = st.multiselect('薬剤選択', df.index)
df_q = df.query(f'products in {products}')
    
vol_list = []
for i in range(len(products)):
    vol = st.number_input(f'{products[i]}(mL)')
    vol_list.append(vol)

btn_cal = st.button('計算')
if btn_cal:
    if len(products) == 0:
        st.write('薬剤を選択してください')
    else:
        res = df_q.iloc[0, :] * vol_list[0]
        df_res = pd.DataFrame(res).T
        for i in range(1, len(df_q)):
            cal = df_q.iloc[i, :] * vol_list[i]
            df_cal = pd.DataFrame(cal).T
            df_res = pd.concat([df_res, df_cal])
        df_res.loc['Total'] = df_res.sum()
        st.dataframe(df_res)