def high(x):
    words=x.split()
    max_score=0
    best_word=""
    for word in words:
        score=0
        for char in word:
            score+=ord(char)-ord('a')+1
        if score>max_score:
            max_score=score
            best_word=word
    return best_word

print(high('man i need a taxi up to ubud'))