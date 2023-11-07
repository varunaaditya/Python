import random
passwd= int(input("enter the length of the password: "))
c= "abcdefghijklmnopqrstuvwxyz81234567898ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&* ()?*"
output="".join(random.sample(c ,passwd))
print(output)
print("MAKE SURE YOUR PASSWORD SAKE!!!!")