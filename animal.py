import sys

def default():
	name=input("what is your name? ")
	print('Hello', name)

def dog(): 
	print("Woof")

def main():
	if sys.argv[1] == 'dog':
		dog()
	else:
		default()

if __name__ == '__main__':
	main()
