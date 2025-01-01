names="jordan,emma,lavine,warui,nyaga ,caleb"
print(names)
#create a list of the names 
names_list=["jordan","Emma","lavine","warui","nyaga","caleb"]
print(names_list)
#To find the length/no. of items in the list we use len()
print("number of items:",len(names_list))
#Selecting one item based on its index 
#note indexing starts from [0]=1st item on the list
print("second  name:",names_list[1])

#To slice out some items before or after a certain index we want to slice out,we use ":"(e.g we are taking then last two names in the list)
print("final two names:",names_list[4:])

#To delete an item we use . remove("")

names_list.remove ("warui")

print(names_list)



# to add something to the list we use .append("")
names_list.append("Mercy")
print(names_list)