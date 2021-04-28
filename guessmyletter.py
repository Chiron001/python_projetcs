word = "user"
comamnd = ""
i=0
guess = []
joined = ""

print("enter some letters to understand")

wordsplit = list(word)

print(wordsplit)

while True:
  command = str(input("guess letter: "))
  if(command == wordsplit[i]):
    guess.append(wordsplit[i])
    i+=1
    if(i == len(wordsplit)):
      print("you done it!")
      break
    print(guess)
  elif(joined == word):
    print("you guessed my word!")
  else:
    print("try one more time")
    print(guess)


joined = joined.join(guess)
print("you corrected right!")
print(joined)
  

 
