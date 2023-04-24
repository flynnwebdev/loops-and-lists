# def get_answer(number):
#     match number:
#         case 1:
#             print("It is certain")
#         case 2:
#             print("It is decidely so")
#         case 3:
#             print("Yes")
#         case 4:
#             print("Try again later")
#         case 5:
#             print("No")
#         case 6:
#             print("Very doubtful")
#         case _:
#             print("Not sure")


# main
print("Magic 8 Ball!")
import random

answers = [
  "It is certain",
  "It is decidely so",
  "Yes",
  "Try again later",
  "No",
  "Very doubtful",
  "Not sure",
]

# get_answer(random.randint(1, 6))
print(answers[random.randint(0, len(answers) - 1)])
