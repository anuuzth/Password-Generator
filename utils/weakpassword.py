import string,secrets

def weak_password():
    letters = string.ascii_letters
    pwd_length = 8
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(letters)) 
    print("Password:"+pwd)