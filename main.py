# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_left = 90 - int(age)
days = round(age_left*365)
weeks = round(age_left*52)
month = round(age_left*12)
print(f"You have {days} days, {weeks} weeks, and {month} months left.")