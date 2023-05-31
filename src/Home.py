import streamlit as st 
from main import Text_To_Speech # Sử dụng text_to_speech của file main.py chuyện văn bản thành giojgn nói
from PIL import Image # Hỗ trợ mở file image demo lên streamlit

st.title(":blue[TRỢ LÝ ẢO RA LỆNH, HỎI ĐÁP BẰNG GIỌNG NÓI] ")
col1,col2 = st.columns(2)
with col1:
    image = Image.open('bot.jpg') 
    st.image(image)
with col2:
    image = Image.open('1.jpg') 
    st.image(image)
st.header(':blue[CÁC TRẢI NGHIỆM MÀ BẠN CÓ THỂ SỬ DỤNG: ]')
st.subheader('👉 QUESTION AND ANSWER')   
st.subheader('👉 TRANSLATION')   
st.subheader('👉 RECOMMENDED PLACE')   


st.caption("MADE BY CAPHATRI")
# Phát âm thanh
Text_To_Speech("Xin chào ! Tôi là trợ lý ảo AI !")



