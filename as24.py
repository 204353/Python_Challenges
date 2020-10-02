import datetime
from datetime import date
print("Enter your date in this format", datetime.date.today())
while True:
    try:
        date_text = input("Date 1:")
        d1 = datetime.datetime.strptime(date_text, '%Y-%m-%d')
        date_text2 = input("Date 2:")
        d2 = datetime.datetime.strptime(date_text2, '%Y-%m-%d')
        print(f"There were {(d2 - d1).days} days in the project")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")