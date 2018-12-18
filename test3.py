import test
import sys

def aa(num):
    a,b=0,1
    for i in range(num):
        yield b
        a,b=b,a+b

if __name__ == '__main__':

    a = int(sys.argv[1])
    for b in aa(a):
        print(b)



