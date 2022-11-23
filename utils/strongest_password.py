import string,secrets

def strongest_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    source = letters + digits+special_chars
    pwd_len = 16
    pwd = ''
    for i in range(pwd_len):
        pwd += ''.join(secrets.choice(source))
    print("Password:"+pwd)