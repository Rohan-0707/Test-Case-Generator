```markdown
# Test Case Generator with LLaMA 2

This Streamlit application leverages the power of the LLaMA 2 language model to automate the creation of detailed and comprehensive test cases for various software applications.

## Features

* **Intelligent Generation:** Utilizes LLaMA 2's natural language processing capabilities to generate relevant test cases based on your input.
* **Customizable:**  Control the number of test cases generated to fit your specific needs.
* **Versatile:** Supports test case creation for Android applications, websites, software programs, and web applications.
* **User-Friendly:** Features a simple and intuitive Streamlit interface for inputting the topic and platform of your application.
```

## How to Use

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rohan-0707/Test-Case-Generator.git
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate       # For Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Download the LLaMA 2 Model:**
   * Download the `llama-2-7b-chat.ggmlv3.q8_0.bin` model (or a smaller, quantized version) from the official source.
   * Place it in the `models` directory within your project.

### Usage

1. **Run the App:**
   ```bash
   streamlit run app.py
   ```

2. **Enter Topic:**
   * Type a description of the feature or functionality you want to test (e.g., "login process," "shopping cart checkout").

3. **Select Number of Test Cases:**
   * Use the number input to specify how many test cases you want to generate.

4. **Choose Platform:**
   * Select the type of application you're testing from the dropdown menu.

5. **Generate Test Cases:**
   * Click the "Generate Test Cases" button.
   * The app will generate test cases with IDs, descriptions, preconditions, input data, steps, expected outputs, and placeholders for actual outputs and statuses.

## Example Output

```
Here's what you might get as output after running this code (assuming topic = "login page", count = "2", and platform = "website"):

Test Case ID: TC_LP_01
Preconditions:
    - The user is on the website's homepage.
    - The login page is accessible.
Input Data:
    - Valid username and password.
Steps to be Executed:
    1. Click on the "Login" button.
    2. Enter the valid username and password.
    3. Click on the "Submit" button.
Expected Output:
    - The user should be successfully logged in and redirected to their account page.
Actual Output:
    - The user is successfully logged in and redirected to their account page.
Remark: Pass

Test Case ID: TC_LP_02
Preconditions:
    - The user is on the website's homepage.
    - The login page is accessible.
Input Data:
    - Invalid username and password.
Steps to be Executed:
    1. Click on the "Login" button.
    2. Enter the invalid username and password.
    3. Click on the "Submit" button.
Expected Output:
    - An error message should be displayed indicating invalid credentials.
Actual Output:
    - An error message is displayed indicating invalid credentials.
Remark: Pass
```

## Technologies Used

* Python
* Streamlit
* LangChain
* LLaMA 2

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

**Additional Notes:**

* **Model Availability:** Make sure you have the necessary permissions and resources to download and use the LLaMA 2 model.
* **Customization:** The prompt can be further tailored to generate test cases that are more specific to your needs.
* **Feedback:** Consider asking users for feedback to help you improve the app!

Let me know if you'd like any adjustments or further details in the README!
