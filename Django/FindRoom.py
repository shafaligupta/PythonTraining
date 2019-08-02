count={}
User_input = [1,1,1,1,1,2,2,2,2,2,8,8,8,8,8,10,10,10,10,10,5]
for items in User_input:
  count[items] = User_input.count(items)

minval = min(count.values())
res = [k for k, v in count.items() if v==minval]
print("The room number for driver is: ", res)
