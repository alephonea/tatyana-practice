
# addition_main module implements the Application entry point and allows
# users to interact with the application.

import addition
import sys
		
def main():
	a_num = sys.stdin.readline().split(' ')
	b_num = sys.stdin.readline().split(' ')
	print addition.add(a_num,b_num)
	print addition.imp_add(a_num,b_num)
		
if __name__ == '__main__':
	main()