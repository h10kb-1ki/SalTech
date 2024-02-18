import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image

img = Image.open('logo.png')
st.image(img, use_column_width=True)

st.title('Memo App')
st.write('※※Web App更新時は必ずDBをバックアップする※※')
mikan = st.checkbox('未完メモ')
if mikan:
    col1, col2 = st.columns([1,  30])
    with col2:
        cat = st.radio('〔分類を選択〕', ['private', 'work'], index=1, horizontal=True)
        db = sqlite3.connect('memo.db')
        cur = db.cursor()
        cur.execute("""
                    SELECT rowid, * 
                    FROM memo
                    WHERE status='未'
                    ORDER BY deadline ASC
                    """)
        mikan_list = cur.fetchall()
        cur.close()
        db.close()
        df = pd.DataFrame(mikan_list)
        df.rename(columns={0: 'id', 1: '分類', 2: 'タイトル', 3: '詳細', 4: '期限', 5: '状態'}, inplace=True)
        df.set_index('id', inplace=True)
        df = df.query(f'分類 == "{cat}"')
        df = df[['分類', 'タイトル', '詳細', '期限']]
        st.table(df)
            
update = st.checkbox('更新')
if update:
    col1, col2 = st.columns([1,  30])
    with col2:
        menu = st.radio('〔処理内容〕', ['新規登録', '終了処理'], index=0, horizontal=True)
        if menu == '新規登録':
            with st.form('input_form', clear_on_submit=True):
                category = st.selectbox('分類', 
                                        ['private', 'work'], 
                                        index=1)
                title = st.text_input('タイトル')
                detail = st.text_input('詳細')
                deadline = st.date_input('期限')
                
                db = sqlite3.connect('memo.db')
                cur = db.cursor()        
                btn1 = st.form_submit_button('作成')
                if btn1:
                    cur.execute('INSERT INTO memo values(?, ?, ?, ?, "未");', 
                                (category, title, detail, deadline))
                    db.commit()
                    cur.close()
                    db.close()
        elif menu == '終了処理':
            with st.form('input_form', clear_on_submit=True):
                num = st.number_input('RowIDを入力', min_value=1, step=1)          
                btn2 = st.form_submit_button('終了')
                if btn2:
                    db = sqlite3.connect('memo.db')
                    cur = db.cursor() 
                    cur.execute(f"""
                                UPDATE memo
                                SET status='終了'
                                WHERE rowid={num}
                                """)
                    db.commit()
                    cur.close()
                    db.close()
                    st.write(f'RowID:{num}のstatusを「終了」に変更しました。')
complete = st.checkbox('終了メモ')
if complete:
    col1, col2 = st.columns([1,  30])
    with col2:
        cat = st.radio('〔分類を選択〕', ['private', 'work'], index=1, horizontal=True)
        db = sqlite3.connect('memo.db')
        cur = db.cursor()
        cur.execute("""
                    SELECT rowid, * 
                    FROM memo
                    WHERE status='終了'
                    ORDER BY deadline DESC
                    """)
        mikan_list = cur.fetchall()
        cur.close()
        db.close()
        df = pd.DataFrame(mikan_list)
        df.rename(columns={0: 'id', 1: '分類', 2: 'タイトル', 3: '詳細', 4: '期限', 5: '状態'}, inplace=True)
        df.set_index('id', inplace=True)
        df = df.query(f'分類 == "{cat}"')
        df = df[['分類', 'タイトル', '詳細', '期限']]
        st.table(df)
backup = st.checkbox('バックアップ')
if backup:
    db = sqlite3.connect('memo.db')
    cur = db.cursor()
    cur.execute("""
                SELECT * 
                FROM memo
                """)
    data = cur.fetchall()
    cur.close()
    db.close()
    df = pd.DataFrame(data)
    df.rename(columns={0: '分類', 1: 'タイトル', 2: '詳細', 3: '期限', 4: '状態'}, inplace=True)
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv',
        )