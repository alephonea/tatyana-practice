
# sys defines functions and objects to interact with the system.
# In our case, we need to read from program's console input (
# called "standard input"), which is defined as sys.stdin
import sys

def main():
  # This function implements an entry point.
  input_line = sys.stdin.readline()
  # You can interpret an input line as an integer
  n = int(input_line)

if __name__ == '__main__':
  # Entry point into the program here
  main()
