# main.py
# Day 05 Procject Password Generator

"""
    This program generates a strong password from user input.
    The user defines the password length by inputting how many
    letters, numbers and symbols to include in its composition.
"""
from random import randint, seed
r_s = randint(0, 4294967295)
s = seed(r_s)
length = 0
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
letters = str(
        "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz"
        )
symbols = str("~`!@#$%^&*-_+=|?<>")
password = ""
print("Weclome to the PyPassword Generator!")
ch_let = int(input("How many letters would you like? "))
ch_sym = int(input("How many symbols would you like? "))
ch_num = int(input("How many numbers would you like? "))
length = ch_let + ch_sym + ch_num

print(
        f"You have chosen {ch_let} letters, {ch_sym} " +
        f"symbols and {ch_num} numbers. " +
        f"A {length} character password."
        )


def choose_letter(num: int):
    if num == 0:
        return
    _letters = ""
    for n in range(num):
        m_index = randint(0, len(letters) - 1)
        ch_l = letters[m_index]
        _letters += ch_l
    return _letters


def choose_symbols(num: int):
    if num == 0:
        return
    _symbols = ""
    for n in range(num):
        m_index = randint(0, len(symbols) - 1)
        ch_s = symbols[m_index]
        _symbols += ch_s
    return _symbols


def choose_numbers(num: int):
    if num == 0:
        return
    _numbers = ""
    for n in range(num):
        m_index = randint(0, len(numbers) - 1)
        ch_n = numbers[m_index]
        _numbers += str(ch_n)
    return _numbers


def scramble(let: str = "", sym: str = "", num: str = ""):
    _password = ""
    let_check = []
    sym_check = []
    num_check = []
    while True:
        ch_set = randint(0, 2)
        if ch_set == 0:
            #  scramble letters
            if let == "":
                pass
            else:
                m_l = randint(0, len(let) - 1)
                if m_l in let_check:
                    pass
                else:
                    ch_l = let[m_l]
                    _password += ch_l
                    let_check.append(m_l)
                    if len(_password) == length:
                        break
        elif ch_set == 1:
            # scramble symbols
            if sym == "":
                pass
            else:
                m_s = randint(0, len(sym) - 1)
                if m_s in sym_check:
                    pass
                else:
                    ch_s = sym[m_s]
                    _password += ch_s
                    sym_check.append(m_s)
                    if len(_password) == length:
                        break

        elif ch_set == 2:
            # scramble numbers
            if num == "":
                pass
            m_n = randint(0, len(num) - 1)
            if m_n in num_check:
                pass
            else:
                ch_n = num[m_n]
                _password += ch_n
                num_check.append(m_n)
                if len(_password) == length:
                    break

    return _password


selected_l = choose_letter(ch_let)
selected_s = choose_symbols(ch_sym)
selected_n = choose_numbers(ch_num)
pw = scramble(selected_l, selected_s, selected_n)
print(f"Your new password is: {pw}")
