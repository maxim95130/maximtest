import time
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_open_page_s6( browser ):
    homePage = HomePage( browser )
    homePage.open()
    homePage.clickOnGalaxyS6()

    productPage = ProductPage( browser )
    productPage.checkTitleSamsungS6( 'Samsung galaxy s6' )


def test_find_monitor( browser ):
    homePage = HomePage( browser )
    homePage.open()  
    homePage.clickMonitor()
    time.sleep( 2 )
    productPage = ProductPage( browser )
    productPage.checkProductCount( 2 )