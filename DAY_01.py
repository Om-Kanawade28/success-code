import random

def motivational_quote():
  quotes = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Don't be afraid to give up the good to go for the great.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "It's not the mountain we conquer but ourselves.",
    "The difference between ordinary and extraordinary is that little extra.",
    "You don't have to be great to start, but you have to start to be great.",
    "The only person you are destined to become is the person you decide to be."
  ]
  return random.choice(quotes)

print(f"You've got this! Remember: {motivational_quote()}")






