from cryptography.fernet import Fernet #cryptograpy used to secure password stored in passwords.txt file.

    
    #To genrate key.key file remove ''' commetn of below program
'''
def write_key():
     key = Fernet.generate_key()
     with open("key.key", "wb") as key_file:
        key_file.write(key)
         '''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



key = load_key()
fer = Fernet(key)


def view(user_name): 
    
    with open('passwords.txt', 'r') as a:
        for line in a.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            if user_name == user:
                 print("Password:", fer.decrypt(passw.encode()).decode())
                 break
           

def add():
    name = input('Account Name: ').lower()
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: #Create passwords.txt file and store user, password separated by '|'.
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")  


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        user_name = input("Enter user name to get password: ").lower() #to find password by user input.
        view(user_name)
            
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue