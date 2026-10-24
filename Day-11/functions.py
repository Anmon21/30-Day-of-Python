# Function without parameters
def generate_full_name():
    first_name = 'Bilguun'
    last_name = 'Deleg'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
generate_full_name()  # 'calling a function without parameters'
def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
add_two_numbers()  # 'calling a function without parameters'

# Function with parameters
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
generate_full_name('Bilguun', 'Deleg')  # 'calling a function with parameters'
def add_two_numbers(num_one, num_two):
    total = num_one + num_two
    return total
add_two_numbers(2, 3)  # 'calling a function with parameters'   
