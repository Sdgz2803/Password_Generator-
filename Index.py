import re
import string
import secrets

'''
This project involves building a program that generates a strong password for users. The program asks users for the length and complexity of the password they want to generate.

Use random module to generate a random password and conditional statements to check the complexity of the password.

Allow users to specify the length and complexity of the generated password.
'''


def easy_password(length):
    characters = string.ascii_lowercase + string.digits
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if re.match(r"^[a-z0-9]{8,}$",password):
            return password

    
def medium_password(length):
    characters = string.ascii_lowercase + string.digits
    random_lower = secrets.choice(string.ascii_lowercase)
    random_upper = secrets.choice(string.ascii_uppercase)
    random_digit = secrets.choice(string.digits)
    temp = random_lower + random_upper + random_digit
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length-3))
        password = password + temp
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
            return password 

def hard_password(length):
    characters = string.ascii_lowercase + string.digits + string.punctuation
    random_punct1 = secrets.choice(string.punctuation)
    random_lower = secrets.choice(string.ascii_lowercase)
    random_upper = secrets.choice(string.ascii_uppercase)
    random_digit = secrets.choice(string.digits)
    random_punct2 = secrets.choice(string.punctuation)
    temp = random_lower + random_punct1 + random_upper + random_digit + random_punct2
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length-5))
        password = password + temp
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[a-zA-Z\d\W_]{10,}$", password):
            return password
        
def get_valid_length():
    while True:
        try:
            password_length = int(input("How long do you want your password?\n"))
            if password_length < 8 or password_length > 12:
                print('Please insert a number higher than 8 or lower than 12 for a valid password length.')
            else:
                return password_length
        except ValueError:
            print('Invalid input. Please enter a valid number.')
            
def get_valid_complex(length):
    while True:
        complexity = input("How complex do you want your password? Easy = s, Medium = m, Hard = h\n")
        if complexity == 's' and length >= 8:
            return 's'
        elif complexity == 'm' and length >= 8:
            return 'm'
        elif complexity == 'h' and length >= 10:
            return 'h'
        elif complexity == 'h' and length <= 9:
            return 'h'
        else:
            print('Invalid input. Please choose again.')
            continue
    
def generate_password():
    while True:
            try:
                password_length = get_valid_length()
                complexity = get_valid_complex(password_length)

                if complexity == 's':
                    print(f"Generating password with length {password_length} and complexity Easy...\n")
                    password = easy_password(password_length)
                elif complexity == 'm':
                    print(f"Generating password with length {password_length} and complexity Medium...\n")
                    password = medium_password(password_length)
                elif complexity == 'h':
                    print(f"Generating password with length {password_length} and complexity Hard...\n")
                    password = hard_password(password_length)

                print(f'Generated Password: {password}\n')
                break

            except Exception as e:
                print(f"Error: {e}")
        

if __name__ == '__main__':
    generate_password()
