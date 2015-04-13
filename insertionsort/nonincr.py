
def nonincr(some_array):
	for j in range(2,len(some_array)):
		key=some_array[j]
		i=j-1
		while (i>0)& (some_array[i]>key):
			some_array[i+1]=some_array[i]
			i=i-1
		some_array[i+1]=key
	return 
