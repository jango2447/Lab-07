#Like in the above statements, all we are doing here is getting some user input and storing 
#that input in the variable userName. In this case, the users log-in name is scored in the variable.

userName = input("Hello! Please enter your facebook username!")

#I'm doing the same thing here as in line 1, except
#the variable userPassword is storing the users password

userPassword = input("Hello! Please enter your facebook password!")

#Here, things get a little more interesting. I'm using a conditional if-statement where I'm checking 
#the boolean expression if userName == michael resolves to true and userPassword == 
#ProgrammingRocks! is also true, then we print out Welcome to facebook!

# if the username that the user provides does not match the string 'michael' and the userPassword the 
#user provides does not match the string ProgrammingRocks!, then the user is denied entry and 
#the message wrong credentials, try again! is reported.


if(userName.lower() == "nicholas" and userPassword == "ThisIsFun!"):
    print("Welcome to facebook!")
else:
    print("Wrong credentials, try again!")
