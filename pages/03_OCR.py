import streamlit as st
from PIL import ImageGrab, Image
import numpy as np
import io
from io import BytesIO
import base64
from google.oauth2 import service_account
from google.cloud import vision

img = Image.open('logo.png')
st.image(img, use_column_width=True)

st.title('光学文字認識')
st.write('---Powered by google Cloud Vision---')

photo = st.checkbox('写真')
if photo:
    file_type = st.selectbox('画像のファイル形式を選択', ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tif', 'svg'])
    uploaded_file = st.file_uploader("ファイルアップロード", type=file_type, accept_multiple_files=False)

    # Create API client #streamlit: app dashboard > Secretsでsecretsを編集
    # https://docs.streamlit.io/knowledge-base/tutorials/databases/gcs
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"]
    )

    if uploaded_file:
        image=Image.open(uploaded_file)
        img_array = np.array(image)
        st.image(img_array,caption = 'プレビュー',use_column_width = True)

        client = vision.ImageAnnotatorClient(credentials=credentials)

        #PILで開いた画像をbase64形式に変換
        def pil_image_to_base64(image):
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            str_encode_file = base64.b64encode(buffered.getvalue()).decode("utf-8")
            return str_encode_file

        content = pil_image_to_base64(image)
        ocr_image = vision.Image(content=content)
        response =  client.document_text_detection(
                image=ocr_image,
                image_context={'language_hints': ['ja']},
                #image_context={'language_hints': ['en']}
            )
        output_text = ''
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        output_text += ''.join([
                            symbol.text for symbol in word.symbols
                        ])
                    output_text += '\n'
        st.write('■OCR結果：')
        st.write(output_text)
        
screenshot = st.checkbox('スクリーンショット')
if screenshot:
    def ocr():    
        img = ImageGrab.grabclipboard()  #クリップボードの画像を取得
        if img is None:
            output_text = '（クリップボードに画像がありません）'
        else:
            img.save('ocr.png')
            client = vision.ImageAnnotatorClient()
            with io.open('ocr.png', 'rb') as image_file:
                content = image_file.read()

            image = vision.Image(content=content)
            response =  client.document_text_detection(
                    image=image,
                    image_context={'language_hints': ['ja']},
                )
            output_text = ''
            for page in response.full_text_annotation.pages:
                for block in page.blocks:
                    for paragraph in block.paragraphs:
                        for word in paragraph.words:
                            output_text += ''.join([
                                symbol.text for symbol in word.symbols
                            ])
                        output_text += '\n'
        return output_text

    st.write('Screenshot OCR for WebApp')
    btn = st.button('OCR')
    if btn:
        st.write('■OCR結果：')
        st.write(ocr())
