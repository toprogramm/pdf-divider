## How to Use the PDF Divider Script

### Prerequisites:
- **Python Installed:** Ensure you have Python installed on your system. You can download and install Python from the official [Python website](https://www.python.org/downloads/).


### Step 1: Download the Script
- **Download the Script:** Copy the provided Python script into a file named `divider.py`.
- **Input PDF File:** Change filename to `input.pdf` and put it in the script directory.

### Step 2: Run the Script
- **Open Terminal/Command Prompt:**
  - On Windows, open Command Prompt.
  - On macOS and Linux, open Terminal.

- **Navigate to the Script Directory:**
  - Use the `cd` command to change your current directory to where the `divider.py` file is located. For example:
    ```
    cd path/to/script-directory
    ```

- **Run the Script:**
  - Type the following command and press Enter to run the script:
    ```
    python divider.py
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

# :) This script made for myself. You can report about issues and I fix it ASAIC (As Soon As I Can) :)