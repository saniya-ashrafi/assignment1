def mixString(s1, s2):
  s2 = s2[::-1]
  lengS1 = len(s1)
  lengS2 = len(s2)
  length  = lengS1 if lengS1 > lengS2 else lengS2 
  resStr=""
  for k in range(length):
    if(k < lengS1):
      resStr = resStr + s1[k]
    if(k < lengS2):
      resStr = resStr + s2[k]
    
  print(resStr)
  
s1 = "Abc"
s2 = "Xyz"
mixString(s1, s2)

