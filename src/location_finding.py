import streamlit as st
import pandas as pd # Hỗ trợ các công cụ làm việc với dữ liệu
import re # Xử lý chuỗi 
st.title(":blue[ĐỀ XUẤT ĐỊA ĐIỂM CẦN TÌM KIẾM]")
col1, col2 = st.columns(2)
with col1:
    # Chọn vị trí
    option1 = st.selectbox("Vui lòng chọn ",
                           ( "Chọn ví trí", "Quận 1", "Quận 2", "Quận 3", "Quận 4", "Quận 5", "Quận 6", "Quận 7", "Quận 8", "Quận 9", "Quận 10", "Quận 11", "Quận 12", "Quận Bình Thạnh", "Quận Tân Bình", "Quận Phú Nhuận", "Quận Tân Phú", "Quận Gò Vấp", "Quận Bình Tân", "Tp. Thủ Đức", "Huyện Bình Chánh", "Huyện Nhà Bè", "Huyện Hóc Môn", "Huyện Củ Chi", "Huyện Cần Giờ"))

with col2:
    # Chọn địa điểm cần tìm kiếm
    option2 = st.selectbox("Vui lòng chọn",
        ("Coffee", "Billards", "Nhà hàng", "Sân bóng đá")
    )
# Hàm xử lý dữ liệu
def edit(df):
    # Rename 
    rename = {'name': 'Tên', 'address': 'Địa Chỉ', 
                'website': 'Website', 'phone_number': 'SĐT', 'reviews_count': 'Số lượt Review', 'reviews_average': 'Điểm đánh giá trung bình'}
    df.rename(columns=rename, inplace=True) 
    # Loại bỏ các trường trùng nhau
    df.drop_duplicates(inplace=True)
    # Thưc hiện định dạng lại dữ liệu trong trường địa chỉ, phục vụ việc truy xuất dễ dàng hơn
    # Tạo 1 cột địa chỉ rút gọn để phục vụ cho việc show dữ liệu
    address_clean = []

    for text in df["Địa Chỉ"]:
        if text is not None:
            text_parts = text.split(", ")  
            text_parts = text_parts[len(text_parts)-3]
            if text_parts == "Bình Thạnh":
                text_parts = "Quận Bình Thạnh"
            if text_parts == "District 9":
                text_parts = "Quận 9"
            if text_parts == "Tân Bình":
                text_parts = "Quận Tân Bình"
            if text_parts == "Phú Nhuận":
                text_parts = "Quận Phú Nhuận"
            if text_parts == "Tân Phú":
                text_parts = "Quận Tân Phú"
            if text_parts == "Gò Vấp":
                text_parts = "Quận Gò Vấp"
            if text_parts == "Bình Tân":
                text_parts = "Quận Bình Tân"
            if "Thủ Đức" in text_parts:
                text_parts = "Tp. Thủ Đức"
            if text_parts == "Bình Chánh":
                text_parts = "Huyện Bình Chánh"
            if text_parts == "Nhà Bè":
                text_parts = "Huyện Nhà Bè"
            if text_parts == "Hóc Môn":
                text_parts = "Huyện Hóc Môn"
            if text_parts == "Củ Chi":
                text_parts = "Huyện Củ Chi"
            if text_parts == "Cần Giờ":
                text_parts = "Huyện Cần Giờ"
            address_clean.append(text_parts)
        else:
            address_clean.append(None)
    df["Địa Chỉ Rút Gọn"] = address_clean
    # Sắp xếp theo điểm đánh giá trung bình
    df =df.sort_values('Điểm đánh giá trung bình', ascending=False)
    # Gán các trường none là 0
    df = df.fillna(0)
    df.replace('facebook.com', 0, inplace=True)
    return df
if st.button("TÌM KIẾM"):
    if option2 == "Coffee":
        # Đọc file csv
        cf_df = pd.read_csv('C:/Users/MSI/OneDrive/Python/Đồ án Python/data/coffee_data.csv', index_col=0)
        cf_df = edit(cf_df) 
        if option1:
            dem = 0
            # Trích xuất thông tin theo lựa chọn của người dùng
            for index, row in cf_df[cf_df['Địa Chỉ Rút Gọn'] == option1].iterrows():
                name = row["Tên"]
                address = row["Địa Chỉ"]
                website = row["Website"]
                SĐT = row["SĐT"]
                review_count = row["Số lượt Review"]
                review_average = row["Điểm đánh giá trung bình"]
                images = row["images"]
                urls = re.findall(r'https?://\S+', images)
                # Lựa chọn nơi có số lượng review và điểm số phù hợp
                if review_count >=15:
                    st.subheader(str(dem + 1) + ". " +  name)
                    col1,col2 = st.columns(2)
                    with col1:
                        st.image(urls[0][:-2])
                    with col2:
                        st.image(urls[1][:-2])
                    st.markdown('##### 👉 Địa chỉ :  {}'.format(address))
                    if website != 0 and website != "facebook.com":
                        st.markdown('##### 👉 WEBSITE :  {}'.format(website)) 
                    if SĐT != 0:
                        st.markdown('##### 👉 SĐT :  {}'.format(SĐT))   
                    if review_count != 0:
                        st.markdown('##### 👉 Số lượt Review:  {}'.format(str(int(review_count))))
                    if review_average != 0:
                        st.markdown('##### 👉 Điểm đánh giá trung bình:  {}'.format(str(review_average)))
                    dem +=1
                else:
                    continue
                if dem == 10:
                    break
    if option2 == "Nhà hàng":
        # Đọc file csv
        cf_df = pd.read_csv('C:/Users/MSI/OneDrive/Python/Đồ án Python/data/res_data.csv', index_col=0)
        cf_df = edit(cf_df) 
        if option1:
            dem = 0
            # Trích xuất thông tin theo lựa chọn của người dùng
            for index, row in cf_df[cf_df['Địa Chỉ Rút Gọn'] == option1].iterrows():
                name = row["Tên"]
                address = row["Địa Chỉ"]
                website = row["Website"]
                SĐT = row["SĐT"]
                review_count = row["Số lượt Review"]
                review_average = row["Điểm đánh giá trung bình"]
                images = row["images"]
                urls = re.findall(r'https?://\S+', images)
                # Lựa chọn nơi có số lượng review và điểm số phù hợp
                if review_count >=15:
                    st.subheader(str(dem + 1) + ". " +  name)
                    col1,col2 = st.columns(2)
                    with col1:
                        st.image(urls[0][:-2])
                    with col2:
                        st.image(urls[1][:-2])
                    st.markdown('##### 👉 Địa chỉ :  {}'.format(address))
                    if website != 0 and website != "facebook.com":
                        st.markdown('##### 👉 WEBSITE :  {}'.format(website)) 
                    if SĐT != 0:
                        st.markdown('##### 👉 SĐT :  {}'.format(SĐT))   
                    if review_count != 0:
                        st.markdown('##### 👉 Số lượt Review:  {}'.format(str(int(review_count))))
                    if review_average != 0:
                        st.markdown('##### 👉 Điểm đánh giá trung bình:  {}'.format(str(review_average)))
                    dem +=1
                else:
                    continue
                if dem == 10:
                    break
    if option2 == "Billards":
        # Đọc file csv
        cf_df = pd.read_csv('C:/Users/MSI/OneDrive/Python/Đồ án Python/data/bida_data.csv', index_col=0)
        cf_df = edit(cf_df) 
        if option1:
            dem = 0
            # Trích xuất thông tin theo lựa chọn của người dùng
            for index, row in cf_df[cf_df['Địa Chỉ Rút Gọn'] == option1].iterrows():
                name = row["Tên"]
                address = row["Địa Chỉ"]
                website = row["Website"]
                SĐT = row["SĐT"]
                review_count = row["Số lượt Review"]
                review_average = row["Điểm đánh giá trung bình"]
                images = row["images"]
                urls = re.findall(r'https?://\S+', images)
                # Lựa chọn nơi có số lượng review và điểm số phù hợp
                if review_count >=0:
                    st.subheader(str(dem + 1) + ". " +  name)
                    col1,col2 = st.columns(2)
                    with col1:
                        st.image(urls[0][:-2])
                    with col2:
                        st.image(urls[1][:-2])
                    st.markdown('##### 👉 Địa chỉ :  {}'.format(address))
                    if website != 0 and website != "facebook.com":
                        st.markdown('##### 👉 WEBSITE :  {}'.format(website)) 
                    if SĐT != 0:
                        st.markdown('##### 👉 SĐT :  {}'.format(SĐT))   
                    if review_count != 0:
                        st.markdown('##### 👉 Số lượt Review:  {}'.format(str(int(review_count))))
                    if review_average != 0:
                        st.markdown('##### 👉 Điểm đánh giá trung bình:  {}'.format(str(review_average)))
                    dem +=1
                else:
                    continue
                if dem == 10:
                    break
    
st.write("  ")
st.write("  ")
st.write("  ")


st.subheader(":green[Lưu ý khi sử dụng: ]")
st.write("**Hỗ trợ tìm kiếm cách dịch vụ: Coffee, Nhà hàng - quán ăn, Billiards, Sân bóng đá, ...**")
st.write("**Hệ thống đề xuất các địa điểm trong khu vực TP HCM**")
st.write("**Danh sách được đưa ra dựa trên lượt đánh giá của khách hàng**" )
