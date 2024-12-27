def construct(n,l):
	arr = [n,]
	length_of_arr = 1
	no_of_nodes = (2**l) - 1
	i = 0
	while(length_of_arr<no_of_nodes):
		ele=arr[i]
		new = 2*ele + 1
		arr.append(new)
		arr.append(new+1)
		i += 1
		length_of_arr += 2
	return arr

def minmax(arr,l,mode):
	if(l==0):
		return arr
	length = (2**(l+1)) - 1
	no = 2**l
	start = length - no
	for i in range(start,length,2):
		if(mode == 1):
			arr[i//2] = max(arr[i],arr[i+1])
		else:
			arr[i//2] = min(arr[i],arr[i+1])
	if(mode == 1):
		return minmax(arr,l-1,0)
	else:
		return minmax(arr,l-1,1)
	

n = int(input("Enter start number: "))
l = int(input("Enter number of levels: "))
arr = construct(n,l+1)
print(arr)
print(minmax(arr,l,1))

