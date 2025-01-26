import sqlite3
import streamlit as st
from PIL import Image

img = Image.open('logo.png')
st.image(img)

st.title('抗菌薬データ検索')
radio = st.radio('検索対象', ['抗菌薬', '細菌'])

def antibiotics(key):
    db = sqlite3.connect('antibiotics.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM T_drug WHERE category LIKE ? OR drug LIKE ? OR abbreviation LIKE ? OR product LIKE ?", 
                [key, key, key, key])
    data = cur.fetchall()
    cur.close()
    db.close()

    if len(data) == 0:
        output = ['該当データなし']
    else:
        # db内のtableから列名を取得しリストへ
        descr = cur.description
        col_list = []
        for desc in descr:
            col_list.append(desc[0])
        # 抽出データをtextに整形
        output = []
        for i in range(0, len(data)):
            elem = '-----------------------------  \n'
            elem += f'[{data[i][1]}]  \n{data[i][2]}  {data[i][3]} ({data[i][4]})   \n'
            if not data[i][5] is None:
                elem += f'{data[i][5]}  \n'
            if not data[i][6] is None:
                elem += f'{data[i][6]}  \n'
            for j in range(7, len(col_list)):  # 7～24がスペクトラムの詳細データ
                if not data[i][j] is None:
                    elem += f'-{col_list[j]}: {data[i][j]}  \n'
            output.append(elem)
    return output

def bacteria(bac):
    db = sqlite3.connect('antibiotics.db')
    cur = db.cursor()
    cur.execute(f"SELECT * FROM T_bacteria WHERE name1 = '{bac}'")
    data2 = cur.fetchone()
    cur.close()
    db.close()
    if not data2[4] is None:
        if not data2[5] is None:
            area = f'＜一般＞{data2[4]}  \n＜重症・特殊病態＞{data2[5]}'
        else:
            area = f'＜一般＞{data2[4]}'
    else:
        if not data2[5] is None:
            area = f'＜重症・特殊病態＞{data2[5]}'
        else:
            area = ''
    note = f'{data2[2]} [{data2[3]}]  \n{area}'
    return note

if radio == '抗菌薬':
    key = st.text_input('検索キーワード')
    key = f'%{key}%'
    btn = st.button('検索')
    if btn:
        output = antibiotics(key)
        for i in output:
            st.write(i)
elif radio == '細菌':
    db = sqlite3.connect('antibiotics.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM T_drug") 
    descr = cur.description
    col_list = []
    for desc in descr:
        col_list.append(desc[0])
    del col_list[0:7]
    bac = st.selectbox('細菌を選択', col_list)
    
    cur.execute(f"SELECT * FROM T_drug WHERE `{bac}` = '**' or `{bac}` = '*' or `{bac}` = '++' or `{bac}` = '+'") 
    data = cur.fetchall()
    cur.close()
    db.close()
    
    note = bacteria(bac)
    st.write(note)
    st.write('---治療薬候補---')
    if len(data) == 0:
        st.write('該当データなし')
    else:
        for i in range(len(data)):
            st.write(f'[{data[i][1]}]  {data[i][2]}  {data[i][3]} ')