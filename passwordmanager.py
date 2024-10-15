import random

def generate_password():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    password = ''
    
    for _ in range(4):
        word = random.choice(words)
        password += word + random.choice(['!', '@', '#', '$'])
    
    password = password.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('u', '9')
    
    return password

if __name__ == '__main__':
    password = generate_password()
    print(password)