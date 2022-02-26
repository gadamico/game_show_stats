def prob_plyr3_too_small(plyr2):
    """This function returns the probability that Player 3's
    total will be under Player 2's (input)."""
    
    import numpy as np
    zs = np.arange(1, plyr2-1)
    addends = [(plyr2-1-z) for z in zs]
    return np.sum(addends) / 400

def prob_plyr3_goes_over(plyr2):
    """This function returns the probability that Player 3's
    total will be over $1.00 (after failing to match or exceed
    Player 2's total on the first spin)."""
    
    import numpy as np
    zs = np.arange(1, plyr2)
    return np.sum(zs) / 400

def prob_plyr3_ties_then_loses(plyr2):
    """This function returns the probability that Player 3
    ties Player 2 on one or two spins and then loses, either
    by exceeding $1.00 or by losing in a one-spin playoff.
    We assume here the optimal strategy for Player 3 when
    tying Player 2 on the first spin of spinning again when
    the score is 50 cents or less and otherwise staying (and
    waiting for the one-spin playoff)."""
    
    import numpy as np
    two_spins = (plyr2-1) / 800
    if plyr2 <= 10:
        one_spin = plyr2/400
    else:
        one_spin = 1/40
    
    return two_spins + one_spin

def first_player():
    """This function simulates the turn of the first person
    in the Showcase Showdown."""
    
    import numpy as np
    choices = [5*i for i in range(1, 21)]
    spin1 = np.random.choice(choices)
    print(f'Player1 spun {spin1} cents. Will Player1 spin again?')
    choice = input('Yes or No: ')
    if choice == 'No':
        play1 = spin1
    else:
        spin2 = np.random.choice(choices)
        if spin1 + spin2 > 100:
            
            # If the player exceeds $1.00 we set the value of their
            # collective spins to 0.
            play1 = 0
            print(f'Player1 spun {spin2}. Player1 is over!')
        else:
            print(f'Player1 spun {spin2}.')
            play1 = spin1 + spin2
            print(f'Player1 has {play1}.')
    return play1

def second_player(play1):
    """This function simulates the turn of the second person
    in the Showcase Showdown."""
    
    import numpy as np
#     if play1 > 0:
#         print(f'Player1 has {play1}.')
    choices = [5*i for i in range(1, 21)]
    spin1 = np.random.choice(choices)
    print(f'Player2 spun {spin1}.')
    if spin1 >= play1:
        
        # Player 2 has the option of spinning again if they beat
        # Player 1 on the first spin.
        print(f'Player2 spun {spin1} cents. Will Player2 spin again?')
        choice = input('Yes or No: ')
        if choice == 'No':
            play2 = spin1
        else:
            spin2 = np.random.choice(choices)
            print(f'Player2 spun {spin2}.')
            if spin1 + spin2 > 100:
                
                # Again we set the value to 0 if the player exceeds
                # $1.00.
                play2 = 0
                print('Player2 is over!')
            elif spin1 + spin2 < play1:
                
                # We'll use the same strategy if Player 2's two
                # spins combined are less than Player 1's score.
                play2 = 0
                print('Player2 can\'t beat Player1!')
            else:
                play2 = spin1 + spin2
                print(f'Player2 has {play2}.')
    else:
        print('Player2 must spin again.')
        spin2 = np.random.choice(choices)
        print(f'Player2 spun {spin2}.')
        if spin1 + spin2 > 100:
            play2 = 0
            print('Player2 is over!')
        elif spin1 + spin2 < play1:
            play2 = 0
            print('Player2 can\'t beat Player1!')
        else:
            play2 = spin1 + spin2
            print(f'Player2 has {play2}.')
    return play2