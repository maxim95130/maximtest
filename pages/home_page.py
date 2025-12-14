from selenium.webdriver.common.by import By

class HomePage:

    def __init__( self, browser ):
        self.browser = browser

    def openPage( self ):
        self.browser.get( 'https://demoblaze.com/index.html' )


    def clickOnGalaxyS6( self ):
        galaxy_s6_name = self.broweser.find_element( By.XPATH, '//*[@class="hrefch" and contains(text(),"galaxy s6")]' )
        galaxy_s6_name.click()

    def clickMonitor( self ):
        monitor_link = self.browser.find_element( By.CSS_SELECTOR, '''[onclick="ByCat('monitor')"]''' )
        monitor_link.click()
    