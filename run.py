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
# CREDS is assigned by passing 'creds.json' as a parameter of the 'from_service_account_file' method of the 'Credentials' class:

CREDS = Credentials.from_service_account_file('creds.json')

# SCOPED_CREDS is assigned by passing the SCOPE variable as a parameter of the 'with_scopes' method of the CREDS object:

SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# GSPREAD_CLIENT is assigned by passing the SCOPED_CREDS variable as a parameter of the 'gspread.authorize' method:

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# SHEET provides access to the 'love_sandwiches' spreadsheet and is assigned by passing the file name as a parameter of the 'open' method of the GSPREAD_CLIENT object:

SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# Function to collect sales data from users:

def get_sales_data():
    """
    It gets sales figures input from the user
    """
    print('Please, enter sales data from the last market.')
    print('Data should be six numbers, separated by commas.')
    print('Example: 10, 20, 30, 40, 50, 60\n')

    data_string = input('Enter data here: ')
    print(f'The data provided is {data_string}')

get_sales_data()