
### BRIEF DESCRIPTION OF EACH FILE INFORMATION

`consult_letter.py`: This file creates the prompt for the API.
`openai_chat.py`: This file stores the API key and manages API requests.
`test_case.py`: This file is used for testing and debugging the code with various test examples.
`final_product_test.py`: This file generates the final product using a given example.
`output.txt`: This file contains the output, specifically the consultation email.
`requirements.txt`: This file lists all the required Python libraries.

### STEPS TO RUN MY IMPLEMENTATION

1. Install Python Libraries: Run `pip install -r requirements.txt` to install the required Python libraries.
2. Configure API Key: Open `openai_chat.py` and paste your OpenAPI key on line 4 as provided in Notion.
3. Navigate to Correct Directory: Open a terminal and ensure you are in the correct file directory.
4. Run Test Demo: In the terminal, run `python -m pytest consult_letter/final_product.py -s` to execute a test demo. 
   This will print the consultation email in the terminal and also save it to a text file named output.txt.

### REASONING FOR MY IMPLEMENTATION
    - For the prompt section in the `consult_letter.py`, I gave it a specific outline of an email to ensure 
      that each iteration the email will follow a specific format. 
    - Added `output.txt` for an easy way to view the email in a file and for copying and pasting.

