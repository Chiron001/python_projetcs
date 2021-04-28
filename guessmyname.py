import random

fruit = ['apple', 'banna', 'pear']
count =0;

word = random.choice(fruit)
print(word)

guess =""

print("In this game you will guess my fruit\n")

while(count!=3):
  guess = input(">>")
  count+=1

  if(guess == word):
    print("you win. You choose right food")
  elif(count == 3):
    print("you loose")
    break
  else:
    print("try hard you are close")
  
