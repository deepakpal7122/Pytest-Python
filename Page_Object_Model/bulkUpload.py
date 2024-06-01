from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BulkUpload:
    upload_button_xpath = "//mat-icon[text() = 'file_upload']"
    headermenu_mydashboard_xpath = "(//span[text() = ' MY DASHBOARD '])[1]"
    headermenu_bulkorderupload_xpath = "//a[text() = 'Bulk Order Upload ']"
    bulkUpload_button_xpath = "//button[text() = 'Bulk Order Upload']"
    sumit_button_xpath = "//button[text() = 'Submit']"
    

    def __init__(self, driver):
        self.driver = driver
        
    def clickMyDashboard(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.headermenu_mydashboard_xpath))).click()

    def clickBulkOrderUpload(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.headermenu_bulkorderupload_xpath))).click()

    def clickBulkUpload(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.bulkUpload_button_xpath))).click()
    
    def uploadBulkFile(self):
        self.driver.find_element(By.XPATH, self.upload_button_xpath).send_keys("C:/Users/RADHE/Downloads/Deepak.xlsx")
    
    def clickSumbitButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sumit_button_xpath))).click()
        