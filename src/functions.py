## Functions for Analysis

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

def plyr2_defeats_plyr3(spin1, spin_again=True):
    """This function returns the probability that Player 2
    defeats Player 3, given the value of Player 2's first
    spin as input. This function assumes that Player 1 is
    out of the picture (either because of exceeding $1.00
    or by having a total less than Player 2's first spin)."""
    
    import numpy as np
    prob = 1
    if spin_again:
        plyr3_too_small = plyr3_too_small_given_first_spin_plyr2(spin1)
        plyr3_goes_over = plyr3_goes_over_given_first_spin_plyr2(spin1)
        plyr3_ties_then_loses = plyr3_ties_then_loses_given_first_spin_plyr2(spin1)
    
    else:
        plyr3_too_small = prob_plyr3_too_small(spin1)
        plyr3_goes_over = prob_plyr3_goes_over(spin1)
        plyr3_ties_then_loses = prob_plyr3_ties_then_loses(spin1)
    
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

def plyr2_ties_then_exceeds_plyr3_ties_then_loses_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 and then goes over, and
    - Player 3 ties Player 1 and then loses in a one-spin
    playoff, given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2 = spin1+spin2
        plyr3 = (spin1+spin2-1) / 40
        if spin1+spin2 > 10:
            plyr3 += 1/2
        if spin1+spin2 > 13:
            plyr3 = 0
        prob += plyr2*plyr3
    return prob / 20**4

def plyr2_ties_then_loses_plyr3_too_small_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 and then loses in a one-spin playoff, and
    - Player 3's total will be under Player 1's,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2 = 1/2
        plyr3_spin1s = np.arange(1, spin1+spin2-1)
        plyr3_addends = [spin1+spin2-1-plyr3_spin1 for plyr3_spin1 in plyr3_spin1s]
        if spin1+spin2 < 14:
            plyr3 = 0
        else:
            plyr3 = np.sum(plyr3_addends)
        prob += plyr2*plyr3
    return prob / 20**4

def plyr2_ties_then_loses_plyr3_exceeds_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 and then loses in a one-spin playoff, and
    - Player 3 exceeds $1.00,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2 = 1/2
        if spin1+spin2 < 14:
            plyr3 = 0
        else:
            plyr3_spin1s = np.arange(1, spin1+spin2)
            plyr3 = np.sum(plyr3_spin1s)
        prob += plyr2*plyr3
    return prob / 20**4

def plyr2_ties_then_loses_plyr3_ties_then_loses_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 on one spin and then loses in a
    one-spin playoff, and
    - Player 3 ties Players 1 and 2 and then loses in a
    one-spin playoff,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2 = 1/3
        if spin1+spin2 < 14:
            plyr3 = 0
        else:
            plyr3 = (spin1+spin2-1) / 20 + 1
        prob += plyr2*plyr3
    return prob / 20**3

def plyr2_ties_on2_then_loses_plyr3_too_small_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 on two spins and then loses in a
    one-spin playoff, and
    - Player 3's total will be under Player 1's,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2 = (spin1+spin2-1) / 2
        plyr3_spin1s = np.arange(1, spin1+spin2-1)
        plyr3_addends = [spin1+spin2-1-plyr3spin1 for plyr3spin1 in plyr3_spin1s]
        plyr3 = np.sum(plyr3_addends)
        prob += plyr2*plyr3
    return prob / 20**5

def plyr2_ties_on2_then_loses_plyr3_exceeds_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 on two spins and then loses in a
    one-spin playoff, and
    - Player 3 exceeds $1.00,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2 = spin1+spin2-1
        if spin1+spin2 < 14:
            plyr3_spin1s = np.arange(1, spin1+spin2+1)
        else:
            plyr3_spin1s = np.arange(1, spin1+spin2)
        plyr3 = np.sum(plyr3_spin1s)
        prob += plyr2*plyr3
    return prob / 20**5

def plyr2_ties_on2_then_loses_plyr3_ties_then_loses_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 ties Player 1 on two spins and then loses in a
    one-spin playoff, and
    - Player 3 ties Player 1 and then loses in a one-spin
    playoff,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2 = (spin1+spin2-1) / 3
        plyr3 = (spin1+spin2-1) / 20
        if spin1+spin2 > 13:
            plyr3 += 1
        prob += plyr2*plyr3
    return prob / 20**4

def plyr2_too_small_plyr3_ties_then_exceeds_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 fails to surpass Player 1's total, and
    - Player 3 ties Player 1 and then goes over $1.00,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 11-spin1):
        plyr2_spin1s = np.arange(1, spin1+spin2-1)
        plyr2_addends = [spin1+spin2-1-plyr2spin1 for plyr2spin1 in plyr2_spin1s]
        plyr2 = np.sum(plyr2_addends)
        plyr3 = spin1+spin2
        prob += plyr2*plyr3
    return prob / 20**5

def plyr2_too_small_plyr3_ties_then_loses_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 fails to surpass Player 1's total, and
    - Player 3 ties Player 1 and then loses in a one-spin
    playoff,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2_spin1s = np.arange(1, spin1+spin2-1)
        plyr2_addends = [spin1+spin2-1-plyr2spin1 for plyr2spin1 in plyr2_spin1s]
        plyr2 = np.sum(plyr2_addends) / 400
        plyr3 = (spin1+spin2-1) / 800
        if spin1+spin2 > 10:
            plyr3 += 1 / 40
        prob += plyr2*plyr3
    return prob / 20

def plyr2_exceeds_plyr3_ties_then_exceeds_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 goes over $1.00 (without first tying Player 1), and
    - Player 3 ties Player 1 and then goes over $1.00,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 11-spin1):
        plyr2_spin1s = np.arange(1, spin1+spin2)
        plyr2_spin1s_alt = np.arange(spin1+spin2+1, 11)
        plyr2 = np.sum(plyr2_spin1s) + np.sum(plyr2_spin1s_alt)
        plyr3 = spin1+spin2
        prob += plyr2*plyr3
    return prob / 20**5

def plyr2_exceeds_plyr3_ties_then_loses_given_first_spin_plyr1(spin1):
    """This function returns the probability that:
    - Player 2 goes over $1.00 (without first tying Player 1), and
    - Player 3 ties Player 1 and then loses in a one-spin
    playoff,
    given the value of Player 1's first spin as input."""
    
    import numpy as np
    prob = 0
    for spin2 in np.arange(1, 21-spin1):
        plyr2_spin1s = np.arange(1, spin1+spin2)
        plyr2_spin1s_alt = np.arange(spin1+spin2+1, 11)
        plyr2 = np.sum(plyr2_spin1s) + np.sum(plyr2_spin1s_alt)
        plyr3 = (spin1+spin2-1) / 40
        if spin1+spin2 > 10:
            plyr3 += 1 / 2
        prob += plyr2*plyr3
    return prob / 20**4

def plyr1_wins(spin1, spin_again=True):
    """This function returns the probability that Player 1
    wins, given the value of Player 1's first
    spin as input. This function assumes that Players 2 and 3
    employ optimal strategy."""
    
    import numpy as np
    win_prob = 1
    if spin_again:
        plyr2_plyr3_too_small = plyr2_and_plyr3_too_small_given_first_spin_plyr1(spin1)
        plyr2_too_small_plyr3_goes_over =\
            plyr2_too_small_and_plyr3_goes_over_given_first_spin_plyr1(spin1)
        plyr2_goes_over_plyr3_too_small =\
            plyr2_goes_over_and_plyr3_too_small_given_first_spin_plyr1(spin1)
        plyr2_plyr3_go_over = plyr2_and_plyr3_go_over_given_first_spin_plyr1(spin1)
        plyr2_ties_exceeds_plyr3_too_small =\
            plyr2_ties_then_exceeds_plyr3_too_small_given_first_spin_plyr1(spin1)
        plyr2_ties_exceeds_plyr3_exceeds =\
            plyr2_ties_then_exceeds_plyr3_exceeds_given_first_spin_plyr1(spin1)
        plyr2_ties_exceeds_plyr3_ties_loses =\
            plyr2_ties_then_exceeds_plyr3_ties_then_loses_given_first_spin_plyr1(spin1)
        plyr2_ties_loses_plyr3_too_small =\
            plyr2_ties_then_loses_plyr3_too_small_given_first_spin_plyr1(spin1)
        plyr2_ties_loses_plyr3_exceeds =\
            plyr2_ties_then_loses_plyr3_exceeds_given_first_spin_plyr1(spin1)
        plyr2_ties_loses_plyr3_ties_loses =\
            plyr2_ties_then_loses_plyr3_ties_then_loses_given_first_spin_plyr1(spin1)
        plyr2_ties_on2_loses_plyr3_too_small =\
            plyr2_ties_on2_then_loses_plyr3_too_small_given_first_spin_plyr1(spin1)
        plyr2_ties_on2_loses_plyr3_exceeds =\
            plyr2_ties_on2_then_loses_plyr3_exceeds_given_first_spin_plyr1(spin1)
        plyr2_ties_on2_loses_plyr3_ties_loses =\
            plyr2_ties_on2_then_loses_plyr3_ties_then_loses_given_first_spin_plyr1(spin1)
        plyr2_too_small_plyr3_ties_exceeds =\
            plyr2_too_small_plyr3_ties_then_exceeds_given_first_spin_plyr1(spin1)
        plyr2_too_small_plyr3_ties_loses =\
            plyr2_too_small_plyr3_ties_then_loses_given_first_spin_plyr1(spin1)
        plyr2_exceeds_plyr3_ties_exceeds =\
            plyr2_exceeds_plyr3_ties_then_exceeds_given_first_spin_plyr1(spin1)
        plyr2_exceeds_plyr3_ties_loses =\
            plyr2_exceeds_plyr3_ties_then_loses_given_first_spin_plyr1(spin1)
    
    else:
        plyr2_plyr3_too_small = prob_plyr2_and_plyr3_too_small(spin1)
        plyr2_too_small_plyr3_goes_over = plyr2_too_small_and_plyr3_goes_over(spin1)
        plyr2_goes_over_plyr3_too_small = plyr2_goes_over_and_plyr3_too_small(spin1)
        plyr2_plyr3_go_over = plyr2_and_plyr3_go_over(spin1)
        plyr2_ties_exceeds_plyr3_too_small =\
            plyr2_ties_then_exceeds_plyr3_too_small(spin1)
        plyr2_ties_exceeds_plyr3_exceeds = plyr2_ties_then_exceeds_plyr3_exceeds(spin1)
        plyr2_ties_exceeds_plyr3_ties_loses =\
            plyr2_ties_then_exceeds_plyr3_ties_then_loses(spin1)
        plyr2_ties_loses_plyr3_too_small = plyr2_ties_then_loses_plyr3_too_small(spin1)
        plyr2_ties_loses_plyr3_exceeds = plyr2_ties_then_loses_plyr3_exceeds(spin1)
        plyr2_ties_loses_plyr3_ties_loses =\
            plyr2_ties_then_loses_plyr3_ties_then_loses(spin1)
        plyr2_ties_on2_loses_plyr3_too_small =\
            plyr2_ties_on2_then_loses_plyr3_too_small(spin1)
        plyr2_ties_on2_loses_plyr3_exceeds =\
            plyr2_ties_on2_then_loses_plyr3_exceeds(spin1)
        plyr2_ties_on2_loses_plyr3_ties_loses =\
            plyr2_ties_on2_then_loses_plyr3_ties_then_loses(spin1)
        plyr2_too_small_plyr3_ties_exceeds =\
            plyr2_too_small_plyr3_ties_then_exceeds(spin1)
        plyr2_too_small_plyr3_ties_loses = plyr2_too_small_plyr3_ties_then_loses(spin1)
        plyr2_exceeds_plyr3_ties_exceeds = plyr2_exceeds_plyr3_ties_then_exceeds(spin1)
        plyr2_exceeds_plyr3_ties_loses = plyr2_exceeds_plyr3_ties_then_loses(spin1)
    
    win_prob *= (plyr2_plyr3_too_small + plyr2_too_small_plyr3_goes_over\
                 + plyr2_goes_over_plyr3_too_small + plyr2_plyr3_go_over\
                 + plyr2_ties_exceeds_plyr3_too_small\
                 + plyr2_ties_exceeds_plyr3_exceeds\
                 + plyr2_ties_exceeds_plyr3_ties_loses\
                 + plyr2_ties_loses_plyr3_too_small\
                 + plyr2_ties_loses_plyr3_exceeds\
                 + plyr2_ties_loses_plyr3_ties_loses\
                 + plyr2_ties_on2_loses_plyr3_too_small\
                 + plyr2_ties_on2_loses_plyr3_exceeds\
                 + plyr2_ties_on2_loses_plyr3_ties_loses\
                 + plyr2_too_small_plyr3_ties_exceeds\
                 + plyr2_too_small_plyr3_ties_loses\
                 + plyr2_exceeds_plyr3_ties_exceeds\
                 + plyr2_exceeds_plyr3_ties_loses)
    
    return win_prob

## Functions for Simulation

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

def third_player(play1, play2):
    """This function simulates the turn of the third person
    in the Showcase Showdown."""
    
    import numpy as np
    scores = dict(enumerate([play1, play2], start=1))
    leader = {k: v for k, v in scores.items() if v == max(scores.values())}
    leader_val = [v for v in leader.values()][0]
    if len(leader) == 2:
        print(f'Player1 and Player2 are tied at {play1}!')
    else:
        leader_num = [k for k in leader.keys()][0]
        print(f'Player{leader_num} has {leader_val}.')
    choices = [5*i for i in range(1, 21)]
    spin1 = np.random.choice(choices)
    print(f'Player3 spun {spin1}.')
    
    ## Case1. Player3 defeats the leader(s) on one spin.
    ## Note: Even in this case, Player3
    ## may spin again to go for the $1.00.
    if spin1 > leader_val:
        print(f'Does Player3 want to go for the $1.00?')
        choice = input('Yes or No: ')
        if choice == 'Yes':
            spin2 = np.random.choice(choices)
            if spin1 + spin2 > 100:
                play3 = 0
                print('Player3 is over!')
            else:
                play3 = spin1 + spin2
                print(f'Player3 wins with {play3}.')
        else:
            play3 = spin1
            print(f'Player3 wins with {play3}.')
        return play3
    
    ## Case 2. Player3 ties the leader(s).
    elif spin1 == leader_val:
        if len(leader) == 2:
            print(f'We have a three-way tie at {leader_val}!')
            print(f'Does Player3 want to spin again?')
            choice = input('Yes or No: ')
            if choice == 'Yes':
                spin2 = np.random.choice(choices)
                if spin1 + spin2 > 100:
                    play3 = 0
                    print('Player3 is over!')
                else:
                    play3 = spin1 + spin2
                    print(f'Player3 wins with {play3}.')
            else:
                print(f'Each player gets one more spin.')
                play1f = np.random.choice(choices)
                print(f'Player1 spun {play1f}.')
                play2f = np.random.choice(choices)
                print(f'Player2 spun {play2f}.')
                if play2f == play1f:
                    print('Player2 must spin again.')
                    play2f += np.random.choice(choices)
                    if play2f > 100:
                        print('Player2 is over!')
                        play2f = 0
                elif play2f < play1f:
                    play2f = 0
                else:
                    play1f = 0
                    print(f'Player2 leads with {play2f}.')
                play3f = np.random.choice(choices)
                print(f'Player3 spun {play3f}.')
                if play3f == play1f or play3f == play2f:
                    print('Player3 must spin again.')
                    play3f += np.random.choice(choices)
                    if play3f > 100:
                        print('Player3 is over!')
                        play3f = 0
                finals = dict(enumerate([play1f, play2f, play3f], start=1))
                winner = {k: v for k, v in finals.items() if v == max(finals.values())}
                print(f'The winner is {[k for k in winner.keys()][0]}!')
                return play3f
        else:
            print(f'We have a tie at {leader_val}!')
            print(f'Does Player3 want to spin again?')
            choice = input('Yes or No: ')
            if choice == 'Yes':
                spin2 = np.random.choice(choices)
                if spin1 + spin2 > 100:
                    play3 = 0
                    print('Player3 is over!')
                else:
                    play3 = spin1 + spin2
                    print(f'Player3 wins with {play3}.')
            else:
                print(f'We have a tie between Player3 and Player{leader_num}.')
                print(f'Each player gets one more spin.')
                play1f = np.random.choice(choices)
                print(f'Player{leader_num} spun {play1f}.')
                play2f = np.random.choice(choices)
                print(f'Player3 spun {play2f}.')
                if play2f == play1f:
                    print('Player3 must spin again.')
                    play2f += np.random.choice(choices)
                    if play2f > 100:
                        print('Player3 is over!')
                        play2f = 0
                elif play2f < play1f:
                    play2f = 0
                    print(f'Player3 can\'t beat Player{leader_num}!')
                else:
                    play1f = 0
                    print(f'Player3 wins with {play2f}.')
    
    ## Case 3. Player3 is under the leader(s) and must spin again.
    else:
        print('Player3 must spin again.')
        spin2 = np.random.choice(choices)
        print(f'Player3 spun {spin2}.')
        if spin1 + spin2 > 100:
            play3 = 0
            print('Player3 is over!')
        elif spin1 + spin2 < leader_val:
            play3 = 0
            print('Player3 can\'t beat Player1 and Player2!')
        else:
            play3 = spin1 + spin2
            if play3 > leader_val:
                print(f'Player3 wins with {play3}.')
            else:
                print(f'We have a tie between Player3 and Player{leader_num}.')
                print(f'Each player gets one more spin.')
                play1f = np.random.choice(choices)
                print(f'Player{leader_num} spun {play1f}.')
                play2f = np.random.choice(choices)
                print(f'Player3 spun {play2f}.')
                if play2f == play1f:
                    print('Player3 must spin again.')
                    play2f += np.random.choice(choices)
                    if play2f > 100:
                        print('Player3 is over!')
                        play2f = 0
                elif play2f < play1f:
                    play2f = 0
                    print(f'Player3 can\'t beat Player{leader_num}!')
                else:
                    play1f = 0
                    print(f'Player3 wins with {play2f}.')
        return play3
    
def play_full():
    """This function simulates a complete Showcase Showdown."""
    
    play1 = first_player()
    play2 = second_player(play1)
    play3 = third_player(play1, play2)

## Functions (and 'wheel' definition) for Statistics    

wheel = [i for i in range(5, 101, 5)]

def stats_player1(choices=wheel, spin_again=True, spin_first=None,
                 opt_strategy=False):
    """This function returns a score for Player1 with optional
    settings for a first spin, whether or not to follow the
    optimal strategy, and whether or not to spin again (the
    optimal strategy notwithstanding)."""
    
    import numpy as np
    if spin_first is None:
        spin1 = np.random.choice(choices)
    else:
        spin1 = spin_first
    if opt_strategy:
        if spin1 > 65:
            spin_again=False
        else:
            spin_again=True
    if spin_again:
        spin2 = np.random.choice(choices)
        if spin1 + spin2 > 100:
            play1 = 0
        else:
            play1 = spin1 + spin2
    else:
        play1 = spin1
    return play1

def stats_player2(play1, choices=wheel, spin_again=True, spin_first=None,
                 opt_strategy=False):
    """This function returns a score for Player2 given a score
    for Player1, with optional settings for a first spin,
    whether or not to follow the optimal strategy, and whether
    or not to spin again (the optimal strategy notwithstanding)."""
    
    import numpy as np
    if spin_first is None:
        spin1 = np.random.choice(choices)
    else:
        spin1 = spin_first
    if opt_strategy:
        if spin1 == play1:
            if play1 > 65:
                spin_again = False
        elif spin1 > 50:
            spin_again = False
        else:
            spin_again = True
    if spin1 < play1:
        spin_again = True
    if spin_again:
        spin2 = np.random.choice(choices)
        if spin1 + spin2 > 100 or spin1 + spin2 < play1:
            play2 = 0
        else:
            play2 = spin1 + spin2
    else:
        play2 = spin1
    return play2

def stats_player3(leader, tie=False, choices=wheel, spin_again=True,
                  spin_first=None, opt_strategy=False, gofordollar=False):
    """This function returns a score for Player3 given a leading
    score, with optional settings for a first spin, whether
    Players 1 and 2 are tied , whether or not to follow the
    optimal strategy, whether or not to spin again (the
    optimal strategy notwithstanding), and whether or not to
    go for a dollar (after defeating the leader(s) one one spin)."""
    
    import numpy as np
    if spin_first is None:
        spin1 = np.random.choice(choices)
    else:
        spin1 = spin_first
    if opt_strategy:
        if spin1 == leader:
            if tie:
                if leader > 65:
                    spin_again = False
                else:
                    spin_again = True
            else:
                if leader > 50:
                    spin_again = False
                else:
                    spin_again = True
    if spin1 < leader:
        spin_again = True
    if leader == 0:
        spin_again = False
    if spin1 > leader:
        if gofordollar == True:
            spin_again = True
        else:
            spin_again = False
    if spin_again:
        spin2 = np.random.choice(choices)
        if spin1 + spin2 > 100 or spin1 + spin2 < leader:
            play3 = 0
        else:
            play3 = spin1 + spin2
    else:
        play3 = spin1
    return play3

def showcase_showdown(plr1_first, plr1_again, plr2_first, plr2_again,
                      plr3_first, plr3_again, plr1os=False, plr2os=False,
                      plr3os=False, plr3gfd=False, tie=False):
    """This function simulates a complete Showcase Showdown with all
    of the options from the individual player functions above."""
    
    import numpy as np
    wheel = [i for i in range(5, 101, 5)]
    plr1 = stats_player1(spin_again=plr1_again, spin_first=plr1_first,
                        opt_strategy=plr1os)
    plr2 = stats_player2(play1=plr1, spin_again=plr2_again,
                         spin_first=plr2_first, opt_strategy=plr2os)
    if plr1 > plr2:
        leader = plr1
    else:
        leader = plr2
    plr3 = stats_player3(leader, spin_again=plr3_again,
                         spin_first=plr3_first, opt_strategy=plr3os,
                         gofordollar=plr3gfd, tie=tie)
    
    score_dict = dict(enumerate([plr1, plr2, plr3], start=1))
    
    wnr = {k: v for k, v in score_dict.items() if v == max(score_dict.values())}
    
    if len(wnr) > 1:
        return np.random.choice([k for k in wnr.keys()])
    else:
        return [k for k in wnr.keys()][0]