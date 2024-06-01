import pytest
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.setPassword import SetPassword
from Page_Object_Model.bulkUpload import BulkUpload
from Page_Object_Model.addToCartWithLogin import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time


class Test_007_SetPassword:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_SetPassword(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.lp = LoginPage(self.driver)
        self.lp.clickloginIconButton()
        '''self.lp.clickPasswordRadioButton()
        self.lp.setModileNumber(self.mobilenumber)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()'''
        time.sleep(25)
        # time.sleep(5)
        
        self.addcart = AddToCart(self.driver)
        self.addcart.clickWelcomeAccountPopup()
        
        self.bulkup = BulkUpload(self.driver)
        self.bulkup.clickMyDashboard()
        
        self.setpwd = SetPassword(self.driver)
        self.setpwd.click_HeaderMenu_SetPassword()
        self.setpwd.click_Button_Request_OTP()
        time.sleep(25)
        self.setpwd.enter_OTP()
        self.setpwd.enter_Password()
        self.setpwd.enter_Confirm_Password()
        self.setpwd.click_Button_Save()
        
        time.sleep(10)
        self.driver.quit()