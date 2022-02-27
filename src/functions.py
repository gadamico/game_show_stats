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

def plyr3_too_small_given_first_spin_plyr2(spin1):
    """This function returns the probability that Player 3's
    total will be under Player 2's total given the value of
    Player 2's first spin as input."""
    
    import numpy as np
    out = 0
    for spin2 in np.arange(1, 21-spin1):
        for z in np.arange(1, spin1+spin2-1):
            out += spin1 + spin2 - 1 - z
    return out / 8000

def plyr3_goes_over_given_first_spin_plyr2(spin1):
    """This function returns the probability that Player 3's
    total will be over $1.00 (after failing to match or exceed
    Player 2's total on the first spin), given the value of
    Player 2's first spin as input."""
    
    import numpy as np
    out = 0
    for spin2 in np.arange(1, 21-spin1):
        for z in np.arange(1, spin1+spin2):
            out += z
    return out / 8000

def plyr3_ties_then_loses_given_first_spin_plyr2(spin1):
    """This function returns the probability that Player 3
    ties Player 2 on one or two spins and then loses, either
    by exceeding $1.00 or by losing in a one-spin playoff,
    given the value of Player 2's first spin as input.
    We assume here the optimal strategy for Player 3 when
    tying Player 2 on the first spin of spinning again when
    the score is 50 cents or less and otherwise staying (and
    waiting for the one-spin playoff)."""
    
    import numpy as np
    out = 0
    start = max(11-spin1, 1)
    for spin2 in np.arange(1, 11-spin1):
        out += (spin1+spin2) / 20 + (spin1+spin2-1) / 40
    for spin2 in np.arange(start, 21-spin1):
        out += 1 / 2 + (spin1+spin2-1) / 40
    return out / 400

def plyr2_defeats_plyr3(plyr2, spin_again=True):
    """This function returns the probability that Player 2
    defeats Player 3, given the value of Player 2's first
    spin as input. This function assumes that Player 1 is
    out of the picture (either because of exceeding $1.00
    or by having a total less than Player 2's first spin."""
    
    import numpy as np
    prob = 1
    if spin_again:
        plyr3_too_small = plyr3_too_small_given_first_spin_plyr2(plyr2)
        plyr3_goes_over = plyr3_goes_over_given_first_spin_plyr2(plyr2)
        plyr3_ties_then_loses = plyr3_ties_then_loses_given_first_spin_plyr2(plyr2)
    
    else:
        plyr3_too_small = prob_plyr3_too_small(plyr2)
        plyr3_goes_over = prob_plyr3_goes_over(plyr2)
        plyr3_ties_then_loses = prob_plyr3_ties_then_loses(plyr2)
    
    prob *= (plyr3_too_small + plyr3_goes_over + plyr3_ties_then_loses)
    
    return prob

def prob_plyr2_and_plyr3_too_small(plyr1):
    """This function returns the probability that Player 2's
    total and Player 3's total  will be under Player 1's
    (input)."""
    
    import numpy as np
    plyr2spin1s = np.arange(1, plyr1-1)
    addends = [(plyr1-1-plyr2spin1) for plyr2spin1 in plyr2spin1s]
    return (np.sum(addends) / 400)**2

def plyr2_too_small_and_plyr3_goes_over(plyr1):
    """This function returns the probability that both Player 2's
    total will be under Player 1's and Player 3's will be over
    $1.00 (after failing to match or exceed Player 1's total on
    the first spin)."""
    
    import numpy as np
    prob = 1
    plyr2spin1s = np.arange(1, plyr1-1)
    addends = [(plyr1-1-plyr2spin1) for plyr2spin1 in plyr2spin1s]
    prob *= np.sum(addends) / 400
    plyr3spin1s = np.arange(1, plyr1)
    prob *= np.sum(plyr3spin1s) / 400
    return prob

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