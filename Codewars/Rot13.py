def rot13(message):
    new_message=''
    for i in message:
        if 'a'<=i<='z':
            new_message+=chr((ord(i)-ord('a')+13)%26 + ord('a'))
        elif 'A'<=i<='Z':
            new_message+=chr((ord(i)-ord('A')+13)%26+ord('A'))
        else:
            new_message+=i
    return new_message

print(rot13('test'))