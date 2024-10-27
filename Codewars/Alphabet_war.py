def alphabet_war(fight):
    left_power=fight.count('s')+2*fight.count('b')+3*fight.count('p')+4*fight.count('w')
    right_power=fight.count('z')+2*fight.count('d')+3*fight.count('q')+4*fight.count('m')
    if left_power>right_power:
        return "Left side wins!"
    elif left_power<right_power:
        return "Right side wins!"
    else:
        return "Let's fight again!"
    
print(alphabet_war('z'))