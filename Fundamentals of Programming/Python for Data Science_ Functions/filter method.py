def find_pos_number(num):
	if num>0:
		return num
number_list=range(-10,10)
print(list(number_list))
postive_num_lst=list(filter(find_pos_number,number_list))
print(postive_num_lst)
