from string import punctuation
def LongestWord(sen):
  
  temp = ""
  strList = sen.split(" ")
  meaningWords = []
  for i in range(len(strList)):

    for word in strList[i]:
      if not any(p in word for p in punctuation):
        control = True
      else:
        control = False
    if control == True:
      meaningWords.append(strList[i])
  if len(meaningWords) == 1:
    return meaningWords[0]
  for i in range(0,len(meaningWords)-1):
    if len(meaningWords[i]) >= len(meaningWords[i+1]):
      temp += meaningWords[i]
    else:
      temp = temp
    
    i += 1
  return temp
  # code goes here
  
# keep this function call here 
print(LongestWord(input()))