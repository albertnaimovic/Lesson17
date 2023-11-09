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

from typing import List
import datetime
import logging

logging.basicConfig(level=logging.DEBUG,filename='1_task.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def format_date_string(my_date: str) -> list:
    try:
        datetime.datetime.strptime(my_date, "%Y:%m:%d")
    except Exception as err:
        logging.error(f'You got {err} error!')
    else:
        number_list = [int(x) for x in my_date if x.isnumeric()]
        return number_list


def sum_numbers(number_list: List[int]) -> int:
    # try:
        suma = sum(number_list)
        return suma
    # except Exception as err:
        # logging.error(f'You got {err} error!')

def divide_two_numbers(number_list: List[int]) -> float:
    # try:
        return max(number_list) / min(number_list)
    # except Exception as err:
        # logging.error(f'You got {err} error!')

def days_power_month(number_list: str) -> int:
    dd = int ("" + (str(number_list[6])) + str(number_list[7]))
    mm = int("" + (str(number_list[4])) + str(number_list[5]))
    # try:
    return dd ** mm
    # except Exception as err:
        # logging.error(f'You got {err} error!')
    

my_date:str = "1997:10:09" # input("Enter your date of birth (YYYY:MM:DD): ")

try:
    number_list: list = format_date_string(my_date)
    suma = sum_numbers(number_list)
    power = days_power_month(number_list)
    divided_nums = divide_two_numbers(number_list)
    print(f"Sum: {suma}\nDivision: {divided_nums}\nPower: {power}")
except Exception as err:
    logging.error(f'You got {err} error!')

