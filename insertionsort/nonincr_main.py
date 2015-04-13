
# solution_main module implements the Application entry point and allows
# users to interact with the application.

import nonincr
import sys
		
def main():
	line = sys.stdin.readline()
	print nonincr.insertionsort(line)
		
if __name__ == '__main__':
	main()