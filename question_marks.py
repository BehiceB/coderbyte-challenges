def QuestionsMarks(strParam):
  control = False
  x = len(strParam)
  a = list(strParam)
  for i in range(0,x-2):
    if a[i] == '?' and a[i+1] == '?' and a[i+2] == '?':
      control = True
    
  if control == True:
    return "true"
  else:
    return "false"

  # code goes here

# keep this function call here 
print(QuestionsMarks(input()))_