import sys

def default():
	name=input("what is your name? ")
	print('Hello', name)

def cat():
	print('Meow')

def dog(): 
	print("Woof!")

def main():
	print('debug print')
	if sys.argv[1] == 'dog':
		dog()
	elif sys.argv[1] == 'cat':
		cat()
	else:
		default()

if __name__ == '__main__':
	main()
