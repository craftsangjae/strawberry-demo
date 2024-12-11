import streamlit as st
import os

import pandas as pd
from PIL import Image
import io
import requests
import base64
# Load environment variables
SERVING_HOST_URL = os.getenv('SERVING_HOST_URL', '')

# 클래스맵
CLASS_NAME = {
    "2": "정상",
    "3": "잿빛곰팡이병",
    "4": "흰가루병"
}

# Wider Layout
st.set_page_config(
    page_title="딸기 병충해 분류",
    layout="wide"
)

st.title("딸기 병충해 분류")

st.markdown(
    """
    <style>
    .img-container img {
        height: 60vh !important;
        width: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 서버 URL 입력 받기
server_name = st.text_input("service name")

# 파일 업로드 위젯 생성
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and server_name:
    # Create two columns for side-by-side display
    left_column, right_column = st.columns([1, 1])  # Adjust column width ratios if needed

    df = None
    with left_column:
        st.subheader("선택한 이미지")
        image = Image.open(uploaded_file)

        # 이미지를 base64로 인코딩
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        value = buffered.getvalue()
        img_b64 = base64.b64encode(value).decode()

        st.markdown(
            f"""
            <div class="img-container">
                <img src="data:image/jpg;base64,{img_b64}" alt="uploaded image">
            </div>
            """,
            unsafe_allow_html=True
        )

        response = requests.post(
            os.path.join(SERVING_HOST_URL, server_name, 'infer'),
            files={"file": value}
        )
        if response.status_code == 200:
            result = response.json()
            df = pd.DataFrame({
                '라벨': [CLASS_NAME[r['label']] for r in result],
                '점수': [r['score'] for r in result]
            })

    with right_column:
        st.subheader("결과")
        if df is not None:
            st.bar_chart(df.set_index('라벨'))
else:
    st.info("이미지를 업로드해주세요. (jpg, jpeg, png 포맷 지원)")
