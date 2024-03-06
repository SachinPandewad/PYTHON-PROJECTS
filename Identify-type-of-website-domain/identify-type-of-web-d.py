#The CODE identifies the which type of website is entered by the user.
#here if-elif used to cheak condition.
#and While loop is used to enter multiple websites multiple times.
            #basic info
            # .com = Commercial website.
            # .org = Organisational Website.
            # .in  = Internet Country Code Website.
            # .edu = Educational Website.
            #.ac.in= academic institutes in India


while True:
    user_input = input("Enter URL : ")
    if user_input != (".com", ".in", ".org", ".edu", "ac.in"):
        print("'Url' information is not available.")
    elif ".com" in user_input:
        print("The given Url is of Commercial website.")
        print("On the Internet","'.com'", "is one of the top-level domain name' \nUsually, it describes the entity owning the domain name as a commercial organization.")
    elif ".org" in user_input:
            print("The given Url is of Organisational Website.")
            print("On the Internet '.org' domain extension is \nregistered and used primarily by non-profit organizations ")
    elif ".in" in user_input:
            print("The given Url is of Internet Country Code Website.")
            print("On the Internet '.in' is the Internet country code top-level domain for India.")
    elif ".edu" in user_input:
        print("The given Url is of Educational Website.")
        print("On the Internet '.edu' Intended for educational use.")
    elif "ac.in" in user_input:
        print("The given Url is of academic institution Wbsite.")
        print("On the Internet 'ac.in' This domain name is used for academic institutes in India")
    else:
        print("Thank You")

    enter_again = input("Want to identify again? (y/n): ")
    if enter_again.lower() != "y":
        break