import streamlit as st
from PIL import Image

st.title('論文の読み方')
#image = Image.open('table.png')
#st.image(image)

a = st.number_input('介入群・Outcome(+)', step=1)
b = st.number_input('介入群・Outcome(-)', step=1)
c = st.number_input('対象群・Outcome(+)', step=1)
d = st.number_input('対象群・Outcome(-)', step=1)

btn = st.button('計算')
if btn:
    EER = a/(a+b)
    CER = c/(c+d)
    RR = EER/CER
    RRR = 1-RR
    ARR = CER-EER
    NNT = 1/ARR
    st.write('')
    st.write(f'介入群合計: {a+b} 例  \n' + 
             f'対象群合計: {c+d} 例  \n' +
             f'Outcome(+)合計: {a+c} 例  \n' +
             f'Outcome(-)合計: {b+d} 例  \n' +
             f'総計: {a+b+c+d}例'
             )
    st.write('---')
    st.write(f'介入群の発生率 (EER): {EER*100:.1f} %  \n' +
             f'対象群の発生率 (CER): {CER*100:.1f} %  \n' +
             f'相対リスク (RR): {RR*100:.1f} %  \n' +
             f'相対リスク減少率 (RRR): {RRR*100:.1f} %  \n' +
             f'絶対リスク減少率 (ARR): {ARR*100:.1f} %  \n' +
             f'治療必要数 (NNT): {NNT:.0f}  \n'
             )
