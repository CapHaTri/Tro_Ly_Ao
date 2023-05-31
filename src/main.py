import speech_recognition as sr #Nhận dạng giọng nói
from gtts import gTTS #Chuyển văn bản thành âm thanh của google
import playsound #Phát âm thanh từ file mp3
import os #Truy cập, xử lý file hệ thống


# CHUYỂN VĂN BẢN SANG GIỌNG NÓI
# - Input vào sẽ là 1 văn bản
# - Thực hiện đọc đoạn văn bản từ input, phát output là âm thanh với văn bản được nhập từ input
def Text_To_Speech(text):
    # Chuyển văn bản thành âm thanh của google
    tts = gTTS(text=text, lang='vi')
    # lưu giọng nói vào file mp3
    file_name = 'voice.mp3'
    tts.save(file_name)
    # phát tệp âm thanh
    playsound.playsound(file_name)
    # xóa filename
    os.remove(file_name)

# CHUYỂN GIỌNG NÓI SANG VĂN BẢN
# - Input sẽ là giọng nói được ghi nhận nói vào từ micro
# - Xử lý và cho ra output là 1 đoạn text chứa nội dung input giọng nói
def Speech_To_Text():
    # Khởi tạo trình nhận dạng
    r = sr.Recognizer()
    # Nói vào từ microphone
    with sr.Microphone() as source:
        print("Listen.....")
        # Đọc dữ liệu âm thanh từ micro
        audio_data = r.record(source, duration= 5)
        try:
            # chuyển lời nói thành văn bản
            text = r.recognize_google(audio_data, language='vi')
        except:
            text = ''
        print(text)
    return text

