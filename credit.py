from cs50 import get_string
import re


def main():
    card = get_string("Number: ")
    card_type(card)
    
    
def card_type(x):
    if re.search("^3(4|7)", x) and len(x) == 15 and Luhns_alg(x):
        print("AMEX")
    elif re.search("^5[1-5]", x) and len(x) == 16 and Luhns_alg(x):
        print("MASTERCARD")
    elif re.search("^4", x) and (len(x) == 13 or 16) and Luhns_alg(x):
        print("VISA")
    else:
        print("INVALID")
    

def Luhns_alg(y):
    # Reverse order of string
    card_rev = y[::-1]
    # Multiply every second character of string by 2, starting from 1st character, and insert into new list
    card_mult = [int(x) * 2 for x in card_rev[1::2]]
    # Convert list into string and add all digits together
    card_mult_str = ""
    for x in card_mult:
        card_mult_str += str(x)
    sum_of_digits = 0
    for digit in card_mult_str:
        sum_of_digits += int(digit)
    # Add together every second character of string, starting from 0th character, and insert into new variable
    card_sum = 0
    for num in card_rev[::2]:
        card_sum += int(num)
    # Add two sums together and check if % 10 == 0
    return (sum_of_digits + card_sum) % 10 == 0
        

main()