import streamlit as st
from PIL import Image

img = Image.open('logo.png')
st.image(img)

st.title('Link')
st.write('---------------------------------')
st.write('✓[Yahoo!JAPAN](https://www.yahoo.co.jp/)')

st.write('---------------------------------')
st.write('■ DI作成資料')
st.write('✓[添付文書改訂情報（Googleドライブ）](https://drive.google.com/drive/folders/1oWfXn2U6ntgeZ7WuOP7wXIre2AwFg7ly?usp=sharing)')
st.write('✓[包装変更情報（Googleドライブ）](https://drive.google.com/drive/folders/1IC6nnVKAjfh28nvKBS5NTUzg6f_XYdqo?usp=sharing)')
st.write('✓[フォーミュラリ#38（Googleドライブ）](https://drive.google.com/drive/folders/1k8Nsp5Mo0DmlVAEqQiRaCQncAY3Uvv0w?usp=sharing)')
st.write('✓相互作用エラー設定（Googleドライブ）  \n'
        + '・[ア行](https://drive.google.com/drive/folders/1C6RFutk30mCumC895SY0zRCqlWVST4QC?usp=sharing)  \n'
        + '・[カ行～サ行](https://drive.google.com/drive/folders/1-779eNFw_1RWiizxrRug4etLGmJ2qDJZ?usp=drive_link)  \n'
        + '・[タ行～ナ行](https://drive.google.com/drive/folders/1uesthl3SENipWn4asIlHtV71O72Qq2G0?usp=drive_link)  \n'
        + '・[ハ行](https://drive.google.com/drive/folders/11robGV1tttS7qeiCJCxQy_JY5B7cge3p?usp=sharing)  \n'
        + '・[マ行～ワ行](https://drive.google.com/drive/folders/1I6uv4SrbhDHv_Ow0Dkp4yN8bafkp07Jg?usp=drive_link)  \n'
        + '・[その他項目](https://drive.google.com/drive/folders/1K3OnACCyJKT5oGWGiEAoEuuyYwmiiPFT?usp=sharing)  \n'
        )
st.write('✓[採用薬の院内運用](https://drive.google.com/drive/folders/1tSW_ZDN1Oe19cvapkGJh6ZAd1gATtK1K?usp=drive_link)')

st.write('---------------------------------')
st.write('■ 医薬品・健康食品')
st.write('✓[PMDA医療用医薬品 情報検索](https://www.pmda.go.jp/PmdaSearch/iyakuSearch/)')
st.write('✓[PMDA医薬品・医療機器等安全性情報](https://www.pmda.go.jp/safety/info-services/drugs/calling-attention/safety-info/0043.html)')
st.write('✓[PMDA医薬品副作用報告受付サイト](https://www.estrigw.pmda.go.jp/Iryo/Login/Index?ReturnUrl=%2fIryo)（ユーザー名・パスワードが必要)')
st.write('✓[SAFE-DI](https://www.safe-di.jp/)（ユーザー名・パスワードが必要)')
st.write('✓[Lexicomp](https://www.uptodate.com/drug-interactions/#di-druglist)（薬物間相互作用検索）')
st.write('✓[「健康食品」の安全性・有効性情報](https://hfnet.nibiohn.go.jp/)')
st.write('---------------------------------')
st.write('■ 中毒')
st.write('✓[中毒情報センター](https://www.j-poison-ic.jp/)（ユーザー名・パスワードが必要)')
st.write('---------------------------------')
st.write('■ 妊婦・授乳婦')
st.write('✓[LactMed](https://www.ncbi.nlm.nih.gov/books/NBK501922/)')
st.write('✓[妊娠と薬情報センター](https://www.ncchd.go.jp/kusuri/)')
st.write('---------------------------------')
st.write('■ アンチドーピング')
st.write('✓[global DRO](https://www.globaldro.com/JP/search/input?pls=true)')
st.write('✓[JSPO　使用可能薬リスト](https://www.japan-sports.or.jp/medicine/doping/tabid537.html)')
st.write('---------------------------------')
st.write('■ 文献検索・辞書')
st.write('✓[メディカルオンライン](https://www.medicalonline.jp/)')
st.write('✓[医中誌](https://search.jamas.or.jp/search)')
st.write('✓[UpToDate](https://www.uptodate.com/contents/search)')
st.write('✓[PubMed](https://pubmed.ncbi.nlm.nih.gov/)')
st.write('✓[ClinicalKey](https://www.clinicalkey.jp/#!/)')
st.write('✓[Life Science Dictionary](https://lsd-project.jp/cgi-bin/lsdproj/ejlookup04.pl)')
st.write('✓[DeepL](https://www.deepl.com/ja/translator)')
st.write('---------------------------------')
st.write('■ ガイドライン・学会HP')
st.write('✓[NCCN](https://www.nccn.org/)')
st.write('✓日本化学療法学会  \n'
        + '・[VCM TDMソフトウェア PAT](https://www.chemotherapy.or.jp/modules/guideline/index.php?content_id=79)  \n'
        + '・[術後感染予防抗菌薬適正使用のための実践ガイドライン（Summary）](https://www.chemotherapy.or.jp/uploads/files/guideline/jyutsugo_shiyou_jissen.pdf)'
        )
st.write('✓日本腎臓病薬物療法学会  \n'
        + '・[腎機能低下時に最も注意が必要な薬剤投与量一覧](https://www.jsnp.org/ckd/yakuzaitoyoryo.php)  \n'
        + '・[eGFR・CCrの計算](https://www.jsnp.org/egfr/)'
        )
st.write('✓[白鷺病院　透析患者に対する投薬ガイドライン](http://www.shirasagi-hp.or.jp/goda/fmly/gate.html)')
         
st.write('---------------------------------')
st.write('■ その他')
st.write('✓[実務実習指導・管理システム](https://training-phm.fujifilm.com/Usersite)')