


#---------تمرین 24 بازی حدس عدد-----------------#



def guess_number_conditional(secret_number):
    guess = int(input("Guess the number: "))
    i = 1
    while guess != secret_number :
        if guess < secret_number:
            print("Too Low")
        else:
            print("Too High")
        guess = int(input("Guess the number: "))
        i +=1
    print("Correct!")
    return i

print(guess_number_conditional(13))


#-----------------



def guess_number_break(secret_number):
    i = 0
    while True :
        guess = int(input("Guess the number: ")) 
        i +=1
        if guess < secret_number:
              print("Too Low")
        elif guess > secret_number:
              print("Too High")
        else:
              print("Correct!")
              return i
          
print(guess_number_break(13))
