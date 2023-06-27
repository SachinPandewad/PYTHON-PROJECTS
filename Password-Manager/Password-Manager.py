def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User Id:", user,) 
            print("Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
       f.write(name + "|" + pwd + "\n")

while True:
    add_id_pass = input("Add your user id & password : (add) ").lower()
    if add_id_pass == "add":
        add()
    else:
        print("Wrong user Input. Enter Again.")
        
        
    mode = input("Would you like to add a new password or view existing one (view or v, add or a), Press q to quit ").lower()

    if mode == "view" or mode == "v":
        view()
    elif mode == "add" or mode=="a" or store_id_pass == "add":
        add()
    else:
        print("Invalid  mode")
        continue
    
    enter_again = input("Enter again? (y/n): ")
    if enter_again.lower() != "y":
        break