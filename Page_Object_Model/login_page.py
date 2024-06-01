from selenium.webdriver.common.by import By

class LoginPage:
    login_button_icon_xpath = "//img[@tabindex='0']"
    radio_button_password_id= "Password"
    textbox_mobile_number_xpath = "//input[@placeholder='Enter mobile number']"
    texbox_password_xpath = "//input[@formcontrolname='password']"
    button_signin_xpath = "//button[text() = 'Sign in']"

    def __init__(self, driver):
        self.driver = driver
        
    def clickloginIconButton(self):
        self.driver.find_element(By.XPATH, self.login_button_icon_xpath).click()
        
    def clickPasswordRadioButton(self):
        self.driver.find_element(By.ID, self.radio_button_password_id).click()
        
    def setModileNumber(self, mobilenumber):
        self.driver.find_element(By.XPATH, self.textbox_mobile_number_xpath).send_keys(mobilenumber)
        
    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.texbox_password_xpath).send_keys(password)
        
    def clickSignIn(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()
        