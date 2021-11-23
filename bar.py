from barcode import EAN13

number = '5901234123457'
my_code = EAN13(number)
print(my_code.save('new_cod'))
