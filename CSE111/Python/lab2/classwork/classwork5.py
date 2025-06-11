def calculating_year(days):
  year=days//365
  month=days%365//30
  day=int(days%365%30)
  print(f"{year} years, {month} months and {day} days")




days= int(input())
calculating_year(days)
