SNIPPETS = {
    #
    # Python
    #
    'python':   """#!/usr/bin/env python

import os
import sys

class Greeter(object):
    def __init__(self, greets):
        self.greets = greets
    
    def say_hello(self):
        return "Hello %s" % self.greets

@decorator
def main(args):
    g = Greeter("World")
    print g.say_hello() * 3

if __name__ == '__main__':
    sys.exit(main(sys.argv))

""",

    #
    # C
    #
    'c':        """include <stdio.h>

int main(int argc, char *argv) {
    printf("Hello world!\n");
}""",

}