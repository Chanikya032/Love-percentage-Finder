# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined= name1+name2
result= combined.lower()
t= result.count("t")
r= result.count("r")
u= result.count("u")
e= result.count("e")
true= str(t+r+u+e)
l= result.count("l")
o= result.count("o")
v= result.count("v")
e= result.count("e")
love= str(l+o+v+e)
lovescore= true+love
score= int(lovescore)
if score<10 or score>90:
    print(f"your score is {score}, you go together like coke and mentos")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"your score is {score}")


