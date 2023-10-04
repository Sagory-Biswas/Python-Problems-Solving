'''10. Let us say your expense for every month are listed below,
 	   1. January -  2200
 	   2. February - 2350
       3. March - 2600
       4. April - 2130
       5. May - 2190

  Create a list to store these monthly expenses and using that find out,

   1. In Feb, how many dollars you spent extra compare to January?
   2. Find out your total expense in first quarter (first three months) of the year.
   3. Find out if you spent exactly 2000 dollars in any month
   4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
   5. You returned an item that you bought in a month of April and
      got a refund of 200$. Make a correction to your monthly expense list based on this'''


expenses = [2200,2350,2600,2130,2190]

print(expenses)
print("In Feb, these dollars I spent extra compare to January:", expenses[1]-expenses[0])
print("My total expenses in first quarter of the year is:", expenses[0]+expenses[1]+expenses[2])
print("Is it true?",2000 in expenses)

expenses.append(1980)
print("add my expenses of june month to our monthly expenses list:", expenses)

expenses[3]-200
print("the correction of my list is:", expenses)