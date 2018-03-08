team_name = 'Santiago'  
strategy_name = 'Mirror Image'
strategy_description = 'Pick c on the first round, then for every round after pick what the other team has picked in the last round.'


def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return "c"
    else:
        return their_history[-1]
