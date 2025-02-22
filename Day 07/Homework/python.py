def convert_number(number, from_base, to_base):
    decimal_number = int(number, from_base)
    
    if to_base == 10:
        return str(decimal_number)
    
    result = ''
    while decimal_number > 0:
        remainder = decimal_number % to_base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        decimal_number //= to_base
    
    return result if result else '0'

number = input("enter number: ")
from_base = int(input("from base: "))
to_base = int(input("to base: "))

converted = convert_number(number, from_base, to_base)
print(f"number {number} ({from_base} system) is {converted} ({to_base} system)")
