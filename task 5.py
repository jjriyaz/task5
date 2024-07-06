# Expected Output of python code
data = [10, 501, 23, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 100, data)
print(list(result))

# Python code using lambda function to check integer or string
items = [1, 'hello',3.5, 'world', 10, '123']
check_type = lambda x: isinstance(x, (int, str))
result = list(map(check_type,items))
print(result)

#Python lambda function to create fibonacci series
from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
n = 50
fib_series = fibonacci(n)
print(fib_series)

# Python function for regular expression validation
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_bd_mobile(mobile):
    pattern = r'^01[3-9]\d{8}$'
    return bool(re.match(pattern, mobile))

def validate_us_telephone(telephone):
    pattern = r'^\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$'
    return bool(re.match(pattern, telephone))

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return bool(re.match(pattern, password))

# Example usage:
email = "test@example.com"
bd_mobile = "01712345678"
us_telephone = "123.456.7890"
password = "Userpassword@123"

print(validate_email(email))
print(validate_bd_mobile(bd_mobile))
print(validate_us_telephone(us_telephone))
print(validate_password(password))