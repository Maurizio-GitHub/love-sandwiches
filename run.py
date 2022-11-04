# The file name, 'run.py', must not be changed.
# The command 'pip3 install gspread google-auth' has been executed in the terminal to leverage 'google-auth'.

import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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


def get_sales_data():
    """
    It gets sales figures input from the user via the terminal.
    It runs a while-loop to collect a valid string of data, which must be a string of six numers separated by commas.
    The loop will repeatedly request data until it is valid.
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


def validate_data(values):
    """
    It validates user data entries (accepting a parameter representing user-entered sales data list).
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


def update_worksheet(data, worksheet):
    """
    It updates the relevant worksheet with the data provided (always a list of integers):
    - It updates the sales worksheet by adding to it a new row with the list of user-provided data;
    - It updates the surplus worksheet by adding to it a new row with the list of calculated surplus data.
    """
    print(f'Updating {worksheet} worksheet...\n')

    # The access to the sales/surplus data hosted into the relevant worksheet is allowed through the 'worksheet()' method of the SHEET object:

    worksheet_to_update = SHEET.worksheet(worksheet)

    # The action of appending data to the spreadsheet hosted into Google Drive is allowed through the 'append_row()' method imported via the 'gspread' library.
    # A new row is added to the end of the data present into the relevant worksheet (explicitly specified when calling the function):

    worksheet_to_update.append_row(data)

    # Print-statements like this are commonly used to provide relevant feedback via the terminal:

    print(f'{worksheet} worksheet updated successfully.\n')


def calculate_surplus_data(sales_row):
    """
    It compares sales with stock and calculates the surplus for each item type.
    The surplus is defined as the sales figures subtracted from the stock:
    - Positive surplus indicates a waste;
    - Negative surplus indicates extra made, due to stock sold out.
    """
    print('Calculating surplus data...\n')

    # The 'get_all_values()' method (imported from 'gspread') is called to pull all the values from the stock worksheet:

    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    surplus_data = [int(stock) - sales for stock, sales in zip(stock_row, sales_row)]
    return surplus_data


def main():
    """
    It runs all program functions.
    The variable assigned first contains the correct sales data returned upon validation.
    The second is assigned with the sales data values converted to integers.
    Then, the following functions are called:
    - The function writing data (sales first) to the relevant spreadsheet;
    - The function to calculate the surplus data;
    - The function writing data (calculated surplus) to the relevant spreadsheet.
    Indeed, it is common practice to wrap the main function calls of a program within a function called main().
    """
    data = get_sales_data()
    sales_data = [int(number) for number in data]
    update_worksheet(sales_data, 'sales')
    current_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(current_surplus_data, 'surplus')


# In Python, function calls must always follow their definitions:

print('Welcome to Love Sandwiches Data Automation!')
main()