import streamlit as st  
from st_pages import Page, Section, show_pages, add_page_title
add_page_title()
# Chia giao diện thành nhiều mục, mỗi mục là 1 trang và 1 source khác nhau thực hiện chức năng khác nhau
show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("Q&A.py", "QUESTION AND ANSWER", ":books:"),
        Page("translation.py", "TRANSLATION", ":candy:"),
        Page("location_finding.py", "RECOMMENDED PLACE", ":🎈️:"),
        Page("images.py", "RECOMMENDED IMAGES", ":💪:"),
    ]
)
