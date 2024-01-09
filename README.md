## How to Use the PDF Splitter Script
<a href="https://github.com/toprogramm/pdf-splitter/tree/main">
  <img src="https://www.lukovskii.com/assets/imagehost/scissors.png" alt="logo" height="250">
</a>

## About: 
The PDF Splitter Script is a Python tool that simplifies the process of breaking down large PDF files into smaller groups of pages. Users can customize the splitting based on the number of pages per group, providing a user-friendly solution for managing and organizing PDF documents. The script includes error handling for smooth execution and is part of the PDF Splitter GitHub repository. Developed for personal use, users are encouraged to report issues for timely resolution.

### Prerequisites:
- **Python Installed:** Ensure you have Python installed on your system. You can download and install Python from the official [Python website](https://www.python.org/downloads/).


### Step 1: Download the Script
- **Download the Script:** Copy the provided Python script into a file named `splitter.py`.
- **Input PDF File:** Change filename to `input.pdf` and put it in the script directory.

### Step 2: Run the Script
- **Open Terminal/Command Prompt:**
  - On Windows, open Command Prompt.
  - On macOS and Linux, open Terminal.

- **Navigate to the Script Directory:**
  - Use the `cd` command to change your current directory to where the `splitter.py` file is located. For example:
    ```
    cd path/to/script-directory
    ```

- **Run the Script:**
  - Type the following command and press Enter to run the script:
    ```
    python splitter.py
    ```
  - The script will execute and prompt you for the required information.

### Step 3: Provide Input
- **Choose a Name for Output Files**
    ```
    Enter the desired name for saving the files (without  extension): 
    ```

- **Specify Number of Pages per Group**
    ```
    How many pages per group do you want to split? (Enter a number): 
    ```

- **Confirmation:**
  
  - If the total number of pages in the input PDF is not divisible by the specified number, you'll see a warning. Confirm by typing `yes`/`y` or `no`/`n` to proceed or cancel the operation.
  - - If you confirm an indivisible operation, your PDF file will be split with the remainder.


### Additional Notes:

- **Error Handling:**
  - The script includes error handling to ensure smooth execution. If there are any issues, the script will display appropriate messages.

# 😀 This script made for myself. You can report about issues and I fix it ASAIC (As Soon As I Can) 😀

<a href="https://www.freepik.com/free-vector/back-school-set-icons_4985031.htm#query=scissors&position=21&from_view=search&track=sph&uuid=fbde3ae1-402d-46d1-bd09-eaaad55b5990">Image by stockgiu</a> on Freepik
