import time

# define variables 
name = input("Enter your name: ")
hour = int(time.strftime("%H"))

# function to return greeting based on the time of day
# 0-11: Good Morning
# 12-17: Good Afternoon
# 18-23: Good Evening
def greeting():
    if hour >= 0 and hour < 12:
        return "Good Morning, " + name
    elif hour >= 12 and hour < 18:
        return "Good Afternoon, " + name
    else:
        return "Good Evening, " + name 
    
print(greeting())

