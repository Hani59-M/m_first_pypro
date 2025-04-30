from datetime import datetime

date1_str = input("Enter the first date (dd-mm-yyyy): ")
date2_str = input("Enter the second date (dd-mm-yyyy): ")

date1 = datetime.strptime(date1_str, "%d-%m-%Y")
date2 = datetime.strptime(date2_str, "%d-%m-%Y")

difference = abs((date2 - date1).days)
print(f"The difference between two dates is {difference} days.")
