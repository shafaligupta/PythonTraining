#Q1
x=[1,2,3,4,[10,20,30,40,[100,200,300,400],"rishabh_",5+5j],4000]

print(x[4][0],',',x[4][1])
print(x[4][6])
print(x[4][4][2],',',x[4][4][3])
print(x[4][3],',',x[4][4],',', '"{0}"'.format(x[4][5]))

#Q2
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

for i in range(0, 21):

    for j in range(i + 1, 21):

        if ((arr[i] + arr[j]) % 2 == 0):
            print("(", i, ",", j, ")", ",", "Sum", i + j, "is even")

#Q3
test_str = input("Enter the String")
spl_char = input("Enter spl characters for which frequency is req")
# "hello&*$$world"
all_freq = {}

for i in test_str:
    if ((i == spl_char) and (i in all_freq)):
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("Count of spl char is :\n " + str(all_freq))

#Q4

for i in range (1,50):
 if ((i%2!=0 and (i*i*i)<50)):
   print(i)


#Q5
list1 = [1,2,3,6,7,9,12,13,15,16,17,18,19,21,22,25,27,29,30,31,33]
list2 = list1.copy()

for i in range(0,len(list2)):
  list2[i] = list2[i]*3
print("New List is: \n",list2)
print("Original list is: \n", list1)


#Q6
x = "Hello world I am lerning python"
print([len(x) for x in x.split()])

#Q7
x= [4,7,10,23,14,37.3,46,59,61,74]
print(all(isinstance(i, (int)) for i in x))


