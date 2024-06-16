# LeetCode Automation Script

This script automates the process of attempting LeetCode questions and submitting solutions using Selenium WebDriver, BeautifulSoup for HTML parsing, and other Python libraries. It navigates through questions, extracts code, and submits answers, aiming to improve efficiency in solving LeetCode problems.

## Prerequisites

To run this script, you need to have the following installed:

1. Python 3.x
2. Selenium WebDriver
3. BeautifulSoup4
4. pyperclip
5. Edge WebDriver

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-repo/leetcode-automation.git
   cd leetcode-automation
   ```

2. **Install Required Packages:**
   ```sh
   pip install selenium beautifulsoup4 pyperclip
   ```

3. **Download Edge WebDriver:**
   - Download the version that matches your Edge browser from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
   - Make sure the WebDriver executable is in your system's PATH.

## Configuration

1. **Update Login Credentials:**
   - Open the script and replace the placeholders `"Email"` and `"Password"` with your LeetCode login credentials.

2. **Modify Chrome Options (Optional):**
   - The script is configured to run Edge WebDriver. If you want to run it headlessly or use a different browser, adjust the `chrome_options` section accordingly.

## Script Overview

### Main Functions

- **goToNextQs()**
  - Navigates to the next question.
  - Clicks on the rightmost element to move to the next question.
  - Opens settings using an action chain to ensure the correct area is clicked.

- **getCode(input_text)**
  - Extracts and formats C++ code from the provided input text.
  - Filters out unnecessary parts and ensures proper code structure.

- **filter_cpp_code(text)**
  - Uses regex to identify and return valid C++ code blocks from the text.

### Workflow

1. **Login to LeetCode:**
   - The script navigates to the LeetCode login page and logs in using provided credentials.

2. **Navigate to Problem of the Day (POTD):**
   - After logging in, the script opens the Problem of the Day in a new tab.

3. **Attempt Questions:**
   - Continuously navigates through questions, extracts the solution code, and submits it.
   - If a question cannot be accessed or answered, it retries by navigating back.

4. **Submit Answers:**
   - Copies the extracted code to the clipboard.
   - Pastes and submits the code in the LeetCode editor.
   - Tracks the total number of questions attempted and successful submissions.

## Usage

1. **Run the Script:**
   - Ensure your WebDriver is set up and accessible.
   - Execute the script:
     ```sh
     python leetcode_automation.py
     ```
   - The script will log in, navigate to questions, and start attempting them automatically.

2. **Monitor Output:**
   - The console will display the total number of questions attempted and the number of successful submissions.

## Notes

- **Error Handling:**
  - The script includes basic error handling to retry questions if they fail initially.
  
- **Clipboard Usage:**
  - `pyperclip` is used to copy the extracted code to the clipboard before pasting it into the LeetCode editor.

- **Adjustments:**
  - You can adjust sleep intervals and other parameters to match your system's performance and internet speed.

## Disclaimer

- **Account Safety:**
  - Use this script responsibly. Automating login and submission processes may violate LeetCode's terms of service.
  - Consider testing with a secondary account to avoid potential issues.

## Contributions

- Feel free to contribute to this project by opening issues or submitting pull requests.

---

By automating repetitive tasks, this script helps users efficiently navigate and solve LeetCode problems. Happy coding!
