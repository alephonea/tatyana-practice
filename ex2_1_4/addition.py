# solution for exercise 2.1-4 adding two n-bit numbers

def add(a,b):
	c_list={}
	c=0
	for j in range((len(a)-1),-1,-1):
		aj=int(a[j])
		bj=int(b[j])
		c=aj+bj+c
		if c==0:
			c_list[j+1]=0
		elif c==1:
			c_list[j+1]=1
			c=0
		elif c==2:
			c_list[j+1]=0
			c=1
		else:
			c_list[j+1]=1
			c=1
	c_list[0]=c
	ans_list=c_list.values()
	return ans_list 

# solution for exercise 2.1-4 adding two n-bit numbers after improvment


def imp_add(a,b):
	c_list={}
	c=0
	for j in range((len(a)-1),-1,-1):
		aj=int(a[j])
		bj=int(b[j])
		c=aj+bj+c
		c_list[j+1]=c%2
		c=int(c/2)
	c_list[0]=c
	ans_list=c_list.values()
	return ans_list 
