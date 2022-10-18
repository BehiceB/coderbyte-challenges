def CodelandUsernameValidation(strParam):

  if (len(strParam) >=4 and len(strParam)<=25) and  strParam[len(strParam)-1] != '_':
    return "true"
  else:
    return "false"
  # code goes here
 

# keep this function call here 
print(CodelandUsernameValidation(input()))