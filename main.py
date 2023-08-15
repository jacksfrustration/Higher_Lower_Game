import random as rand

from data import data
from art import logo,vs

score=0
q_number=0
print(logo)
while data:
    a=rand.choice(data)
    data.remove(a)
    b=rand.choice(data)
    data.remove(b)
    print(f"CHoice A: {a['name'].title()}, a {a['description'].lower()} from {a['country'].title()}")
    print(vs)
    print(f"CHoice B: {b['name'].title()}, a {b['description'].lower()} from {b['country'].title()}")
    if a['follower_count']>b['follower_count']:
        corr_ans="a".upper()
    elif a['follower_count']<b['follower_count']:
        corr_ans="b".upper()
    else:
        corr_ans="tie".upper()
    user_ans=input(f"Who has more followers?\n{a['name'].title()} or {b['name'].title()}\nAnswer 'A','B' or 'TIE'\t").upper()
    if corr_ans==user_ans:
        score+=1
        q_number+=1
        print(f"You got it right!!\nScore: {score}/{q_number}")

    else:
        q_number+=1
        print(f"You got it wrong!!\nScore: {score}/{q_number}")
print(f"Game Over!!\nYou got {score} out of {q_number}")


