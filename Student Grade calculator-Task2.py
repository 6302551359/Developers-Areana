#basic student grade claculautor
social=int(input("Enter your marks out of 100:"))
science=int(input("Enter your marks out of 100:"))
telugu=int(input("enter your marks out of 100:"))
english=int(input("enter your marks out of 100:"))
total=social+science+telugu+english
average=total/4
print( "Average:",average)
if average >= 90:
    Grade= "A"
    comment="Excellent"
elif average >= 80:
    Grade= "B"
    comment="Very good"
elif average >= 70:
    Grade="c"
    comment="good"
elif average >= 60:
    Grade ="D"
    comment="Average"
elif average >= 50:
    Grade ="E"
    comment="Just pass"
else:
    Grade="F"
    comment="Fail"
result=[total,average,Grade,comment]
print("Result=",result)
    
    


    

    


    

    


    