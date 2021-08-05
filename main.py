# This is a sample Python script.
import datetime
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

user_name = 'Artem'
list_part = ['Elena','Grigory']
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello my freand, {name}')  # Press ⌘F8 to toggle the breakpoint.
    list_part.append(name)

    # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
print_hi(user_name)
print(f'Now you are in the list of participant {list_part}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(datetime.date.today())