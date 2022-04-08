from importlib.resources import path
from multiprocessing.sharedctypes import Value
from RPA.Browser.Selenium import Selenium
from RPA.Archive import Archive
from RPA.HTTP import HTTP
from RPA.Desktop.Windows import Windows
import os

browser = Selenium(auto_close=False)
r = HTTP()
archive = Archive()
lib = Windows()

def download_file():
    r.download(url='https://botsdna.com/BGV/Employee%20Documents.zip', target_file="output/", overwrite=True)

def unzip_files():
    archive.extract_archive(archive_name="output/Employee%20Documents.zip",path="output/")

def create_zip():
    dirs = './output/Employee Documents'
    for name in os.listdir(dirs):
        if os.path.isdir(os.path.join(dirs, name)):
            print(name)
            archive.archive_folder_with_zip(folder=dirs+"/"+name, archive_name=dirs+"/"+name+".zip",recursive=True)
            # break
def open_site():
    browser.open_chrome_browser(url="https://botsdna.com/BGV/")
    browser.wait_until_element_is_visible(locator='//*[@id="CurrentEmpID"]')

def close_browser():
    browser.close_browser()

def take_screenshot():
    from datetime import datetime
    now = datetime.now()
    browser.screenshot(filename="output/sc/sc.png")

def upload_docs():
    # browser.open_chrome_browser(url="https://botsdna.com/BGV/")
    # browser.wait_until_element_is_visible(locator='//*[@id="CurrentEmpID"]')
    emp_id = browser.get_element_attribute(locator='//*[@id="CurrentEmpID"]', attribute="value")
    browser.wait_until_element_is_visible(locator='//*[@id="uploadedFile"]')
    browser.click_element(locator='//*[@id="dataEntry"]/table/tbody/tr[4]/td[2]')
    # browser.click_element(locator='//*[@id="uploadedFile"]')
    cwd = "d:\\robocorp\\output\\Employee{SPACE}Documents\\"
    lib.send_keys(keys='d:')

    
    # lib.send_keys_to_input(keys_to_type=cwd+emp_id+".zip",with_enter=True)
    lib.send_keys(keys=cwd+emp_id+".zip")
    lib.send_keys('{ENTER}')
    browser.click_button(locator='//*[@id="Submit"]')
    print('upload complete')
    

def background_check():
    import glob
    dirs = glob.glob("output/Employee Documents/*.zip")
    
    for i in range(11):
        upload_docs()
        print(i)
    
def main():
    try:
        download_file()
        unzip_files()
        create_zip()
        open_site()
        background_check()
        take_screenshot()
    except:
        take_screenshot()
        pass
    finally:
        take_screenshot()
        close_browser()


if __name__ == "__main__":
    main()