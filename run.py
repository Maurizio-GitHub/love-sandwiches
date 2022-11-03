# The file name, 'run.py', must not be changed.
# The command 'pip3 install gspread google-auth' has been executed in the terminal to leverage 'google-auth'.

import gspread
from google.oauth2.service_account import Credentials

# The variables whose value is never going to change (SCOPE, CREDS, SCOPED_CREDS, GSPREAD_CLIENT, SHEET) are written in capital letters.
# In Python, this is a best practice to flag constants (i.e. variables that should not be changed) to other developers.
# Every Google account has an IAM (Identity and Access Management) configuration. SCOPE lists the APIs that the program should access in order to run:

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# The JSON file with the credentials generated through GCP (Google Cloud Platform), 'creds.json', has been imported here.
# CREDS is assigned by passing 'creds.json' as a parameter of the 'from_service_account_file()' method of the 'Credentials' class:

CREDS = Credentials.from_service_account_file('creds.json')

# SCOPED_CREDS is assigned by passing the SCOPE variable as a parameter of the 'with_scopes()' method of the CREDS object:

SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# GSPREAD_CLIENT is assigned by passing the SCOPED_CREDS variable as a parameter of the 'gspread.authorize()' method:

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# SHEET provides access to the 'love_sandwiches' spreadsheet and is assigned by passing the file name as a parameter of the 'open()' method of the GSPREAD_CLIENT object:

SHEET = GSPREAD_CLIENT.open('love_sandwiches')


# Function to collect sales data from users:

def get_sales_data():
    """
    It gets sales figures input from the user
    """
    while True:
        print('Please, enter sales data from the last market.')
        print('Data should be six numbers, separated by commas.')
        print('Example: 10, 20, 30, 40, 50, 60\n')

        # The user is prompted with a call to action:

        data_string = input('Enter data here: ')

        # The 'split()' method returns the broken up values as a list, removing the specified punctuation (comma) used to enter data:

        sales_data = data_string.split(',')

        # The validation function is called, by passing it the list containing the sales data.
        # If the function returns 'True' (no errors found), the while-loop breaks; otherwise, the user is prompted again with the same call to action:

        if validate_data(sales_data):
            print('Valid data entered; thank you.')
            break

    # Upon successful validation, the sales data list is returned:

    return sales_data


# Function validating user data entries; it accepts a parameter representing the sales data list:

def validate_data(values):
    """
    It tries to convert the provided string values into integers and raises ValueError if:
    - the strings cannot be converted into integers;
    - there are not exactly six values (length of the provided list not equal to 6);
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f'Exactly 6 values are required; {len(values)} entered instead')

    # The ValueError class contains the details of the error triggered in the try-block.
    # The 'as' keyword allows for the assignement of the ValueError object to the 'e' variable, which is standard Python shorthand for 'error':

    except ValueError as e:
        print(f'Invalid data: {e}; please, try again.\n')
        return False

    # These boolean return values (in the following and above) serve as a stopping condition for the while-loop within 'get_sales_data()' function:

    return True


# The following variable contains the correct sales data returned by 'get_sales_data()' function upon validation:

data = get_sales_data()