# write a function to test if a year is a leap year
# Hints:
# 1. A year is a leap year if it is divisible by 4 but not by 100 
# 2. A year is always a leap year if it is divisible by 400



def is_leap_year(year):
  is_leap = False
  
  if year % 4 == 0:
    is_leap = True
    
    if year % 100 == 0:
      is_leap = False
      
      if year % 400 == 0:
        is_leap = True
  
  res = "Leap" if is_leap else "Not leap"
  
  print(f"{year} is {res}")    

# test 
year = 2016

is_leap_year(2100)