import pytest
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.bulkUpload import BulkUpload
from Page_Object_Model.addToCartWithoutLogin import AddToCartWithoutLogin
from Page_Object_Model.addToCartWithLogin import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time


class Test_004_BulkUplaod:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_BulkUpload(self, setup):
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
        time.sleep(5)
        
        self.addcart = AddToCart(self.driver)
        self.addcart.clickWelcomeAccountPopup()
        
        self.bulkup = BulkUpload(self.driver)
        self.bulkup.clickMyDashboard()
        self.bulkup.clickBulkOrderUpload()
        # self.bulkup.clickBulkUpload()
        self.bulkup.uploadBulkFile()
        self.bulkup.clickSumbitButton()