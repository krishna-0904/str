q=['1.what is the capital of india?',
    '2.what is the national animal?',
    '3.who is the hero of bahubali?',
    '4.who is rajamouli?',
    '5.where is banglore?']
ans=['delhi','tiger', 'prabhas', 'directot','karnataka']
for x in range(len(q)):
    print(q[x])
    user_ans=input('enter answer:').lower()
    if user_ans==ans[x]:
        print('correct ans')
    else:
        print('wrong ans')