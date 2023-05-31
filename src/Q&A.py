import streamlit as st
import openai
import openai_api_key
from main import Text_To_Speech,Speech_To_Text # Sử dụng text_to_speech và speech_to_text từ file main.py

openai.api_key = openai_api_key.key # Tạo openai api key
st.title(":blue[HỎI ĐÁP TẤT CẢ MỌI THỨ BẠN MUỐN ]") 

if st.button('BẮT ĐẦU'):
        st.write('Listen....')
        prompt = Speech_To_Text() # Nhận thông tin từ giọng nói của người dùng, lưu dưới dạng text
        
        if prompt:
                st.write("You entered: ", prompt)
                # Sử dụng api lấy response, lưu dưới dạng text
                resp = openai.Completion.create(
                model = "text-davinci-003",
                prompt = prompt,
                max_tokens = 1024,
                temperature = 0.3       
                )
                result = resp.choices[0].text
                print(result)
                st.text_area("Answer: ", value=result, height = 600, max_chars = None)
                # Từ text response, sử dụng text_to_speech để đưa ra response tới người dùng bằng âm thanh
                Text_To_Speech(result)
        else:
                # Click button để thực hiện hỏi đáp lại
                Text_To_Speech("Vui lòng bấm bắt đầu để thực hiện lại")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")

st.subheader(":green[Lưu ý khi sử dụng: ]")
st.write("**Click 'BẮT ĐẦU' để thực hiện hỏi (Đợi sau 2s click rồi hỏi sẽ hiệu quả hơn) !**")
st.write("**Câu hỏi của bạn sẽ được ghi lại và in ra dưới dạng text, hệ thống sẽ thực hiện trả lời câu hỏi của bạn !**" )
st.write("**Click 'BẮT ĐẦU' để thực hiện hỏi câu hỏi tiếp theo !**")