from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

caption = ('''This post was shared using a bot that I learnt to create from Python Bootcamp 2020 held by DSC@DSU. #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot''')
share_text_box_EC = ('<textarea class="sharerTextAreaArea mentions-input" name="comment" rows="3" id="share_msg_input" data-sigil="sharer-textarea m-textarea-input"></textarea>')

def start():
    global driver

    driver = webdriver.Chrome()
    driver.get("https://m.facebook.com")

def login(user_email,user_password):

    email = driver.find_element_by_id("m_login_email")
    password = driver.find_element_by_css_selector("input[name='pass']")
    login_btn = driver.find_element_by_name("login")

    email.send_keys(user_email)
    password.send_keys(user_password)
    login_btn.click()


def load_fb_post(url):

    driver.get(url)
    print("\nPost loaded")

def like_post():

    like_btn = driver.find_element_by_css_selector("div[data-sigil='ufi-inline-actions'] div a")
    like_btn.click()

    print("\nLiked")
    sleep(.8)


#Forgot to complete and include xD

def cmnt_on_post():
    # Not completed
    cmnt_box = driver.find_element_by_id("composerInput")
    cmnt_post_btn = driver.find_element_by_name("submit")


def share_post():

    share_btn = driver.find_element_by_css_selector("div[data-sigil='ufi-inline-actions'] div a[data-sigil='share-popup']")
    write_post_btn = driver.find_element_by_id("share-with-message-button")

    share_btn.click()
    print("\nShare button clicked")
    sleep(.8)

    write_post_btn.click()
    print("\nWrite post clicked")


def add_caption():
    
    while True:
        caption_text_area = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR ,'div[data-sigil="marea"] div textarea')))
        
        if caption_text_area.get_attribute("outerHTML") != share_text_box_EC:
            break

    print(caption_text_area.get_attribute("outerHTML"))
    caption_text_area.send_keys(caption)

    print("\nCaption added")

def click_post():

    post_btn = driver.find_element_by_id("share_submit")
    post_btn.click()

    print("\nPosted")


def main():

    start()
    
    email = input("Enter your email:")
    password = getpass("Enter your password:")

    login(email, password)
    print("\nLogged in")

    url = input("\nEnter the post link:")

    load_fb_post(url)
    

    like_post()

    share_post()    

    add_caption()

    click_post()

    input("Press ENTER to exit.")
    


if __name__ == "__main__":
    main()