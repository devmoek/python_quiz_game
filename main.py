print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# first answer
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Good job! You are right")
    score += 1
else:
    print("Unfortunately, you are not right. Try again!")

# second answer
answer = input("What is RAM? ")
if answer.lower() == "random access memory":
    print("Good job! Let's continue")
    score += 1
else:
    print("Unfortunately, you are not right. Try again!")

# third answer
answer = input("What is PC? ")
if answer.lower() == "personal computer":
    print("Good job!")
    score += 1
else:
    print("Unfortunately, you are not right. Try again!")

# fourth answer
answer = input("What is GPU? ")
if answer.lower() == "graphics processor unit":
    print("That's right!")
    score += 1
else:
    print("Unfortunately, you are not right. Try again!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")