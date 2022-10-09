''' Write a script which accepts two sequences of comma-separated colors from user. 
	Then print out a set containing all the colors from color_list_1 which are not 
	present in color_list_2. '''


def colors (color_list_1, color_list_2):
	return print(list(set(color_list_1) - set(color_list_2)))
	
		
color_list_1 = ['black', 'green', 'blue']
color_list_2 = ['red', 'black', 'yellow']

colors(color_list_1, color_list_2)