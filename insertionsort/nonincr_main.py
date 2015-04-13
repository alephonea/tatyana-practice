
# solution_main module implements the Application entry point and allows
# users to interact with the application.

import nonincr
import sys
		
def main():
	line = sys.stdin.readline().split(' ')
	l=list(line)
	l[-1]=l[-1].strip()
	print nonincr.nonincr(l)
		
if __name__ == '__main__':
	main()