def BracketCombinations(num):
  
  num = (factorial(2 * num)) / (factorial(num + 1) * factorial(num))
  return int(num)
  
  
def factorial(num):
  if num > 1:
        return num * factorial(num - 1)
  else:
        return 1
# keep this function call here 
print(BracketCombinations(input()))