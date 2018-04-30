#!/usr/bin/env python
# code co argcount should return 1 instead of 0
# python 3.6.4 default March 23, 2018


def test_arg(aFunction):
    funcName = aFunction.__code__.co_name
    numArgs = aFunction.__code__.co_argcount
    print(funcName)
    print(numArgs)

def myFunction(*arg):
    print(arg)

if __name__ == "__main__":
    test_arg(myFunction)