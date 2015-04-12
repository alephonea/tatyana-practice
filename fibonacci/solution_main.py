
# solution_main module implements the Application entry point and allows
# users to interact with the application.

import solution
import sys
		
def main():
	line = sys.stdin.readline()
	n = int(line)
	print solution.fibonacci(n)
		
if __name__ == '__main__':
	main()