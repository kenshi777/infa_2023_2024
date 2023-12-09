import sys

if __name__ == "__main__":
    if len (sys.argv) > 1:
        print ("Привет, {}!".format (sys.argv[1] ) )
    else:
        print ("Привет, мир!")