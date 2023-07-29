import streamlit as st

st.title('栄養必要量の計算')

bw = st.sidebar.slider('■体重 (kg)', 0, 150, 50, step=1)
height = st.sidebar.slider('■身長 (cm)', 100, 200, 150, step=1)
age = st.sidebar.slider('■年齢', 15, 99, 50, step=1)
gender = st.sidebar.radio('■性別', ['男性', '女性'])
st.sidebar.write('')

af_str = st.sidebar.selectbox('■活動量', ['寝たきり', 'ベッド上安静', 'ベッド以外での活動あり', 'やや軽い労作', '中等度の労作', '重度の労作'])
dict_af = {'寝たきり': 1.1, 
           'ベッド上安静': 1.2, 
           'ベッド以外での活動あり': 1.3, 
           'やや軽い労作': 1.5, 
           '中等度の労作': 1.7, 
           '重度の労作': 1.9}
af = dict_af[f'{af_str}']
st.sidebar.write('')

sf_str = st.sidebar.selectbox('■ストレス', 
                      ['ストレス無し', '飢餓', '手術（軽度侵襲）', '手術（中等度侵襲）', '手術(高度侵襲)', 
                       '骨折', '頭部損傷＋ステロイド使用', '感染症（軽度）', '感染症（中等度～重度）', 
                       '熱傷（体表面積の40%）', '熱傷（体表面積の100%）'])
dict_sf = {'ストレス無し': 1.0, 
           '飢餓': 0.84, 
           '手術（軽度侵襲）': 1.1, 
           '手術（中等度侵襲）': 1.2, 
           '手術(高度侵襲)': 1.8, 
           '骨折': 1.35, 
           '頭部損傷＋ステロイド使用': 1.6, 
           '感染症（軽度）': 1.2,  
           '感染症（中等度～重度）': 1.5, 
           '熱傷（体表面積の40%）': 1.5, 
           '熱傷（体表面積の100%）': 2.0}
sf = dict_sf[f'{sf_str}']
st.sidebar.write('')
BEE = st.sidebar.selectbox('■基礎代謝量の算出方法', ['Harris-Benedict式', '簡易式', '体重から推測'])

def calc_basic(bw, height, age, gender, af, sf):
    BMI = bw/(height/100)**2
    if gender == '男性':
        BEE_HB = 66.47 + (13.75*bw) + (5*height) - (6.75*age)
        BEE_easy = 14.1*bw + 620
    else:
        BEE_HB = 655.1 + (9.56*bw) + (1.85*height) -(4.68*age)
        BEE_easy = 10.8*bw + 620
    BEE_bw = 25*bw
    return BMI, BEE_HB, BEE_easy, BEE_bw

def totalCal(bee, af, sf):
    totalCal = bee*af*sf
    return totalCal


BMI, BEE_HB, BEE_easy, BEE_bw = calc_basic(bw, height, age, gender, af, sf)
if BEE == 'Harris-Benedict式':
    st.write(f'基礎代謝量 BEE: {BEE_HB:.0f}  kcal')
elif BEE == '簡易式':
    st.write(f'基礎代謝量 BEE: {BEE_easy:.0f}  kcal')
else:
    st.write(f'基礎代謝量 BEE: {BEE_bw:.0f}  kcal')
st.write(f'活動係数 AF: {str(af)}')
st.write(f'ストレス係数 SF: {str(sf)}')

    
btn = st.button('計算')

if btn:
    IBW = 22*(height/100)**2
    if BMI > 25:
        judge = f'肥満（理想体重 {IBW:.1f}kg）'
    elif BMI <= 18.5:
        judge = f'痩せ（理想体重 {IBW:.1f}kg）'
    else:
        judge = '標準'      
    st.write(f'BMI: {BMI:.1f}---{judge}')

    if BEE == 'Harris-Benedict式':
        st.write(f'総消費カロリー: {totalCal(BEE_HB, af, sf):.0f} kcal')
    elif BEE == '簡易式':
        st.write(f'総消費カロリー: {totalCal(BEE_easy, af, sf):.0f} kcal')
    else:
        st.write(f'総消費カロリー: {totalCal(BEE_bw, af, sf):.0f} kcal')


