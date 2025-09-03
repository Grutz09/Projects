import sys
from datetime import datetime

employees = open("employees.txt").read()
    
name = input("Please enter your name:").strip()
count = 0

while name not in employees:
    count += 1
    if count == 3:
        print("Tried 3 times. Please contact info desk. Program Terminated.")
        sys.exit()
    name = input("Please enter your name again:")
    
clockin_time = datetime.now().replace(microsecond=0)


last_action = None
try:
    with open("clockin_record.txt") as db:
        for line in db:
            parts = line.strip().split("\t")
            if len(parts) >=3 and parts[0] == name:
                last_action = parts[2].strip()
except FileNotFoundError:
    pass


if last_action == "Clock In":
    new_action = "Clock Out"
    print("Have a nice day!", name)
    if clockin_time.hour < 16:
        print("Status:Early Leave")
else:
    new_action = "Clock In"
    print("Welcome to the office! ", name)
    if clockin_time.hour > 8:
        print("Status:Late")
    
with open("clockin_record.txt", "a") as f:
    f.write(f"{name}\t{clockin_time}\t{new_action}\n")



print("Request Monthly Summary? Y|N")
req = input()
if req == "Y":
    print("Monthly Summary")
    with open("clockin_record.txt", "r") as timestamp:
        for line in timestamp:
            parts = line.strip().split("\t")
            if len(parts) == 3:
                name, time, action = parts
            elif len(parts) == 2:
                name, time = parts
                action = "Unknown"
            else:
                continue
            time_obj = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
            if time_obj.month == 8:
                print(f"{name}\t{time}\t{action}")
else:
    pass
