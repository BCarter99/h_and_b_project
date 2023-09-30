'''
First python project with B and H
'''
import functions as func
import profiles as pf


def main():

    pf.profile()

    input1 = 0

    while input1 != 4:

        # raises an error if user input can not be converted to an int
        try:
            input1 = int(
                input('1. Add an item\n'
                      '2. View items\n'
                      '3. Delete item\n'
                      '4. Quit\n\n'))
        except ValueError:
            print('\nNot a valid input dumass\n')
            continue

        # adds an item to the text file list
        if input1 == 1:
            item = input('\nAdd item: ')
            print()
            with open('lists/list1.txt', 'a') as list_file:
                list_file.write(f'{item.upper()}\n')

        # prints the list to the user
        elif input1 == 2:
            with open('lists/list1.txt', 'r') as list_file:
                file_items = list_file.read()
            print()
            print(file_items)

        # option to delete item off of list
        elif input1 == 3:
            txt_list = func.create_list('lists/list1.txt')

            dlt_item = input('\nWhat would you like to delete?\n\n').upper()

            if dlt_item in txt_list:
                cert1 = input(
                    f'\nAre you sure you want to delete {dlt_item}? (y/n)\n\n'
                ).upper()

                if cert1 == 'Y' or cert1 == 'YES':
                    txt_list.remove(dlt_item)
                    print(f'\n{dlt_item} has been deleted\n\n')

                    func.overwrite(txt_list, 'lists/list1.txt')

                else:
                    print()
                    continue

            else:
                print(f'\n{dlt_item} is not in list\n\n')
                continue

        # repeats the while loop if user does not input a valid int
        elif input1 < 1 or input1 > 4:
            print('\n\nstoopid\n\n')
            continue


if __name__ == '__main__':
    main()
