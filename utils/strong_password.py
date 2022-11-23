import string,secrets

def strong_password():
    letters = string.ascii_letters
    digits = string.digits
    source = letters + digits
    pwd_len = 12
    pwd = ''
    for i in range(pwd_len):
        pwd += ''.join(secrets.choice(source))
    print("password:"+pwd)