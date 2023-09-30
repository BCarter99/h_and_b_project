from dotenv import load_dotenv
import os


def create_list(file_name) -> list:
    '''
    Opens a given file and creates a list of the items.

    Returns (list): txt_list.

    Keyword arguments:
    file_name (str): name of the file to be opened.

    Variables:
    file_items (str): content of the given text file.
    txt_list (list): list of file_items items split by \n.
    '''
    with open(file_name, 'r') as list_file:
        file_items = list_file.read()
        txt_list = file_items.split('\n')
        txt_list = txt_list[:-1]
        return txt_list


def overwrite(txt_list, file_name) -> None:
    '''
    Overwrites contents of file with list contents.

    Keyword arguments:
    txt_list (list): list to overwrite file with.
    file_name (str): name of the file to be overwritten.
    '''
    with open(file_name, 'w') as list_file:
        for item in range(len(txt_list)):
            list_file.write(f'{txt_list[item]}\n')


def validate_password(user, password):
    '''
    Validates the password given matches the correct user.

    Keyword arguments:
    user (str): The given user
    password (str): The given password

    Returns (bool): True if the password was validated, nothing
                  if not valid
    '''
    load_dotenv()
    env_password = os.getenv(user)

    if password == env_password:
        print('\nLog in successful\n')
        return True
    else:
        print('\nIncorrect password\n')
