from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

prod = input('Enter product name which you want to buy: ')
email = input('Enter your email: ')
password = input('Enter your password: ')

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.amazon.in')
browser.maximize_window()
wait = WebDriverWait(browser, 120)

hover_element = browser.find_element(By.ID, "nav-link-accountList")  
actions = ActionChains(browser)
actions.move_to_element(hover_element).perform()

dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, "nav-link-accountList")))  

signIn = dropdown_element.find_element(By.XPATH, "//span[@class='nav-action-inner'][contains(text(), 'Sign in')]")  
signIn.click()

email_input = browser.find_element(By.ID, "ap_email")  
continue_button = browser.find_element(By.ID, "continue")  
email_input.send_keys(email)  
continue_button.click()

pass_input = browser.find_element(By.ID, "ap_password")  
signin_button = browser.find_element(By.ID, "signInSubmit")  
pass_input.send_keys(password)  
signin_button.click()

input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
search_button = browser.find_element(By.XPATH, "(//input[@type='submit'])[1]")

input_search.send_keys(prod)
search_button.click()

elements_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']"))) 
print(len(elements_list))

if elements_list:
    first_element = elements_list[0]
    first_element.click()
else:
    print(f'{prod} not available')

main_window_handle = browser.current_window_handle
new_window_handle = None

for handle in browser.window_handles:
    if handle != main_window_handle:
        new_window_handle = handle
        break

if new_window_handle:
    browser.switch_to.window(new_window_handle)
    
buyNow_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='buy-now-button'])")))
buyNow_button.click()

addr_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='a-button-input'])")))  
addr_button.click()

order_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@name='placeYourOrder1'])")))
order_button.click()

browser.quit()