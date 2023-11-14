# def divide_two_numbers(dividend: int, divisor: int) -> None:
#     try:
#         return dividend / divisor
#     except Exception as err:
#         print(f'You got {err} error!')

# def power(a, b):
#     answer_number = divide_two_numbers(a, b)
#     if not answer_number:
#         return 0
#     return answer_number ** 2

# # print(divide_two_numbers(1, 0))
# print(power(1, 0))


# Create a program which takes a sentence as your birth date (YYYY:MM:DD)
# The program should return sum of all numbers, bigest and lowest number division
# and days with power of month (dd ** mm)
# The code should be structured correctly: functions, error handling and logging.

# from typing import List
# import datetime
# import logging

# logging.basicConfig(level=logging.DEBUG,filename='1_task.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


# def format_date_string(my_date: str) -> list:
#     try:
#         datetime.datetime.strptime(my_date, "%Y:%m:%d")
#     except Exception as err:
#         logging.error(f'You got {err} error!')
#     else:
#         number_list = [int(x) for x in my_date if x.isnumeric()]
#         return number_list


# def sum_numbers(number_list: List[int]) -> int:
#     suma = sum(number_list)
#     return suma


# def divide_two_numbers(number_list: List[int]) -> float:
#     return max(number_list) / min(number_list)


# def days_power_month(number_list: str) -> int:
#     dd = int ("" + (str(number_list[6])) + str(number_list[7]))
#     mm = int("" + (str(number_list[4])) + str(number_list[5]))
#     return dd ** mm


# my_date:str = "1997:10:09" # input("Enter your date of birth (YYYY:MM:DD): ")

# try:
#     number_list: list = format_date_string(my_date)
#     suma = sum_numbers(number_list)
#     power = days_power_month(number_list)
#     divided_nums = divide_two_numbers(number_list)
#     print(f"Sum: {suma}\nDivision: {divided_nums}\nPower: {power}")
# except Exception as err:
#     logging.error(f'You got {err} error!')

# create a program which takes random sequence of numbers and letters (example: 'dfssdfsdfsdf655sdf2654fs6d4646').
# The program should return (All stages requires separate functions, with logging all necessary data to file and error handling):
# 1) list of letters ordered
# 2) list of letters of reversed order
# 3) funtion which return list with only uniques letters (Can't repeat)
# 4) the same do with numbers
# 5)the sum of amount of letters and numbers are provided
# Rules:
# The program after text entered, should provide options list of actions:
# 1) Get list ordered
# 2) Get list ordered reversed etc...

# If there is special symbols,gaps - they should be added to special data structure , as we will have option :
# n) Show special symbols if provided.
# After any option is being used, terminal should ask if we want to use another option or to exit the program.
# If we choose to use another option, the option we already choose should be marked as `checked`:
# 1) Get list ordered[checked]

import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename="main_task.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


def ordering_letters(letters: str) -> list:
    ordered_letters: list = sorted([x for x in letters if x.isalpha()])
    return ordered_letters


def reverse_ordering_letters(letters: str) -> list:
    reversed_order_letters: list = sorted(
        [x for x in letters if x.isalpha()], reverse=True
    )
    return reversed_order_letters


def do_unique_letters(letters: str) -> list:
    unique_letters = set([x for x in letters if x.isalpha()])
    return list(unique_letters)


def ordering_numbers(numbers: str) -> list:
    ordered_numbers: list = sorted([x for x in numbers if x.isnumeric()])
    return ordered_numbers


def reverse_ordering_numbers(numbers: str) -> list:
    reversed_order_numbers: list = sorted(
        [x for x in numbers if x.isnumeric()], reverse=True
    )
    return reversed_order_numbers


def do_unique_numbers(numbers: str) -> list:
    unique_numbers = set([x for x in numbers if x.isnumeric()])
    return list(unique_numbers)


def sum_of_numbers_and_letters(sequence: str) -> str:
    letters = [x for x in sequence if x.isalpha()]
    numbers = [x for x in sequence if x.isnumeric()]
    return f"Sum of letters: {len(letters)}\nSum of numbers: {len(numbers)}"


def special_chars(sequence: str) -> bool:
    special_chars: list = [x for x in sequence if not x.isalnum()]
    return special_chars


def check_for_special_chars(sequence: str) -> bool:
    special_chars: list = [x for x in sequence if not x.isalnum()]
    if len(special_chars) == 0:
        return False
    else:
        return True


def main_menu() -> None:
    random_sequence: str = "c6809856m u985uc2*-93xmi239m2958m2cn952"

    # random_sequence: str = input("Enter random sequence: ")
    # while len(random_sequence) < 25 and any(x.isalpha() for x in random_sequence) != True and any(x.isnumeric() for x in random_sequence) != True:
    #     random_sequence: str = input("Enter random sequence: ")

    selection_1: str = " 1) list of letters ordered"
    selection_2: str = " 2) list of letters of reversed order"
    selection_3: str = " 3) funtion which return list with only uniques letters"
    selection_4: str = " 4) list of numbers ordered"
    selection_5: str = " 5) list of numbers of reversed order"
    selection_6: str = " 6) funtion which return list with only uniques numbers"
    selection_7: str = " 7) the sum of amount of letters and numbers are provided"
    selection_8: str = " 8) Show special symbols if provided."
    selection_9: str = " 9) exit."

    menu_one: str = f"{selection_1}\n{selection_2}\n{selection_3}\n{selection_4}\n{selection_5}\n{selection_6}\n{selection_7}\n{selection_9}\nEnter your selection:  "
    menu_two: str = f"{selection_1}\n{selection_2}\n{selection_3}\n{selection_4}\n{selection_5}\n{selection_6}\n{selection_7}\n{selection_8}\n{selection_9}\nEnter your selection:  "

    if check_for_special_chars(random_sequence) == True:
        menu = menu_two
    else:
        menu = menu_one

    while True:
        menu_select: str = input(menu)
        print()

        if menu_select.isnumeric() == True:
            if menu_select == "1":
                print(ordering_letters(random_sequence))
                if selection_1[-9:] != "[checked]":
                    selection_1 += " [checked]"
            elif menu_select == "2":
                print(reverse_ordering_letters(random_sequence))
                if selection_2[-9:] != "[checked]":
                    selection_2 += " [checked]"
            elif menu_select == "3":
                print(do_unique_letters(random_sequence))
                if selection_3[-9:] != "[checked]":
                    selection_3 += " [checked]"
            elif menu_select == "4":
                print(ordering_numbers(random_sequence))
                if selection_4[-9:] != "[checked]":
                    selection_4 += " [checked]"
            elif menu_select == "5":
                print(reverse_ordering_numbers(random_sequence))
                if selection_5[-9:] != "[checked]":
                    selection_5 += " [checked]"
            elif menu_select == "6":
                print(do_unique_numbers(random_sequence))
                if selection_6[-9:] != "[checked]":
                    selection_6 += " [checked]"
            elif menu_select == "7":
                print(sum_of_numbers_and_letters(random_sequence))
                if selection_7[-9:] != "[checked]":
                    selection_7 += " [checked]"
            elif menu_select == "8" and menu == menu_two:
                print(special_chars(random_sequence))
                if selection_8[-9:] != "[checked]":
                    selection_8 += " [checked]"
            elif menu_select == "9":
                print("Bye")
                break
            else:
                print("There is no such selection.")
        else:
            print(
                "Please enter number from list provided without any symbols and spaces."
            )
        print()


main_menu()
