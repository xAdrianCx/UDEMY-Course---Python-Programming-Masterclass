shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]


## Don't print specific item from list.
# for item in shopping_list:
# 	if item != "spam":
# 		print("Buy " + item)


# # Skipping an item from printing using 'continue'.
# for item in shopping_list:
# 	if item == "spam":
# 		continue
#
# 	print("Buy " + item)

item_to_find = "spam"
found_at = None

# # Skip printing the rest of the list using 'break'(break out of the loop).
# for index in range(len(shopping_list)):
# 	if shopping_list[index] == item_to_find:
# 		found_at = index
# 		break

# Does the same as the above code
if item_to_find in shopping_list:
	found_at = shopping_list.index(item_to_find)

if found_at is not None:
	print("Item found at position: {}".format(found_at))
else:
	print("{} not found".format(item_to_find))
	
	
	