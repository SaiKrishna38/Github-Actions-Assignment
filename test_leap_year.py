from leap_year import is_leap_year
assert is_leap_year(2000) == True
assert is_leap_year(2400) == True
assert is_leap_year(1900) == False
assert is_leap_year(2100) == False
assert is_leap_year(2016) == True
assert is_leap_year(2020) == True
assert is_leap_year(2019) == False
assert is_leap_year(2021) == False
print("✅ All tests passed successfully!")
