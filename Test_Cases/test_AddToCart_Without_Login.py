import pytest
from Page_Object_Model.addToCartWithoutLogin import AddToCartWithoutLogin
from Utilities.readProperties import ReadConfig
import time

# ************** Working code ************************

class Test_002_AddToCartWithoutLogin:
    baseURL = ReadConfig.getApplicationURL()
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_addToCartWithoutLogin(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.addcart = AddToCartWithoutLogin(self.driver)
            self.addcart.clickOilDefCoolant()   
            time.sleep(5)
            self.addcart.clickselectpart()
            self.addcart.clickAddToCartButton()
            self.addcart.clickIconCart()
            self.addcart.clickViewCartButton()
            self.addcart.clickNextButton()

            self.driver.quit()
            
        finally:
            try:
                self.driver.save_screenshot(".\\Screenshots\\" + "Add_To_Cart_without_Login.png")
            except Exception as e:
                print(f"failed to the screenshot: {e}")
        