from utils.weakpassword import weak_password
from utils.strong_password import strong_password
from utils.strongest_password import strongest_password
def main():
    print("""
        ========WELCOME TO PASSWORD GENERATOR===========
                1.Weak Password
                2.Strong Password
                3.Strongest Password
            **enter any number to EXIT** 
        """)
    choice = int(input("Enter your choice:"))
    if choice == 1 :
        weak_password()
        main()
    elif choice == 2:
        strong_password()
        main()
    elif choice == 3:
        strongest_password()
        main()
    else:
        exit()   


if __name__ == "__main__":
    main() 