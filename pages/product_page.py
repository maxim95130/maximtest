from selenium.webdriver.common.by import By

class ProductPage():

    def __init__(self, browser ):


    def checkTitleSamsungS6( self, title ):
        title_page = self.browser.find_element( By.XPATH, '//*[@class="name" and contains(text(),"Samsung galaxy s6")]' )
        assert title_page == title


    def checkProductCount( self, count ):
        monitors = self.browser.find_elements( By.CSS_SELECTOR, '.card')
        assert len( monitors ) == count