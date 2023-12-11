import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('name', nargs='?', default='мир')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args (sys.argv[1:])

    # print (namespace)

    print ("Привет, {}!".format (namespace.name) )