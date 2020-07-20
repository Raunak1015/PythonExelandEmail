import ExcelUtilityForDataDriven
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:/Users/computer/Downloads/driver/chromedriver_win32 (2)/chromedriver.exe")
driver.get("https://www.saucedemo.com/index.html")
driver.maximize_window()
path="D:/testData.xlsx"
rows=ExcelUtilityForDataDriven.getRowCount(path,'Sheet3')
for r in range(2,rows+1):
    UserName=ExcelUtilityForDataDriven.readData(path,"Sheet3",r,1)
    Password=ExcelUtilityForDataDriven.readData(path,"Sheet3",r,2)
    driver.find_element_by_xpath("//input[@id='user-name']").send_keys(UserName)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(Password)
    driver.find_element_by_xpath("//input[@id='login-button']").click()
    if driver.title=="Swag Labs":
        print("PASS")
        ExcelUtilityForDataDriven.writeData(path,"Sheet3",r,3,"PASS")
    else:
        print("FAIL")
        ExcelUtilityForDataDriven.writeData(path,"Sheet3",r,3,"FAIL")

    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//button[contains(text(),'Open Menu')]").click()
    driver.find_element_by_xpath("//a[@id='logout_sidebar_link']").click()
    driver.implicitly_wait(10)
