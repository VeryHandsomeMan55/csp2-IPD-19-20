####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Collude'
strategy_description = 'Always collude.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player always colludes.
    return 'c'

import random

def Stra_all(my_history, their_history, my_score, their_score):
  ''' That it will be a function where it will check if it is the first round it will conclude. The last few rounds of games, it will betray, if it is false, then it will see if the other person betrayed last time, if it is false, then it will do a coin flip to see if it will betray or conclude. They all return betray except the coin flip and at the beginning.'''
  if len(my_history) == 8 or len(my_history) == 9:
    return 'b'
  elif my_history[-1]=='c' and their_history[-1]=='b':
    return 'b' 
  else:
    choice == random.randint(1, 2)
    if choice == 1:
      return 'c'
    elif choice == 2:
      return 'b'