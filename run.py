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

# GSPREAD_CLIENT is assigned by passing the SCOPED_CREDS variable as a parameter of the 'gspread.authorize' method.

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# SHEET provides access to the 'love_sandwiches' spreadsheet and is assigned by passing the file name as a parameter of the 'open' method of the GSPREAD_CLIENT object.

SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# Here is how to access the data into the 'sales' worksheet. The parameter name, 'sales', corresponds to the name of the relevant worksheet:

sales = SHEET.worksheet('sales')

# Here a 'gspread' method, 'get_all_values' is called to pull all the values from our sales worksheet:

data = sales.get_all_values()

# Whenever data is printed out here (by typing 'python3 run.py' to the terminal), it is imported as a list of lists:

print(data)