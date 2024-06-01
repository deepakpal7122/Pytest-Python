import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_Object_Model.addToCartWithoutLogin import AddToCartWithoutLogin
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.addToCart import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time

class Test_002_AddToCart:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    Logger = LogGen.loggen()
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_addToCart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        # using WithoutLogin addtocart test data
        self.addcartwithoutogin = AddToCartWithoutLogin(self.driver)
        self.addcartwithoutogin.clickOilDefCoolant()   
        time.sleep(3)
        self.addcartwithoutogin.clickselectpart()
        self.addcartwithoutogin.clickAddToCartButton()
        self.addcartwithoutogin.clickIconCart()
        self.addcartwithoutogin.clickViewCartButton()
        self.addcartwithoutogin.clickNextButton()

        # using login page test data
        self.lp = LoginPage(self.driver)
        self.lp.clickPasswordRadioButton()
        self.lp.setModileNumber(self.mobilenumber)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()

        # using login Addtocart data
        self.addcart = AddToCart(self.driver)
        self.addcart.clickWelcomeAccountPopup()


        self.addcartwithoutogin = AddToCartWithoutLogin(self.driver)
        self.addcartwithoutogin.clickIconCart()
        self.addcartwithoutogin.clickViewCartButton()
        self.addcartwithoutogin.clickNextButton()

        self.addcart.clickProceedToPaymentButton()
        self.addcart.clickCheckBox()
        time.sleep(5)
        self.addcart.clickPlaceOrderButton()
        self.addcart.clickOrdersNotConfirmed()
        self.addcart.clickOrderHistory()
        
        