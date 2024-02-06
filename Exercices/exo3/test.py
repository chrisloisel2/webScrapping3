import test2
import sys

print(__name__)


def main(Name = "default"):
	print(Name)
	print(__name__)

if __name__ == "__main__":
	main(sys.argv[1])
	dir(test2)


test2.bonjour()
