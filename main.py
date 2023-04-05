rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
image = [rock, paper, scissors]

print("Let's play rock, paper scissors!")
choice_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if choice_user >= 0 and choice_user <= 2:
  print(image[choice_user])
else:
  print("")
  
print("Computer chose:\n")
choice_computer = random.randint(0,2)
print(image[choice_computer])

if choice_user >= 3:
  print("You typed an invalid number. You lose")
elif choice_user == choice_computer:
  print("It's a tie")
elif choice_user + 2 == choice_computer:
  print("You win!")
elif choice_user <  choice_computer:
  print("You lose")
elif choice_user == choice_computer + 2:
  print("You lose")
else:
  print("You win!")