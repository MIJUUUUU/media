
def getGrade(score):
  if score >= 90: 
    return 'A'
  elif score < 90 and score>= 80:
    return 'B'
  
  elif score < 80 and score >=70:
    return 'C'
  
  elif score <70 and score >=60:
    return'D'
  
  else:
    return 'F'

score = int(input(""))
if score <0 or score >100:
    print(-1)
else:
    print("Your Grade is" ,getGrade(score))
