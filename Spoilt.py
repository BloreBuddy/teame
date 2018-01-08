import requests
import sys
import json
from splinter import Browser
import selenium

datame = {
  'message': 'Urgent! I need some help.',
  'level': 5,
  'secret': '35926afd4ca93c229ba6201805031273'
}


browser = Browser('phantomjs', user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3187.0 Safari/537.36')
#browser = Browser('chrome', headless = True)

# browser.visit('https://google.co.in')
# browser.fill('q', 'splinter - python acceptance testing for web applications')
# browser.find_by_name('btnK').click()
#
# if browser.is_text_present('splinter.readthedocs.io'):
#     print ("Yes, the official website was found!")
# else:
#     print ("No, it wasn't found... We need to improve our SEO techniques")

browser.visit('http://casualtalk.chatovod.com/')
button = browser.find_by_value("Enter chat")
button.click()


if browser.is_text_present('Choose your nick:'):
        print ("Yes, the official website was found!")
        iconfb = browser.find_by_css("#loginForm > p.social.alignCenter > a:nth-child(7)").first
        #browser.is_element_present_by_id(iconfb)
        iconfb.click()
        browser.windows.current = browser.windows[1]
        #browser.visit('http://noki.chatovod.com/widget/login?n=fb')
        browser.fill('email', 'chatmod@gmail.com')
        browser.fill('pass', 'memod')
        button1 = browser.find_by_name("login")
        button1.click()
        print('attempted')
        browser.windows.current = browser.windows[0]
        browser.reload()
        # if browser.is_text_present('Vijay..'):
        #      print ("YazzAgain!")
        p=0
        while(1):
            element_list = browser.find_by_xpath("(//div[@class='chatMessage ts'])[last()]//span[@class='minor']")
            try:
                while(element_list.is_empty() or (element_list.first.text.upper().replace('REH','') != 'ANA.. HAS JOINED THIS ROOM')):
                        element_list = browser.find_by_xpath("(//div[@class='chatMessage ts'])[last()]//span[@class='minor']")
                        p=0
                    # browser.find_by_xpath("(//div[@class='chatMessage ts'])[last()]//a[@data-nick='Vijay']")
                else:

                    if (p==0 or p==1):
                        p=p+1
                    if(p==1):
                        print(element_list.first.text)
                        element = browser.find_by_xpath("(//div[@class='chatMessage ts'])[last()]//span[@class='time']").first
                        strr = element['title']
                        print(strr)
                        resp = requests.post('https://api.pushjet.io/message', data=datame).json()
                        resp = requests.post('https://api.pushjet.io/message', data=datame).json()
                        resp = requests.post('https://api.pushjet.io/message', data=datame).json()
            except selenium.common.exceptions.StaleElementReferenceException as e:
                e = sys.exc_info()[0]
                print(e)

            except json.decoder.JSONDecodeError as ee:
                ee = sys.exc_info()[0]
                print(ee)

print("End")
browser.quit()