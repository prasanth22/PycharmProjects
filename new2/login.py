from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/AddSession/identifier?hl=en&continue=https%3A%2F%2Fwww.google.co.in%2F&flowName=GlifWebSignIn&flowEntry=AddSession')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('not_my_real_email@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()