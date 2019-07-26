def sortWords(wordList):
  for i in range(len(wordList)-1):
    for j in range(i+1, len(wordList)):
      if wordList[i] > wordList[j]:
        temp = wordList[i]
        wordList[i]=wordList[j]
        wordList[j]=temp
  print("Sorted words:", wordList)


a="this is something new"
tmp=""
new=[]
for i in a:
  if i==" ":
      new.append(tmp)
      tmp=""
  else:
      tmp=tmp+i
if tmp:
  new.append(tmp)
  print("Splitted sentence into words:", new)
  sortWords(new)