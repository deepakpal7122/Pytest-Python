from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddToCart:
    welcome_popup_xpath = "//button[text() = 'OK']"
    button_proceedtopayment_xpath = "//button[text() = 'PROCEED TO PAYMENT']"
    checkbox_click_xpath = "//input[@type='checkbox']"
    button_placeorder_xpath = "//button[text() = 'Place Order']"
    linktext_ordernotconfirmed_xpath ="//a[text() = 'Orders Not Confirmed']"
    module_orderhistory_xpath ="//a[text() = 'Order History ']"    
    
        
    def __init__(self, driver):
        self.driver = driver
        
    def clickWelcomeAccountPopup(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.welcome_popup_xpath))).click()
   
    def clickProceedToPaymentButton(self):
        # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable)((By.XPATH, self.button_proceedtopayment_xpath))
        # element.click()
        self.driver.find_element(By.XPATH, self.button_proceedtopayment_xpath).click()
    
    def clickCheckBox(self):
        self.driver.find_element(By.XPATH, self.checkbox_click_xpath).click()
    
    def clickPlaceOrderButton(self):
        self.driver.find_element(By.XPATH, self.button_placeorder_xpath).click()
    
    def clickOrdersNotConfirmed(self):
        self.driver.find_element(By.XPATH, self.linktext_ordernotconfirmed_xpath).click()
    
    def clickOrderHistory(self):
        self.driver.find_element(By.XPATH, self.module_orderhistory_xpath).click()
        
    