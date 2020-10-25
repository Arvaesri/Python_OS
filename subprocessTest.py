import subprocess
import sys

# python ./subprocessTest.py argumento2 argumento3
# ./subprocessTest.py vai ser o primeiro argv




if __name__ == "__main__":
	subprocess.run(['python','./Test.py','argument2','argument3'])
	print(sys.argv[0])
	print(sys.argv[1])
	print(sys.argv[2])
