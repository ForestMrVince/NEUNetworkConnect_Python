from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

url = r"https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_portal_sso%3Fac_id%3D1"
# 用户名密码
stu_number = '2188888'
stu_pass = 'goodjob8888'

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

elem = driver.find_element_by_name('un')
elem.send_keys(stu_number)

elem = driver.find_element_by_name('pd')
elem.send_keys(stu_pass)

driver.find_element('id', 'index_login_btn').click()

driver.quit()


"""
东北大学校园网联网代码
"""
