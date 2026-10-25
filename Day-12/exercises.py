# Write a function which generates a six digit/character random_user_id.
import random
import string

def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters for each ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))

    characters = string.ascii_letters + string.digits
    ids = []
    for _ in range(num_ids):
        id = ''.join(random.choice(characters) for _ in range(num_characters))
        ids.append(id)
    return ids

# write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

# Level 2

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hex_colors.append(color)
    return hex_colors

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(num_colors, color_type):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("Invalid color type. Use 'hexa' or 'rgb'.")