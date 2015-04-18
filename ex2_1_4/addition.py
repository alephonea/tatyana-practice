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
  # NOTE(orlov)
  # In this implementation, you assume that high order digits come first.
  # For example, 8 = 1000 binary is represented as the following array.
  # [1, 0, 0, 0].
  # This is a very common mistake of anyone who's implementing arithmetic 
  # functions themself on the first try.
  # Instead, you should keep low order digits first. Number 8 would be
  # represented in the following way:
  # x = [0, 0, 0, 1]
  # The latter representation gives you more flexibility to do operations
  # that grow the number (you can not easily extend an array from the left),
  # but it is easier to extend it from the right.
  # It is also useful to think as x[i] to contribute 2**i * x[i] to the
  # number (in the proper representation).

	for j in range((len(a)-1),-1,-1):
    # NOTE(orlov) Why do you need taking int() from a[j] or b[j]?
		aj=int(a[j])
		bj=int(b[j])
		c=aj+bj+c
    # NOTE(orlov) c%2 is a nice optimization! 
    # Totally better than 4 comparisons. You can also do c&1 instead of
    # c&2. Try to think why.
		c_list[j+1]=c%2
    # NOTE(dnorlov) Why int()? Integer division rounds down.
    # Try "print 3/2" in python shell.
		c=int(c/2)
	c_list[0]=c
	ans_list=c_list.values()
	return ans_list 
