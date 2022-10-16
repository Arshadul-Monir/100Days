# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

pizza = {
    "S":15,
    "M":20,
    "L":25
}

price = pizza[size]

if(add_pepperoni=="Y"):
    if(size=="S"):
        price+=2
    else:
        price+=3
if(extra_cheese=="Y"):
    price+=1

print("Your final bill is: $%i"%(price))
