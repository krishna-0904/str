corr_ans=0
incorr_ans=0
print("1.what is the capital of india?")
user_ans=input("enter answer:").lower()
print(user_ans)
if user_ans=="delhi":
    corr_ans+=1
    print("correct answer")
else:
    incorr_ans+=1
    print("incorrect answer")
print("percentage",((corr_ans/(corr_ans+incorr_ans))*100))