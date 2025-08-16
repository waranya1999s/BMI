import streamlit as st

import streamlit as st
import requests
from pathlib import Path

API_URL = "https://api-voice.botnoi.ai/openapi/v1/generate_audio"
API_TOKEN = "piJ5bwPRpWRKWZ0M2oqJp2gFdG01Zt9Q"

st.set_page_config(page_title='Body Mass Index : Web Application',page_icon='😎')

st.title('ค่า BMI')
st.snow()
st.image('bmi1.jpg')
kg=st.number_input('นํ้าหนัก (Kg):')
cm=st.number_input('ส่วนสูง (Cm):')

import io
if st.button('คำนวณ'):
    bmi=kg/(cm/100)**2
    tt = f'ค่า BMI ของคุณคือ {bmi:.2f}'
    if bmi < 18.50:
        st.info(tt)
        st.image('image1.png')
        word='ผอมเกินไป'

    elif bmi < 24.9:
        st.success(tt)
        st.image('image2.png')
        word='ปกติจ้า'
        
    elif bmi < 29.90:
        st.warning(tt)
        st.image('image3.png')
        word='อ้วนนนน'
        
    elif bmi = 0:
        st.text( )
    
    else:
        st.error(tt)

    payload = {
        "text": word,
        "speaker": "1",
        "volume": 1,
        "speed": 1,
        "type_media": "mp3",
        "save_file": "true",
        "language": "th",
        "page": "user"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "botnoi-token": API_TOKEN
    }

    try:
        res = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        res.raise_for_status()
        data = res.json()
        st.write("API Response:", data)

        # ดึง URL ไฟล์เสียง
        audio_url = (
            data.get("url")
            or data.get("audio_url")
            or (data.get("data") or {}).get("url")
        )

        if audio_url:
            audio_bytes = requests.get(audio_url, timeout=30).content
            out_path = Path("botnoi_voice.mp3")
            out_path.write_bytes(audio_bytes)
            st.success(f"✅ บันทึกเสียงเรียบร้อย → {out_path.resolve()}")
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.error("ไม่พบลิงก์ไฟล์เสียงใน response")

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")





        
col1,col2 = st.columns(2)
with col1:
    if st.button('ฟังเพลง'):
        st.video('https://youtu.be/wn0IyvGBeUI?si=MPGe3oAYYWyemaoi')
    
with col2:
    if st.button('vlog'):
        st.video('https://youtu.be/1BJvsUG9wIA?si=IkLZYv199N7IPO9Q')

