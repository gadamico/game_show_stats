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
    total and Player 3's total will be under Player 1's
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

def plyr2_goes_over_and_plyr3_too_small(plyr1):
    """This function returns the probability that both Player 2's
    total will be over $1.00 and Player 3's will be under
    Player 1's (after failing to match or exceed Player 1's total on
    the first spin). This function follows the optimal strategy for
    Player 2 according to which Player 2 should spin again with 50
    cents or less (even if the first spin is enough to defeat Player
    1's score)."""
    
    import numpy as np
    prob = 1
    plyr2spin1unders = np.arange(1, plyr1)
    underspins = np.sum(plyr2spin1unders)
    plyr2spin1overs = np.arange(plyr1+1, 11)
    overspins = np.sum(plyr2spin1overs)
    prob *= np.sum((underspins, overspins)) / 400
    plyr3spin1s = np.arange(1, plyr1-1)
    addends = [(plyr1-1-plyr3spin1) for plyr3spin1 in plyr3spin1s]
    prob *= np.sum(addends) / 400
    return prob

def plyr2_and_plyr3_go_over(plyr1):
    """This function returns the probability that both Player 2's
    and Player 3's totals will be over $1.00. This function follows
    the optimal strategy for Player 2 according to which Player 2
    should spin again with 50 cents or less (even if the first spin
    is enough to defeat Player 1's score)."""
    
    import numpy as np
    prob = 1
    plyr2spin1unders = np.arange(1, plyr1)
    underspins = np.sum(plyr2spin1unders)
    plyr2spin1overs = np.arange(plyr1+1, 11)
    overspins = np.sum(plyr2spin1overs)
    prob *= np.sum((underspins, overspins)) / 400
    plyr3spin1s = np.arange(1, plyr1)
    prob *= np.sum(plyr3spin1s) / 400
    return prob

def plyr2_ties_plyr1_stays_then_wins(plyr1):
    """This function returns the probability that Player 2
    wins by tying Player 1 on the first spin and then staying."""
    
    import numpy as np
    prob = 0.05
    plyr3spin1s = np.arange(1, plyr1-1)
    too_small_addends = [(plyr1 - 1 - plyr3spin1) for plyr3spin1 in plyr3spin1s]
    plyr3_too_small = np.sum(too_small_addends)
    if plyr1 <= 13:
        plyr3spin1s_alt = np.arange(1, plyr1+1)
        plyr3_too_big = np.sum(plyr3spin1s_alt)
    
        plyr3_ties = (plyr1-1)
    
        prob *= (plyr3_too_small + plyr3_too_big) / 800 + plyr3_ties / 1200
    
    else:
        plyr3spin1s_alt = np.arange(1, plyr1)
        plyr3_too_big = np.sum(plyr3spin1s_alt)
        
        plyr3_ties = (plyr1-1) / 20 + 1
        
        prob *= (plyr3_too_small + plyr3_too_big) / 800 + plyr3_ties / 60
    
    return prob

def plyr2_ties_plyr1_spins_again_then_wins(plyr1):
    """This function returns the probability that Player 2
    wins by tying Player 1 on the first spin and then spinning
    again."""
    
    import numpy as np
    prob = 0
    plyr2spin2s = np.arange(1, 21-plyr1)
    
    for plyr2spin2 in plyr2spin2s:
        plyr3spin1s = np.arange(1, plyr1+plyr2spin2-1)
        too_small_addends = [(plyr1 + plyr2spin2 - 1 - plyr3spin1)\
                             for plyr3spin1 in plyr3spin1s]
        plyr3_too_small = np.sum(too_small_addends) / 400
        
        plyr3spin1s_alt = np.arange(1, plyr1+plyr2spin2)
        plyr3_too_big = np.sum(plyr3spin1s_alt) / 400
    
        plyr3_ties_two_spins = (plyr1 + plyr2spin2 - 1) / 800
        
        if plyr1 + plyr2spin2 <= 10:
            plyr3_ties_one_spin = (plyr1 + plyr2spin2) / 800
    
        else:
            plyr3_ties_one_spin = 1 / 40
        
        prob += (plyr3_too_small + plyr3_too_big\
                     + plyr3_ties_two_spins + plyr3_ties_one_spin)
   
    prob *= 1 / 400
    
    return prob

def plyr2_ties_then_exceeds_plyr3_too_small(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties then goes over $1.00
    - Player 3 fails to surpass Player 1's score."""
    
    import numpy as np
    if plyr1 > 13:
        return 0
    else:
        prob = plyr1 / 400
        plyr3spin1s = np.arange(1, plyr1-1)
        addends = [(plyr1 - 1 - plyr3spin1) for plyr3spin1 in plyr3spin1s]
        prob *= np.sum(addends) / 400
        return prob

def plyr2_ties_then_exceeds_plyr3_exceeds(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties then goes over $1.00
    - Player 3 goes over $1.00."""
    
    import numpy as np
    prob = plyr1 / 400
    if plyr1 <= 10:
        plyr3spin1s = np.arange(1, plyr1+1)
        prob *= np.sum(plyr3spin1s) / 400
    elif plyr1 < 14:
        plyr3spin1s = np.arange(1, plyr1)
        prob *= np.sum(plyr3spin1s) / 400
    else:
        prob = 0
    return prob

def plyr2_ties_then_exceeds_plyr3_ties_then_loses(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties then goes over $1.00
    - Player 3 ties then loses to Player 1 in a one-spin
    playoff."""
    
    prob = plyr1 / 400
    if plyr1 <= 10:
        prob *= (plyr1 - 1) / 800
    elif plyr1 < 14:
        prob *= (1 / 40 + (plyr1 - 1) / 800)
    else:
        prob = 0
    return prob

def plyr2_ties_then_loses_plyr3_too_small(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties, stays, then loses to Player 1 in a
    one-spin playoff
    - Player 3 fails to surpass Player 1's score."""
    
    import numpy as np
    if plyr1 < 14:
        return 0
    plyr3spin1s = np.arange(1, plyr1-1)
    addends = [(plyr1 - 1 - plyr3spin1) for plyr3spin1 in plyr3spin1s]
    return np.sum(addends) / 16000

def plyr2_ties_then_loses_plyr3_exceeds(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties, stays, then loses to Player 1 in a
    one-spin playoff
    - Player 3 ties goes over $1.00."""
    
    import numpy as np
    if plyr1 < 14:
        return 0
    else:
        plyr3spin1s = np.arange(1, plyr1)
        return np.sum(plyr3spin1s) / 16000
    
def plyr2_ties_then_loses_plyr3_ties_then_loses(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties, stays, then loses to Player 1 in a
    one-spin playoff
    - Player 3 ties then loses to Player 1 in a one-spin
    playoff."""
    
    if plyr1 < 14:
        return 0
    else:
        return 1 / 60 * (1 / 20 + (plyr1-1) / 400)
    
def plyr2_ties_on2_then_loses_plyr3_too_small(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties Player 1 on two spins, then loses to
    Player 1 in a one-spin playoff
    - Player 3 fails to surpass Player 1's score."""
    
    import numpy as np
    prob = (plyr1-1) / 400
    plyr3spin1s = np.arange(1, plyr1-1)
    addends = [(plyr1 - 1 - plyr3spin1) for plyr3spin1 in plyr3spin1s]
    prob *= np.sum(addends) / 800
    return prob

def plyr2_ties_on2_then_loses_plyr3_exceeds(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties Player 1 on two spins, then loses to
    Player 1 in a one-spin playoff
    - Player 3 goes over $1.00."""
    
    import numpy as np
    prob = (plyr1 - 1) / 400
    if plyr1 < 13:
        limit = plyr1+1
    else:
        limit = plyr1
    plyr3spin1s = np.arange(1, limit)
    prob *= np.sum(plyr3spin1s) / 400
    return prob

def plyr2_ties_on2_then_loses_plyr3_ties_then_loses(plyr1):
    """This function returns the probability that Player 1
    wins after:
    - Player 2 ties Player 1 on two spins, then loses to Player 1 in a
    one-spin playoff
    - Player 3 ties then loses to Player 1 in a one-spin
    playoff."""
    
    prob = (plyr1-1) / 400
    if plyr1 < 13:
        prob *= (plyr1-1) / 1200
    else:
        prob *= (1 / 60 + (plyr1-1) / 1200)
    return prob

def plyr2_too_small_plyr3_ties_then_exceeds(plyr1): 
    """This function returns the probability that Player 1
    wins after:
    - Player 2 fails to surpass Player 1's score
    - Player 3 ties then goes over $1.00."""
    
    import numpy as np
    if plyr1 > 10:
        prob = 0
    else:
        plyr2spin1s = np.arange(1, plyr1-1)
        addends = [(plyr1-1-plyr2spin1) for plyr2spin1 in plyr2spin1s]
        prob = np.sum(addends) / 400
        prob *= plyr1 / 400
    return prob

def plyr2_too_small_plyr3_ties_then_loses(plyr1): 
    """This function returns the probability that Player 1
    wins after:
    - Player 2 fails to surpass Player 1's score
    - Player 3 ties then loses to Player 1 in a one-spin
    playoff."""
    
    import numpy as np
    plyr2spin1s = np.arange(1, plyr1-1)
    addends = [(plyr1-1-plyr2spin1) for plyr2spin1 in plyr2spin1s]
    prob = np.sum(addends) / 400
    plyr3_prob = (plyr1 - 1) / 800
    if plyr1 > 10:
        plyr3_prob += 1 / 40
    prob *= plyr3_prob
    return prob

def plyr2_exceeds_plyr3_ties_then_exceeds(plyr1): 
    """This function returns the probability that Player 1
    wins after:
    - Player 2 goes over $1.00
    - Player 3 ties then goes over $1.00."""
    
    import numpy as np
    if plyr1 > 10:
        return 0
    plyr2spin1s = np.arange(1, plyr1)
    prob = np.sum(plyr2spin1s) / 400
    plyr2spin1alts = np.arange(plyr1+1, 11)
    prob += np.sum(plyr2spin1alts) / 400
    plyr3_prob = plyr1 / 400
    prob *= plyr3_prob
    return prob

def plyr2_exceeds_plyr3_ties_then_loses(plyr1): 
    """This function returns the probability that Player 1
    wins after:
    - Player 2 goes over $1.00
    - Player 3 ties then loses to Player 1 in a one-spin
    playoff."""
    
    import numpy as np
    plyr2spin1s = np.arange(1, plyr1)
    prob = np.sum(plyr2spin1s) / 400
    plyr2spin1alts = np.arange(plyr1+1, 11)
    prob += np.sum(plyr2spin1alts) / 400
    plyr3_prob = (plyr1 - 1) / 800
    if plyr1 > 10:
        plyr3_prob += 1 / 40
    prob *= plyr3_prob
    return prob

def plyr2_and_plyr3_too_small_given_first_spin_plyr1(spin1):
    """This function returns the probability that Player 2's
    total and Player 3's total will be under Player 1's,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2spin1s = np.arange(1, spin1+spin2-1)
        addends_plyr2 = [(spin1+spin2-1-plyr2spin1) for plyr2spin1 in plyr2spin1s]
        prob += (np.sum(addends_plyr2))**2
    return prob / 20**5

def plyr2_too_small_and_plyr3_goes_over_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2's total will be under Player 1's, and
    - Player 3 will go over $1.00 (without first tying),
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2spin1s = np.arange(1, spin1+spin2-1)
        addends_plyr2 = [(spin1+spin2-1-plyr2spin1) for plyr2spin1 in plyr2spin1s]
        plyr2 = np.sum(addends_plyr2)
        plyr3spin1s = np.arange(1, spin1+spin2)
        plyr3 = np.sum(plyr3spin1s)
        prob += plyr2*plyr3
    return prob / 20**5

def plyr2_goes_over_and_plyr3_too_small_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 will go over $1.00 (without first tying), and
    - Player 3's total will be under Player 1's,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2spin1s = np.arange(1, spin1+spin2)
        first_addends_plyr2 = np.sum(plyr2spin1s)
        plyr2spin1s_alt = np.arange(spin1+spin2+1, 11)
        second_addends_plyr2 = np.sum(plyr2spin1s_alt)
        plyr2 = first_addends_plyr2 + second_addends_plyr2
        plyr3spin1s = np.arange(1, spin1+spin2-1)
        addends_plyr3 = [(spin1+spin2-1-plyr3spin1) for plyr3spin1 in plyr3spin1s]        
        plyr3 = np.sum(addends_plyr3)
        prob += plyr2*plyr3
    return prob / 20**5

def plyr2_and_plyr3_go_over_given_first_spin_plyr1(spin1):
    """This function returns the probability that Player 2
    and Player 3 will both go over $1.00 (without first tying),
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2spin1s = np.arange(1, spin1+spin2)
        first_addends_plyr2 = np.sum(plyr2spin1s)
        plyr2spin1s_alt = np.arange(spin1+spin2+1, 11)
        second_addends_plyr2 = np.sum(plyr2spin1s_alt)
        plyr2 = first_addends_plyr2 + second_addends_plyr2
        plyr3spin1s = np.arange(1, spin1+spin2)
        plyr3 = np.sum(plyr3spin1s)
        prob += plyr2*plyr3
    return prob / 20**5

def plyr2_ties_then_exceeds_plyr3_too_small_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 and then goes over, and
    - Player 3's total will be under Player 1's,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 14-spin1):
        plyr2 = spin1+spin2
        plyr3_spin1s = np.arange(1, spin1+spin2-1)
        plyr3_addends = [spin1+spin2-1-plyr3spin1 for plyr3spin1 in plyr3_spin1s]
        plyr3 = np.sum(plyr3_addends)
        prob += plyr2*plyr3
    return prob / 20**5

def plyr2_ties_then_exceeds_plyr3_exceeds_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 and then goes over, and
    - Player 3 goes over,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2 = spin1+spin2
        if spin1 + spin2 < 11:
            plyr3_spin1s = np.arange(1, spin1+spin2+1)
        elif spin1 + spin2 < 13:
            plyr3_spin1s = np.arange(1, spin1+spin2)
        else:
            plyr3_spin1s = 0
        plyr3 = np.sum(plyr3_spin1s)
        prob += plyr2*plyr3
    return prob / 20**5

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
    if play1 > 0:
        print(f'Player1 has {play1}.')
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