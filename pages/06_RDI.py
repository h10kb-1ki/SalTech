import streamlit as st
from PIL import Image

img = Image.open('logo.png')
st.image(img)

st.header("RDI計算")
def dose_intensity(dose, on, off):
    di = (dose * on)/(on + off)
    return round(di, 1)

col1, col2, col3 = st.columns([0.45, 0.1, 0.45])
with col1:
    st.subheader("標準", divider='grey')
    s_dose = st.number_input("標準投与量(mg/d)", step=1)
    s_on = st.selectbox("服用期間（週）", [1, 2, 3, 4, 5, 6], index=3)
    s_off = st.selectbox("休薬期間（週）", [1, 2, 3, 4, 5, 6], index=1)

with col3:
    st.subheader("減量", divider="grey")
    m_dose = st.number_input("減量投与量(mg/d)", step=1)
    m_on = st.selectbox("服用（週）", [1, 2, 3, 4, 5, 6], index=3)
    m_off = st.selectbox("休薬（週）", [1, 2, 3, 4, 5, 6], index=1)

st.write("  \n")
st.write("  \n")

if st.button("calc"):
    s_di = dose_intensity(s_dose, s_on, s_off)
    m_di = dose_intensity(m_dose, m_on, m_off)
    rdi = round((m_di * 100)/s_di, 1)

    st.write("  \n")
    st.write("  \n")
    st.write(f"◼︎標準&nbsp;{s_dose}mg/d&nbsp;&nbsp;{s_on}投{s_off}休  \n"
            + f"&nbsp;&nbsp;dose&nbsp;intensity:&nbsp;{s_di}mg/d")
    st.write(f"◼︎減量後&nbsp;{m_dose}mg/d&nbsp;&nbsp;{m_on}投{m_off}休  \n"
            + f"&nbsp;&nbsp;dose&nbsp;intensity:&nbsp;{m_di}mg/d")
    st.write(f"★Relative&nbsp;dose&nbsp;intensity:&nbsp;{rdi}%")