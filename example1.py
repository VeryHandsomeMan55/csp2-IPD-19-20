####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Betray'
strategy_description = 'Always betray.'
    
import random

def move(my_history, their_history, my_score, their_score):
  '''50% chance to put a c and 50% chance to put a b'''
  ch = 0
  ch == random.randint(1, 2)
  if ch == 1:
    return 'c'
  elif ch == 2:
    return 'b'
