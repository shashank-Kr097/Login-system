#This is a simple login ststem.
user = 'Sha78'
passw = '7854'
#We assume that user name is 'Sha78' and pasword is 7854.
attempt = 0
max_attempt = 3
#People try upto 3 times login.
while True:
    usp = input("Enter Your user ID - ")
    pps = input("Enter your password - ")
    if user == usp and passw == pps:
        print("Welcome Shashank")
#If everything enter right. it login.
        break
#This code run if user enter wrong user ID and Password.After 3 times it cloze.
    else:
        attempt += 1
        print('Wrong credentials. Attempts left:', max_attempt - attempt)
        if attempt >= max_attempt:
            print("To many error. Try again latter")
            break
