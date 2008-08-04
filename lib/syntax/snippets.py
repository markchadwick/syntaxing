SNIPPETS = {
# --------------------------------------------------------------------------
# Python
# --------------------------------------------------------------------------
'python':

"""#!/usr/bin/env python

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


# ------------------------------------------------------------------------------
# Ruby
# ------------------------------------------------------------------------------
"ruby":

"""#!/usr/bin/ruby
# Syntax Highlighting Test File for Ruby
# Some Comments about this file
# Hello World in ruby

# Keyword statement and string
puts 'Hello world'

# Function Definitions
def hello2(name)
    puts "Hello #{name}!"
end

# Class Definition
class Greeter
    def intialize(name = "World")
        @name = name
    end
    def say_hello
        puts "Hello #{@name}!"
    end
    def say_bye
        puts "Bye #{@name}, come again."
    end
end

# Keyword and some Numbers
puts 5 ** 2
""",

# ------------------------------------------------------------------------------
# C
# ------------------------------------------------------------------------------
'c':

"""/** Syntax Highlighting Test File for C
 *  \\brief Doxygen tag highlighting
 */

#include"stdlib.h"

int main()
{
    int val1 = 10;
    int val2 = val1 * 2;
    char mychar = 'A';

    for(;;) {
        val2 = val1 - 1;
        if(val <= 0) break;
    }

	printf("Hello World, %d + %d = %d", val1, val2, val1 + val2);
	printf("An unclosed string and unmatched brace
}/*End Main*/

/*EOF*/
""",

}