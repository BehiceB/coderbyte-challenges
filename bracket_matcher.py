def BracketMatcher(strParam):
  countLeft = 0
  countRight = 0
  # code goes here
  listA = []
  listA[:0] = strParam
  for i in range(len(listA)):
    if listA[i]== '(':
      countLeft +=1
    elif listA[i] == ')':
      countRight += 1
  if countLeft == countRight:
    return 1
  else:
    return 0

# keep this function call here 
print(BracketMatcher(input()))