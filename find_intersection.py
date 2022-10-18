def FindIntersection(strArr):
  s1 = ""
  listIntersection = []
  list1= strArr[0]
  list2 = strArr[1]
  list1 = list1.split(',')
  list2 = list2.split(',')
  x = len(list1)
  y = len(list2)
  for i in range(0,x):
    for j in range(0,y):
      if list1[i] == list2[j]:
        listIntersection.append(list1[i].strip())
  listIntersection = ",".join(listIntersection)
  return listIntersection

# keep this function call here 
print(FindIntersection(input()))