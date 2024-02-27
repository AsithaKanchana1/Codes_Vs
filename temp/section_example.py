print("____This is Age Calculator____")

x=int(input("Enter Present Year : "))
y=int(input("Enter Your Birth Year : "))

z=x-y

if z<18:
    print("You Are ",z," years old so You are chiled")
else:
    print("You Are ",z," years old so You are adoult")