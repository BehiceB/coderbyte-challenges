def MinWindowSubstring(strArr):

  lenK = len(strArr[1])
  lenN = len(strArr[0])
  K = strArr[1]
  N = strArr[0]
  while True:
    for i in range(lenK, lenN+1):
      subStr = strArr[0][i-lenK:i]
      control = True
      for char in set(list(K)): #separate the char of K
        if char not in subStr or subStr.count(char) < K.count(char):
          control = False
          break
      if control == True:
        return subStr
    lenK += 1


print(MinWindowSubstring(input()))