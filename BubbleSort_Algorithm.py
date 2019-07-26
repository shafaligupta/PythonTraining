def BubbleSort(wordList):
  for i in range(len(wordList)-1):
    for j in range(i+1, len(wordList)):
      if wordList[i] > wordList[j]:
        temp = wordList[i]
        wordList[i]=wordList[j]
        wordList[j]=temp
  print("Sorted Items:", wordList)

my_list = ['5', '1', '4', '2', '8']

BubbleSort(my_list)
