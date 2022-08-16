uid=[]

for n in range (int(input())):
  uid.append(input())

for i in range (len(uid)):
  #total count of digits
  numbers = sum(c.isdigit() for c in uid[i])
  #total count of uppercase
  alpha   = sum(c.isupper() for c in uid[i])
  rep = set(uid[i])
  #valid if there's no repeat and length of uid=10 and alphanumeric and digits>=3 and uppercase >=2
  if bool(len(uid[i]) > len(rep)) == False and len(uid[i])==10 and uid[i].isalnum()==True and numbers>=3 and alpha>=2:
    print("Valid")
  else:
    print("Invalid")