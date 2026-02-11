import streamlit as st
import sqlite3

st.title('医薬品DB横断検索')
st.write('')

kensaku = st.text_input('キーワード')
btn1 = st.button('検索')

if btn1:
    if kensaku == '':
            st.write('何か入力してください！')
    else:
        kensaku = '%' + kensaku + '%'
        # 医薬品メモDB
        db1 = sqlite3.connect('drug_memo.db')
        cur = db1.cursor()
        cur.execute(f"SELECT * FROM memo WHERE (drug LIKE ? OR tag LIKE ? OR memo LIKE ?)", [kensaku, kensaku, kensaku])
        data = cur.fetchall()
        cur.close()
        db1.close()

        st.subheader('医薬品メモDB')
        if len(data) == 0:
             st.write('該当データなし')
        else:
             st.write(f'該当データ: {len(data)}件')
             for i in range(len(data)):
                  st.markdown("""
                              <style>
                              .custom-text {
                                   font-size: 16px;
                              }
                              </style>
                              """, unsafe_allow_html=True)
                  st.markdown(f'<p class="custom-text">◼︎{data[i][1]}&nbsp;&nbsp; <<{data[i][2]}>> &nbsp;&nbsp; id：{data[i][0]}  \n</p>'
                              + f'<p class="custom-text">{data[i][3]}  \n</p>', 
                              unsafe_allow_html=True)
                  st.markdown('---')
        st.write('')
        #医薬品供給DB
        st.subheader('医薬品供給DB')
        db2 = sqlite3.connect('drug_supply.db')
        cur = db2.cursor()    
        #解消していない案件
        cur.execute(f"SELECT * FROM unstable WHERE (drug LIKE ? OR maker LIKE ?) AND status = 0", [kensaku, kensaku])
        data0 = cur.fetchall()
        #解決済
        cur.execute(f"SELECT * FROM unstable WHERE (drug LIKE ? OR maker LIKE ?) AND status = 1", [kensaku, kensaku])
        data1 = cur.fetchall()
        cur.close()
        db2.close()

        st.write('#### ---未解決案件---')
        if len(data0) == 0:
             st.write('該当データなし')
        else:
             st.write(f'該当データ: {len(data0)}件')
             for i in range(len(data0)):
                  st.write(f'■{data0[i][3]}（{data0[i][4]}）&nbsp;&nbsp; **id**：{data0[i][0]}  \n'
                           + f'- **情報入手日**：{data0[i][1]}  \n'
                           + f'- **供給**：{data0[i][2]}  \n'
                           + f'- **原因**：{data0[i][5]}  \n'
                           + f'- **確保量**：{data0[i][6]}  \n'
                           + f'- **消尽予測**：{data0[i][7]}  \n'
                           + f'- **回復**：{data0[i][8]}  \n'
                           + f'- **対応**：{data0[i][9]}  \n'
                           + f'- **資料**：{data0[i][10]}  \n'
                           + '-----'
                           )
        st.write('')
        st.write('#### ---解決済---')
        if len(data1) == 0:
             st.write('該当データなし')
        else:
             st.write(f'該当データ: {len(data1)}件')
             for i in range(len(data1)):
                  st.write(f'■{data1[i][3]}（{data1[i][4]}）&nbsp;&nbsp; **id**：{data1[i][0]}  \n'
                           + f'- **情報入手日**：{data1[i][1]}  \n'
                           + f'- **供給**：{data1[i][2]}  \n'
                           + f'- **原因**：{data1[i][5]}  \n' 
                           + f'- **確保量**：{data1[i][6]}  \n' 
                           + f'- **消尽予測**：{data1[i][7]}  \n' 
                           + f'- **回復**：{data1[i][8]}  \n' 
                           + f'- **対応**：{data1[i][9]}  \n' 
                           + f'- **資料**：{data1[i][10]}  \n' 
                           + f'-----' 
                           )