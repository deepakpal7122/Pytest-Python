import pytest
from Page_Object_Model.addToCartWithoutLogin import AddToCartWithoutLogin
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.addToCartWithLogin import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time

# ************** Working code ************************

class Test_003_AddToCartWithLogin:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    Logger = LogGen.loggen()
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_addToCartWithLogin(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        # using WithoutLogin addtocart test data
        self.addcartwithoutogin = AddToCartWithoutLogin(self.driver)
        self.addcartwithoutogin.clickOilDefCoolant()   
        time.sleep(5)
        self.addcartwithoutogin.clickselectpart()
        self.addcartwithoutogin.clickAddToCartButton()
        self.addcartwithoutogin.clickIconCart()
        self.addcartwithoutogin.clickViewCartButton()
        self.addcartwithoutogin.clickNextButton()


        # using login page test data
        self.lp = LoginPage(self.driver)
        '''self.lp.clickPasswordRadioButton()
        self.lp.setModileNumber(self.mobilenumber)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()'''
        time.sleep(35)
        
        # using login Addtocart data
        self.addcart = AddToCart(self.driver)
        self.addcart.clickWelcomeAccountPopup()
        time.sleep(3)
        # using WithoutLogin addtocart test data
        self.addcartwithoutogin = AddToCartWithoutLogin(self.driver)
        self.addcartwithoutogin.clickIconCart()
        self.addcartwithoutogin.clickViewCartButton()
        self.addcartwithoutogin.clickNextButton()
        time.sleep(5)
        
        # using login Addtocart data
        self.addcart = AddToCart(self.driver)
        self.addcart.scrollPage()
        time.sleep(3)

        self.addcart.clickProceedToPaymentButton()
        time.sleep(3)
        self.addcart.scrollPlaceOrderPage()
        time.sleep(3)
        self.addcart.clickCheckBox()
        time.sleep(3)
        self.addcart.clickPlaceOrderButton()
        self.addcart.clickOrdersNotConfirmed()
        self.addcart.clickOrderHistory()
              
        self.driver.quit()
        
        