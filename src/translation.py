import streamlit as st
import googletrans
from googletrans import Translator # Thư viện hỗ trợ dịch văn bản
from gtts import gTTS #Chuyển văn bản thành âm thanh của google
import playsound #Phát âm thanh từ file mp3
import os # Truy cập, xử lí file trong hệ thống
from PIL import Image # Hỗ trợ mở file image demo lên streamlit
# Khởi tạo trinh dịch
translator = Translator()
st.title(":blue[DỊCH NGÔN NGỮ]")
# Chuyển văn bản thành âm thanh, dùng để phát âm thanh result
def Text_To_Speech(text, lang):
    # Chuyển văn bản thành âm thanh của google
    tts = gTTS(text=text, lang=lang)
    # lưu giọng nói vào file mp3
    file_name = 'voice.mp3'
    tts.save(file_name)
    # phát tệp âm thanh
    try:
        playsound.playsound(file_name)
    except:
        st.error('Please click again', icon="🚨")
        pass

    # xóa filename  
    os.remove(file_name)
# Danh sách các ngôn ngữ hỗ trợ
case = {
    'af': 'Afrikaans', 
    'sq': 'Albanian', 
    'am': 'Amharic', 
    'ar': 'Arabic', 
    'hy': 'Armenian', 
    'az': 'Azerbaijani', 
    'eu': 'Basque', 
    'be': 'Belarusian', 
    'bn': 'Bengali', 
    'bs': 'Bosnian', 
    'bg': 'Bulgarian', 
    'ca': 'Catalan', 
    'ceb': 'Cebuano', 
    'ny': 'Chichewa', 
    'zh-cn': 'Chinese (simplified)', 
    'zh-tw': 'Chinese (traditional)', 
    'co': 'Corsican', 
    'hr': 'Croatian', 
    'cs': 'Czech', 
    'da': 'Danish', 
    'nl': 'Dutch', 
    'en': 'English', 
    'eo': 'Esperanto', 
    'et': 'Estonian', 
    'tl': 'Filipino', 
    'fi': 'Finnish', 
    'fr': 'French', 
    'fy': 'Frisian', 
    'gl': 'Galician', 
    'ka': 'Georgian', 
    'de': 'German', 
    'el': 'Greek', 
    'gu': 'Gujarati', 
    'ht': 'Haitian Creole', 
    'ha': 'Hausa', 
    'haw': 'Hawaiian', 
    'iw': 'Hebrew', 
    'he': 'Hebrew', 
    'hi': 'Hindi', 
    'hmn': 'Hmong', 
    'hu': 'Hungarian', 
    'is': 'Icelandic', 
    'ig': 'Igbo', 
    'id': 'Indonesian', 
    'ga': 'Irish', 
    'it': 'Italian', 
    'ja': 'Japanese', 
    'jw': 'Javanese', 
    'kn': 'Kannada', 
    'kk': 'Kazakh', 
    'km': 'Khmer', 
    'ko': 'Korean', 
    'ku': 'Kurdish (kurmanji)', 
    'ky': 'Kyrgyz', 
    'lo': 'Lao', 
    'la': 'Latin', 
    'lv': 'Latvian', 
    'lt': 'Lithuanian', 
    'lb': 'Luxembourgish', 
    'mk': 'Macedonian', 
    'mg': 'Malagasy', 
    'ms': 'Malay', 
    'ml': 'Malayalam', 
    'mt': 'Maltese', 
    'mi': 'Maori', 
    'mr': 'Marathi', 
    'mn': 'Mongolian', 
    'my': 'Myanmar (burmese)', 
    'ne': 'Nepali', 
    'no': 'Norwegian', 
    'or': 'Odia', 
    'ps': 'Pashto', 
    'fa': 'Persian', 
    'pl': 'Polish', 
    'pt': 'Portuguese', 
    'pa': 'Punjabi', 
    'ro': 'Romanian', 
    'ru': 'Russian', 
    'sm': 'Samoan', 
    'gd': 'Scots gaelic', 
    'sr': 'Serbian', 
    'st': 'Sesotho', 
    'sn': 'Shona', 
    'sd': 'Sindhi', 
    'si': 'Sinhala', 
    'sk': 'Slovak', 
    'sl': 'Slovenian', 
    'so': 'Somali', 
    'es': 'Spanish', 
    'su': 'Sundanese', 
    'sw': 'Swahili', 
    'sv': 'Swedish', 
    'tg': 'Tajik', 
    'ta': 'Tamil', 
    'te': 'Telugu', 
    'th': 'Thai', 
    'tr': 'Turkish', 
    'uk': 'Ukrainian', 
    'ur': 'Urdu', 
    'ug': 'Uyghur', 
    'uz': 'Uzbek', 
    'vi': 'Vietnamese', 
    'cy': 'Welsh', 
    'xh': 'Xhosa', 
    'yi': 'Yiddish', 
    'yo': 'Yoruba', 
    'zu': 'Zulu'
}

col1, col2,col3 = st.columns(3)
src = ''
with col1:
    option1 = st.selectbox(
        'Chọn ngôn ngữ gốc',
        ('Tự phát hiện ngôn ngữ', 'Afrikaans','Albanian', 'Amharic', 'Arabic', 'Armenian','Azerbaijani','Basque', 'Belarusian','Bengali','Bosnian',  'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (simplified)',  'Chinese (traditional)', 'Corsican', 'Croatian', 'Czech',  'Danish',  'Dutch', 'English',  'Esperanto', 'Estonian','Filipino', 'Finnish', 'French','Frisian',  'Galician', 'Georgian', 'German','Greek','Gujarati','Haitian Creole', 'Hausa', 'Hawaiian',  'Hebrew', 'Hebrew','Hindi','Hmong','Hungarian','Icelandic', 'Igbo','Indonesian', 'Irish','Italian','Japanese',  'Javanese', 'Kannada','Kazakh','Khmer',  'Korean', 'Kurdish (kurmanji)',  'Kyrgyz', 'Lao',  'Latin',  'Latvian',  'Lithuanian',  'Luxembourgish',  'Macedonian', 'Malagasy','Malay',  'Malayalam','Maltese', 'Maori', 'Marathi',  'Mongolian', 'Myanmar (burmese)',  'Nepali',  'Norwegian',  'Odia',  'Pashto', 'Persian', 'Polish',  'Portuguese', 'Punjabi', 'Romanian',  'Russian',  'Samoan',  'Scots gaelic', 'Serbian',  'Sesotho', 'Shona', 'Sindhi',  'Sinhala',  'Slovak',  'Slovenian', 'Somali',  'Spanish',  'Sundanese', 'Swahili',  'Swedish','Tajik', 'Tamil',  'Telugu',  'Thai',  'Turkish',  'Ukrainian', 'Urdu','Uyghur', 'Uzbek',  'Vietnamese',  'Welsh', 'Xhosa',  'Yiddish',  'Yoruba', 'Zulu'))
    # Nhập văn bản gốc
    text = st.text_area("Nhập văn bản", height = 200, max_chars = None)
    if option1 == "Tự phát hiện ngôn ngữ":
        if text:
            # Sử dụng tính năng phát hiện ngôn ngữ của thư viện để phát hiện ngôn ngữ của văn bản do người dùng nhập vào
            src = translator.detect(text).lang
            st.success('Phát hiện ngôn ngữ: ' + case[src])
        else :
            st.warning("Waiting....")

    else:
        # Thực hiện lấy mã ngôn ngữ tương ứng với ngôn ngữ được chọn
        # ví dụ : Tiếng việt - vi, Tiếng Anh - en
        for key, val in case.items() :
            if val == option1:
                src = key
                break

with col2:
    image = Image.open('convert.jpg') 
    st.image(image)
with col3:
    option2 = st.selectbox(
        'Chọn ngôn ngữ đích',
        ('Afrikaans','Albanian', 'Amharic', 'Arabic', 'Armenian','Azerbaijani','Basque', 'Belarusian','Bengali','Bosnian',  'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (simplified)',  'Chinese (traditional)', 'Corsican', 'Croatian', 'Czech',  'Danish',  'Dutch', 'English',  'Esperanto', 'Estonian','Filipino', 'Finnish', 'French','Frisian',  'Galician', 'Georgian', 'German','Greek','Gujarati','Haitian Creole', 'Hausa', 'Hawaiian',  'Hebrew', 'Hebrew','Hindi','Hmong','Hungarian','Icelandic', 'Igbo','Indonesian', 'Irish','Italian','Japanese',  'Javanese', 'Kannada','Kazakh','Khmer',  'Korean', 'Kurdish (kurmanji)',  'Kyrgyz', 'Lao',  'Latin',  'Latvian',  'Lithuanian',  'Luxembourgish',  'Macedonian', 'Malagasy','Malay',  'Malayalam','Maltese', 'Maori', 'Marathi',  'Mongolian', 'Myanmar (burmese)',  'Nepali',  'Norwegian',  'Odia',  'Pashto', 'Persian', 'Polish',  'Portuguese', 'Punjabi', 'Romanian',  'Russian',  'Samoan',  'Scots gaelic', 'Serbian',  'Sesotho', 'Shona', 'Sindhi',  'Sinhala',  'Slovak',  'Slovenian', 'Somali',  'Spanish',  'Sundanese', 'Swahili',  'Swedish','Tajik', 'Tamil',  'Telugu',  'Thai',  'Turkish',  'Ukrainian', 'Urdu','Uyghur', 'Uzbek',  'Vietnamese',  'Welsh', 'Xhosa',  'Yiddish',  'Yoruba', 'Zulu'), key=None)
    if option2:
        # Thực hiện lấy mã ngôn ngữ tương ứng với ngôn ngữ được chọn
        # ví dụ : Tiếng việt - vi, Tiếng Anh - en
        for key, val in case.items() :
            if val == option2:
                dest = key
                break
    if src:
        # Thực hiện dịch ngôn ngữ, hiển thị result ra màn hình
        st.text_area("Result: ", translator.translate(text, src=src, dest = dest).text, height = 200, max_chars = None)
        # Từ result là 1 đoạn text, phát âm thanh của đoạn text đó với text_to_speech
        if st.button('READ'):
            try:
                Text_To_Speech(translator.translate(text, src=src, dest = dest).text, dest)
            except:
                # 1 số ngôn ngữ không hỗ trợ đọc văn bản
                st.error("NOT SUPPORTED THIS LANGUAGE")
                Text_To_Speech("Not supported", 'en')
                
st.write("  ")
st.write("  ")
st.write("  ")


st.subheader(":green[Lưu ý khi sử dụng: ]")
st.write("**Hệ thống có chức năng tự phát hiện ngôn ngữ người dùng nhập vào**")
st.write("**Một số ngôn ngữ không hỗ trợ đọc**" )
st.write("**Nếu click 'READ' bị lỗi không đọc văn bản, vui lòng click lại**")
