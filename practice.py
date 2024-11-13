# Write a program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.

def convert_date(date):
    year, month, day = date.split('-')
    return f"{day}-{month}-{year}"
print(convert_date("2020-05-06"))  








