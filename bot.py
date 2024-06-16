from bs4 import BeautifulSoup
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

import re

total_question_attempted = 0
success = 0

def goToNextQs() -> None:
    # Find the rightmost element using XPath
    rightmost_element = driver.find_element(By.XPATH, "//div[@class='lc-md:flex group flex items-center overflow-hidden rounded hover:bg-fill-tertiary dark:hover:bg-fill-tertiary']/a[last()]")

    # Click on the rightmost element
    rightmost_element.click()


    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='settings']"))
    )
    actions = ActionChains(driver)

    actions.move_to_element(button)

    actions.move_by_offset(50, 0)

    actions.click().perform()

    sleep(5)

def getCode(input_text):
    braces = 1
    detect_text_first = """class Solution {
class Solution {
public:
public:"""
    detect_first = input_text.index(detect_text_first) + len(detect_text_first)
    res = ""
    toggle = 1
    for i in input_text[detect_first::].lstrip('\n'):
        if braces == 0:
            break
        if i == "{":
            braces += 1
        if i == "}":
            braces -= 1
        if toggle == 1:
            res += i
        if i == '\n':
            toggle = -toggle

    res = """class Solution {
public:
""" + res + ';'
    filtered_cpp_code = filter_cpp_code(res)
    return filtered_cpp_code

def filter_cpp_code(text):
    # Define the regular expression pattern to match C++ code blocks
    pattern = r'class Solution {[\s\S]*?};'
    
    # Use re.findall to find all matches of the pattern in the text
    cpp_code_blocks = re.findall(pattern, text)
    
    # Join the matched code blocks into a single string
    cpp_code = '\n'.join(cpp_code_blocks)
    
    return cpp_code

# Going Headless, To Be Done
chrome_options = Options()
chrome_options.add_argument("--headless")  # For Chrome versions below 109
chrome_options.add_argument("--headless=new")  # For Chrome versions 109 and above (recommended)


# driver = webdriver.Edge()
driver = webdriver.Edge()
driver.get("https://leetcode.com/")

# Wait for the sign-in button to be clickable
signInButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/accounts/login/']"))
)
signInButton.click()

sleep(10)

# Wait for email input to be clickable and enter email
emailInput = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "id_login"))
)
emailInput.send_keys("aura.2758.08@gmail.com")

# Wait for password input to be clickable and enter password
passwordInput = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "id_password"))
)
passwordInput.send_keys("15081947gG29082004")

# Wait for login button to be clickable and click on it
logInButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-content-container__2HVS"))
)
logInButton.click()

sleep(5)


# Click on the element to open the new tab
goToPOTD = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "headlessui-popover-button-3"))
)
goToPOTD.click()

# Wait for the new window or tab to open
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))


# Switch to the new tab
for handle in driver.window_handles:
    if handle != driver.current_window_handle:
        driver.switch_to.window(handle)
        break

sleep(5)

while True:
    total_question_attempted += 1
    goToNextQs()

    try:
        goToAns = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "solutions_tab"))
        )
        goToAns.click()
        sleep(5)
    except:
        # Perform some action (e.g., pressing Alt + Left Arrow) REDO
        webdriver.ActionChains(driver).key_down(Keys.ALT).send_keys(Keys.ARROW_LEFT).key_up(Keys.ALT).perform()
        sleep(5)
        webdriver.ActionChains(driver).key_down(Keys.ALT).send_keys(Keys.ARROW_LEFT).key_up(Keys.ALT).perform()
        continue


    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search...']"))
    )
    search.send_keys("C++")
    sleep(3)

    # Select the 1st ans
    url = driver.current_url
    url = url.removeprefix("https://leetcode.com")

    try:
        firstAns = driver.find_element(By.XPATH, f"//a[contains(@href,'{url}')]")
        firstAns.click()
        sleep(2)
    except:
        continue


    # Get the answer

    spanElements = driver.find_elements(By.TAG_NAME, "span")
    html_content = ""
    for span in spanElements:
        html_content += span.get_attribute("outerHTML")


    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the plain text from the code element
    plain_text_code = soup.get_text()

    # Extract C++ Code from the text

    try:
        res = getCode(plain_text_code)

        filtered_cpp_code = filter_cpp_code(res)
        # # Copy the code into the clipboard
        pyperclip.copy(filtered_cpp_code)
        sleep(3)

        # Enter the filtered_cpp_code into the text editor
        auto_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Auto')]"))
        )

        actions = ActionChains(driver)

        # Move the mouse to the element
        actions.move_to_element(auto_button)

        # Move the mouse down by 100 pixels (adjust as needed)
        actions.move_by_offset(0, 100)

        # Perform the click
        actions.click().perform()

        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        sleep(2)
        # Copy the code into the clipboard
        # print(filtered_cpp_code)
        # pyperclip.copy(filtered_cpp_code)
        # sleep(3)
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        sleep(2)

        # Simulate pressing Ctrl + ', needed to submit the solution
        # webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("'").key_up(Keys.CONTROL).perform()

        # Simulate pressing Ctrl + Enter
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        success += 1
        sleep(5)
    except:
        continue
    # show result
    print("Total Qs Attempted: ", total_question_attempted)
    print("No. of Success: ", success)
    print('\n')
    