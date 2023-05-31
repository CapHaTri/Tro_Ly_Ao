from playwright.sync_api import sync_playwright # Hỗ trợ tương tác với các trang web, phục vụ việc crawl data
from dataclasses import dataclass, asdict, field # Định nghĩa các lớp dữ liệu
import pandas as pd # Hỗ trợ các công cụ làm việc với dữ liệu
@dataclass
class Business:
    # Xây dựng dữ liệu Business
    name: str = None # Dùng để lưu tên
    address: str = None # Dùng để lưu địa chỉ
    website: str = None # Dùng để lưu địa chỉ website
    phone_number: str = None # Dùng để lưu sđt
    reviews_count: int = None # Dùng để lưu số lượt review
    reviews_average: float = None # Dùng để lưu điểm review trung bình
    images: str = None # Dùng để lưu ảnh
@dataclass
class BusinessList:
    #Xây dựng danh sách của đối tượng business và lưu dữ liệu vào file csv

    business_list : list[Business] = field(default_factory=list)
    
    def dataframe(self):
        # Chuyển business_list thành pandas dataframe
        # Trả về 1 pandas dataframe

        return pd.json_normalize((asdict(business) for business in self.business_list), sep="_")
    def save_to_csv(self, filename):
        # Lưu pandas dataframe thành file csv
        self.dataframe().to_csv(f'{filename}.csv', index=True)
# Hàm crawl dữ liệu
# Input : 
# - data : thông tin cần tìm kiếm, ở đây bao gồm coffee, restaurant, billiards, sân bóng đá, ..
# - file : tên file csv để lưu data
# Output : 
# - Lưu trữ thông tin dữ liệu đã crawl được vào file csv
def main(data, file):
    # Danh sách các địa điểm cần access data để crawl
    list = ["Quận 1", "Quận 2", "Quận 3", "Quận 4", "Quận 5", "Quận 6", "Quận 7", "Quận 8", "Quận 9", "Quận 10", "Quận 11", "Quận 12", "Quận Bình Thạnh", "Quận Tân Bình", "Quận Phú Nhuận", "Quận Tân Phú", "Quận Gò Vấp", "Quận Bình Tân", "Tp. Thủ Đức", "Huyện Bình Chánh", "Huyện Nhà Bè", "Huyện Hóc Môn", "Huyện Củ Chi", "Huyện Cần Giờ"]
    total = 20 # Tổng số data cho mỗi thành phần trong list
    business_list = BusinessList() # Khởi tạo danh sách đối tượng business
    for item in list:
        search_for = data + " "+ item
        with sync_playwright() as p:
        
            browser = p.chromium.launch(headless=False) # Khởi tạo browser
            page = browser.new_page()
        
            page.goto('https://www.google.com/maps', timeout=60000)
            # Truy cập đến trang web
            page.wait_for_timeout(5000)
        
            page.locator('//*[@id="searchboxinput"]').fill(search_for) # Chọn vào button search, nhập input để bắt đầu tìm kiếm
            page.wait_for_timeout(3000)
        
            page.keyboard.press('Enter') # Press Enter
            page.wait_for_timeout(5000)
        
            # Cuộn dòng data 
            page.hover('(//div[@role="article"])[1]')

        # Thực hiện kiểm tra số lượng data trong 1 field, nếu số lượng data > total thì chỉ crawl total data, ngược lại nếu số lượng data < total thì crawl tất cả data đó
            previously_counted = 0
            while True:
                page.mouse.wheel(0, 10000)
                page.wait_for_timeout(3000)
            
                if page.locator('//div[@role="article"]').count() >= total:
                    listings = page.locator('//div[@role="article"]').all()[:total]
                    print(f'Total Scraped: {len(listings)}')
                    break
                else:
                # Đưa ra điều kiện thoát khỏi vòng lặp 
                    if page.locator('//div[@role="article"]').count() == previously_counted:
                        listings = page.locator('//div[@role="article"]').all()
                        print(f'Arrived at all available\nTotal Scraped: {len(listings)}')
                        break
                    else:
                        previously_counted = page.locator('//div[@role="article"]').count()
                        print(f'Currently Scraped: ', page.locator('//div[@role="article"]').count())
        
            
        
        # Scraping
            for listing in listings:
            
                listing.click()
                page.wait_for_timeout(5000)
                
                name_xpath = '//h1[contains(@class, "fontHeadlineLarge")]' # Khởi tạo xPath
                address_xpath = '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]' # Khởi tạo xPath
                website_xpath = '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]' # Khởi tạo xPath
                phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]' # Khởi tạo xPath
                reviews_span_xpath = '//span[@role="img"]' # Khởi tạo xPath
                    
                business = Business() # Khởi tạo object
                # Lấy dữ liệu, lưu vào object
                if page.locator(name_xpath).count() > 0:
                    business.name = page.locator(name_xpath).text_content()
                else:
                    business.name = ''
                if page.locator(address_xpath).count() > 0:
                    business.address = page.locator(address_xpath).text_content()
                else:
                    business.address = ''
                if page.locator(website_xpath).count() > 0:
                    business.website = page.locator(website_xpath).text_content()
                else:
                    business.website = ''
                if page.locator(phone_number_xpath).count() > 0:
                    business.phone_number = page.locator(phone_number_xpath).text_content()
                else:
                    business.phone_number = ''
                if listing.locator(reviews_span_xpath).count() > 0:
                    try:
                        business.reviews_average = float(listing.locator(reviews_span_xpath).get_attribute('aria-label').split()[0].replace(',','.').strip())
                        business.reviews_count = int(listing.locator(reviews_span_xpath).get_attribute('aria-label').split()[2].strip())
                    except:
                        business.reviews_average = ''
                        business.reviews_count = ''
                else:
                    business.reviews_average = ''
                    business.reviews_count = ''
                # Xử lý lưu trữ link các ảnh thành 1 list, ở đây mỗi địa điểm chỉ lưu trữ 2 ảnh
                a = []
                dem = 0
                all_images = page.query_selector_all('img') # Thẻ img
                for i, img in enumerate(all_images):
                    image_url = img.get_attribute("src")
                    try:
                        if image_url.startswith("https"):
                            sub_url = image_url[:image_url.index("=w")]      
                            if sub_url not in a:
                                a.append(sub_url)
                                dem += 1
                            else:
                                continue
                        else:
                            continue
                    except:
                        pass
                    if dem == 2:
                        break
                business.images = a
                business_list.business_list.append(business) # Append object vào list

        #Lưu vào file csv.
    business_list.save_to_csv(file)
    browser.close()
#Crawl dữ liệu của các địa điểm billiards, lưu vào file bida_data.csv
main("billiards", "bida_data")
# Ngoài ra, còn sử dụng để crawl dữ liệu của các địa điểm coffee, restaurant, sân bóng đá , .....