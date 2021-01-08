

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')#上面三行代码就是为了将Chrome不弹出界面，实现无界面爬取
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://tl.cyg.changyou.com/goods/selling?world_id=0&have_chosen=&page_num=2")
print(driver.page_source)
