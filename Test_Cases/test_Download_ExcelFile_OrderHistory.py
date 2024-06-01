import pytest
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.setPassword import SetPassword
from Page_Object_Model.download_ExcelFile_OrderHistory import DownloadExcelFile
from Page_Object_Model.addToCart import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time


class Test_004_BulkUplaod:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    def test_BulkUpload(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.lp = LoginPage(self.driver)
        self.lp.clickloginIconButton()
        self.lp.clickPasswordRadioButton()
        self.lp.setModileNumber(self.mobilenumber)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        time.sleep(2)
        
        self.setpwd = SetPassword(self.driver)
        self.setpwd.click_HeaderMenu_Mydashboard()
        
        self.dwnexcel = DownloadExcelFile(self.driver)
        self.dwnexcel.click_Order()
        self.dwnexcel.click_History()
        self.dwnexcel.click_ExcelFile()
        
        
        