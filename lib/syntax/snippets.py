SNIPPETS = {
# ------------------------------------------------------------------------------
# Bash
# ------------------------------------------------------------------------------
'bash':
"""# Syntax Highlighting Test File for Bash
# Comment Line

# Test Assignment
BLUE="[34;01m"
CYAN="[36;01m"
GREEN="[32;01m"
RED="[31;01m"
YELLOW="[33;01m"
OFF="[0m"

echo "${YELLOW}**${OFF} Hello World in Yellow ${YELLOW}**${OFF}"
sleep 2

# Test Scalar
HELLO=$(Hello)
HELLO2=${Hello}
HELLO3=`Hello`

# Test Loop/Condition
if [ 'a' == 'a' ]; then
    for file in $( ls ); do
        echo $file
    done
fi

# Test Function Definition
function quit {
    exit
}

# Here Statement
cat <<EOF
This is a multiline block for testing the
highlighting of a here statement
EOF
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

# ------------------------------------------------------------------------------
# C++
# ------------------------------------------------------------------------------

'c++': 

"""/** Syntax Highlighting test file for C++
 *  \brief Doxygen tag highlighing
 */
#include<iostream>
#include<cstdlib>

using namespace std;

int main(void)
{
    cout << "\nHello World" << endl;
    cout << "\nUnclosed String << endl;

    // One line comment
    int a = 0;
    
    exit(a);
}

int add(int x, int y)
{
    return x + y;
}

// EOF
""",

# ------------------------------------------------------------------------------
# Diff
# ------------------------------------------------------------------------------

'diff': """--- Syntax Highlighting Test File for Diff results
--- Comment Lines are like this
--- cpp.cpp     2007-06-26 07:14:22.000000000 -0500
+++ hello_diff.cpp      2007-08-06 17:01:47.000000000 -0500
@@ -2,24 +2,29 @@
  *
  */
 #include<iostream>
-#include<cstdlib>
 
 using namespace std;
 
 int main(void)
 {
-    cout << "\nHello World" << endl;
+    cout << "\nHello World!" << endl;
     cout << "\nUnclosed String << endl;
 
     // One line comment
     int a = 0;
-    
-    exit(a);
+    cout << add(a, 22) << endl;
 }
 
-int add(x, y)
+// Add two numbers
+int add(int x, int y)
 {
     return x + y;
 }
 
+// Subtract two numbers
+int sub(int x, int y)
+{
+    return x - y;
+}
+
 // EOF""",

# ------------------------------------------------------------------------------
# Erlang
# ------------------------------------------------------------------------------
'erlang': """%% Syntax Highlighting Test file for Erlang
%% Some comments about this file

%% quicksort:qsort(List)
%% Sort a list of items
-module(quicksort).
-export([qsort/1]).

qsort([]) -> [];
qsort([Pivot|Rest]) ->
    qsort([ X || X <- Rest, X < Pivot]) ++ [Pivot] ++ qsort([ Y || Y <- Rest, Y >= Pivot]).

%% --------------------------------------------------------------------- %%
%% Sort a list by length
-module(listsort).
-export([by_length/1]).

by_length(Lists) ->
    F = fun(A,B) when is_list(A), is_list(B) ->
            length(A) < length(B)
        end,
    qsort(Lists, F).

 qsort([], _)-> [];
 qsort([Pivot|Rest], Smaller) ->
     qsort([ X || X <- Rest, Smaller(X,Pivot)], Smaller)
     ++ [Pivot] ++
     qsort([ Y ||Y- Rest, not(Smaller(Y, Pivot))], Smaller).
""",

# ------------------------------------------------------------------------------
# Haskell
# ------------------------------------------------------------------------------

'haskell': """-- Syntax Highlighting test file for Haskell
-- Some comments about this file

-- Hello World in Haskell
putStrLn "Hello, Haskell"

-- Simple do structure
do putStrLn "What is 2 + 2?"
    x <- readLn
    if x == 4
      then putStrLn "You're right!"
      else putStrLn "You're wrong!"

-- Class def
class Num a  where
    (+)    :: a -> a -> a
    negate :: a -> a

-- Data Declaration
data Set a = NilSet 
           | ConsSet a (Set a)

-- Import statement
import somthing

-- Instance
instance Num Int  where
    x + y       =  addInt x y
    negate x    =  negateInt x

-- Module
module Tree ( Tree(Leaf,Branch), fringe ) where
 
data Tree a                = Leaf a | Branch (Tree a) (Tree a) 
 
fringe :: Tree a -> [a]
fringe (Leaf x)            = [x]
fringe (Branch left right) = fringe left ++ fringe right
""",

# ------------------------------------------------------------------------------
# HTML
# ------------------------------------------------------------------------------
'html': """<!-- Syntax Highlighting Test File for Html -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
   <head>
    <!-- Some Comments about this file -->
    <title>Hello World</title>
    <link href="hello.css" rel="stylesheet" type="text/css">
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
        <script language="JavaScript" type="text/JavaScript">
        <!-- Some Embedded JavaScript --!>
        <!--
        function MM_swapImgRestore() { //v3.0
        var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
        }
        //-->
        </script>
   </head>
   <body>
       <div>
        <h1>Hello World HTML</h1>
        <p class="bigHello">HELLO HELLO HELLO</p>
       </div>
   </body>
</html>
""",

# ------------------------------------------------------------------------------
# Java
# ------------------------------------------------------------------------------
'java': """// Syntax Highlighting Test File For Java
// Comment Line

/*
 * HelloWorld Using Swing
 */
import javax.swing.*;        

public class HelloWorldSwing {
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("HelloWorldSwing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the ubiquitous "Hello World" label.
        JLabel label = new JLabel("Hello World");
        frame.getContentPane().add(label);

        //Display the window.
        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}
""",

# ------------------------------------------------------------------------------
# JavaScript
# ------------------------------------------------------------------------------
'javascript': """// Syntax Highlighting Test File for JavaScript
// Some Comments about this file

function HelloAlert ()
{
    alert("Hello World!")
}

function count(to)
{
    for (i = 0; i <= to; i++)
    {
        document.write("The number is " + i)
        document.write("<br />")
    }
}
""",

# ------------------------------------------------------------------------------
# Common Lisp
# ------------------------------------------------------------------------------
'common-lisp': """; Syntax Highlighting Test File for Lisp
; Comment Line

; Lisp funciton and keyword test
(defpackage :mypackage
  (:use :common-lisp :cffi))

; hello version 1
(defun hello-word1 ()
  (print (list 'HELLO 'WORLD)))

; hello version 2
(defun hello-world ()
  (format t "hello world~%"))

; Lets do some factorials too
(defun factorial (N)
  (if (= N 1)
      1
    (* N (factorial (- N 1)))))

; Fibonacci numbers are fun too
(defun fibonacci (N)
  (if (or (zerop N) (= N 1))
      1
    (+ (fibonacci (- N 1)) (fibonacci (- N 2)))))
""",

# ------------------------------------------------------------------------------
# Makefile
# ------------------------------------------------------------------------------
'makefile': """# Syntax Highlighting Test File for Makefile
# Some more comments about this file

# Some Identifiers and Preproccessor stuff
!ifndef DEBUG
CFLAGS=-DDEBUG -g $(CFLAGS)
!else
CFLAGS=-Os $(CFLAGS)
!endif

# Some Targets
helloworld: helloworld.o
		cc -o $@ $<

helloworld.o: helloworld.c
		cc -c -o $@ $<

.PHONY: clean
clean:
		rm -f helloworld helloworld.o *~ core
""",

# ------------------------------------------------------------------------------
# Matlab
# ------------------------------------------------------------------------------
'matlab': """% Syntax Highlight Test File for MatLab
% Some comments about this file

% HelloWorld in MatLab
disp('Hello World');

% And now some other randomness to test different color regions
for j=1:4,
   j
end

A = 1;   B = [];
if(A|B) disp 'The statement is true',  end;

% Plotting Polynomials
x=[27.7 28 29 30];
a=[4.1 4.3 4.1];
b=[0.749 0.503 -0.781];
c=[0.0 -0.819 -0.470];
d=[-0.910 0.116 0.157];

for i=1:3
   ['p_' num2str(i) '(x) = ' num2str(a(i)) ' + ' ...
         num2str(b(i)) ' (x - ' num2str(x(i)) ') + ' ...
         num2str(c(i)) ' (x - ' num2str(x(i)) ')^2 + ' ...
         num2str(d(i)) ' (x - ' num2str(x(i)) ')^3']
end;

%---------------------------------------------------------------------
function y = nev(xx,n,x,Q)
% NEV   Neville's algorithm as a function
%       y= nev(xx,n,x,Q)
%
% inputs:
%    n = order of interpolation (n+1 = # of points)
%    x(1),...,x(n+1)    x coords
%    Q(1),...,Q(n+1)    y coords
%    xx=evaluation point for interpolating polynomial p
%
% output:  p(xx)
for i = n:-1:1
   for j = 1:i
      Q(j) = (xx-x(j))*Q(j+1) - (xx-x(j+n+1-i))*Q(j);
      Q(j) = Q(j)/(x(j+n+1-i)-x(j));
   end
end

y = Q(1);

%---------------------------------------------------------------------
function ssum = geom(a,N)
  n=0:N;
  ssum = sum(a.^n);
end
""",

# ------------------------------------------------------------------------------
# PHP
# ------------------------------------------------------------------------------
'php': """<?php
    // Syntax Highlighting Test File for PHP
    /* Some comments about this file */
    // Comment line
    $hello = "HELLO"
    $world = "WORLD"

    include_once($hello_root_path . 'hellolib.php');

    function print_mood()
    {
        switch($_GET['friendly'])
        {
            case "yes":
                echo "<h1>$hello $world</h1>";
                break;
            case "no":
                echo "<h1>Bah!!</h1>"
                break;
            default:
                echo "<h1>$hello???</h1>";
        } 
    }

    /* Class Definition Test */
    class Foo
    {
        var $myvalue;

        function bar()
        {
            if (isset($this))
            {
                echo '$this is defined (';
                echo get_class($this);
                echo ")\n";
            } else {
                echo "\$this is not defined.\n";
            }
        }
        function helloA(param) {
            echo "$param";
        }

    }

    function hello(param) {
        echo "$param";
    }
?>

<html>
   <head>
      <!-- Some Embedded HTML -->
      <title>Hello.php</title>
   </head>
   <body>
      <div>
        <p>Today is <?php disp_date() ?> and this website says <?php print_mood() ?></p>
      </div>
   </body>
</html>
""",

# ------------------------------------------------------------------------------
# Perl
# ------------------------------------------------------------------------------
'perl': """#!/usr/bin/perl
# Syntax Highlighting test file for Perl
# Some comments about this file

# Hello world in Perl
print "Hello, world!\n";

# Numerous other style region tests

# Number
$number1 = 42;

# String Tests
$answer = "The answer is $number1";  # Variable interpolation
$h1  = "Hello World \"Perl\""; # Double quoted string
$h2  = 'Hello World "Perl"';  # Single Quoted String
$h3  = qq(Hello World "Perl"); # qq() instead of quotes
$multilined_string =<<EOF
A multilined string that is terminated with
with the word "EOF"
EOF

# Array
@greetings = ('Hello', 'Holla', 'Konichiwa');

# Hash Table
%translate = (
    Hello => 'Hola',
    Bye => 'Adios'
);
print $translate[Hello];

=item B<function1>

This is a POD doc section

=cut
sub function1 { 
  my %args = @_;
  print "Joe said '$args{Joe}'\n";
}
function1( Joe => "Hello World" );

# Some Regular Expressions
$x =~ m/abc/
$x =~ s/abc/aBc/;   # substitute lowercase b with uppercase B
""",

# ------------------------------------------------------------------------------
# Plain Text
# ------------------------------------------------------------------------------
'text': """Here is some plain text to test the editor with highlighting in an in active state. This is rather boring isn't it?

Hello World
""",

# ------------------------------------------------------------------------------
# Python
# ------------------------------------------------------------------------------
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
# SQL
# ------------------------------------------------------------------------------
'sql': """/******************************************
* Syntax Highlighting Test File for SQL   *
* Multi-Line Comment Block                *
* Oracle 9i SQL                           *
*******************************************/
--- Single Line Comments are like this

--- Drop all tables, in case they were previously created ---
DROP TABLE shipment;
DROP TABLE customer;
DROP TABLE truck;
DROP TABLE city;

--- Create the customer table ---
CREATE TABLE customer
(
	CUS_ID	     Char(4) CONSTRAINT cus_id_pk PRIMARY KEY,
	CUS_LNAME    Varchar2(20),
	CUS_FNAME    Varchar2(20),
	ANN_REVENUE  Number(12,2),
	CUS_TYPE     Char(1)
);

--- Create the truck table ---
CREATE TABLE truck
(
	TRUCK_ID     Char(4)	   CONSTRAINT truck_id_pk PRIMARY KEY,
	DRIVER_NAME  Varchar2(40)
);

--- Create the city table ---
CREATE TABLE city
(
	CITY_ID	     Varchar2(4)   CONSTRAINT city_id_pk PRIMARY KEY,
	CITY_NAME    Varchar2(30),
	CITY_STATE   Char(2),
	POPULATION   Number(10)
);

--- Create the shipment table ---
CREATE TABLE shipment
(
   SHIPMENT_ID Char(4)	   CONSTRAINT ship_id_pk PRIMARY KEY,
   CUS_ID      Char(4)	   CONSTRAINT cust_id_fk REFERENCES customer(cus_id),
   WEIGHT      Number(12,2),
   TRUCK_ID    Char(4)	   CONSTRAINT truck_id_fk REFERENCES truck(truck_id),
   CITY_ID     Varchar2(4) CONSTRAINT city_id_fk  REFERENCES city(city_id),
   SHIP_DATE   DATE
);

--- Insert records into customer table ---
INSERT INTO customer VALUES
	('C101','Smith','Joe',3000000.3,'P');
INSERT INTO customer VALUES
	('C102','Sneider','Jenny',7000000.5,'P');
INSERT INTO customer VALUES
	('C103','Robinson','Dan',1000000.8,'C');
COMMIT;

--- Insert records into truck table ---
INSERT INTO truck VALUES
	('T101','Dan Brun');
INSERT INTO truck VALUES
	('T102','Bob Lee');
INSERT INTO truck VALUES
	('T104','Jerry Carlson');
INSERT INTO truck VALUES
	('T103','Frank Hong');
COMMIT;

--- Insert records into city table ---
INSERT INTO city VALUES
	('101','Dekalb','IL',50000);
INSERT INTO city VALUES
	('201','Lincoln','NE',160000);
INSERT INTO city VALUES
	('301','Houston','TX',800000);
INSERT INTO city VALUES
	('401','Laredo','TX',260000);
COMMIT;

--- Insert records into shipment table ---
INSERT INTO shipment VALUES
	('2001','C101',2500.2,'T101','101','12-Apr-2002');
INSERT INTO shipment VALUES
	('2002','C102',7500.7,'T101','201','20-Apr-2002');
INSERT INTO shipment VALUES
	('2003','C103',800000.8,'T103','201','25-May-2002');
INSERT INTO shipment VALUES
	('2004','C102',95.00,'T102','301','02-May-2003');
INSERT INTO shipment VALUES
	('2005','C101',85.00,'T102','401','02-May-2003');
COMMIT;

--- Queries 1 - 10 ---

--- How many shipments between 1/1/02 & 5/1/03?
--- Version 1 shows all records between the given dates
SELECT *
FROM   shipment
WHERE  SHIP_DATE >= '01-Jan-2002' 
AND    SHIP_DATE <= '01-May-2003';

--- Version 2 returns simply a count of all the given dates
SELECT COUNT(*)
FROM   shipment
WHERE  SHIP_DATE >= '01-Jan-2002' 
AND    SHIP_DATE <= '01-May-2003';

--- What is destination city name of shipment id# 2004
SELECT CITY_NAME
FROM   shipment,city
WHERE  SHIPMENT_ID = '2004' 
AND    shipment.CITY_ID = city.CITY_ID;

--- What are the truck ids of trucks that have carried 
--- shipments over 100 lbs?
SELECT DISTINCT TRUCK_ID
FROM   shipment
WHERE  WEIGHT >= 100;

--- Give the Names of customers who have sent shipments to cities 
--- starting with 'L'?
SELECT CUS_LNAME, CUS_FNAME
FROM   customer,shipment,city
WHERE  customer.CUS_ID = shipment.CUS_ID 
AND    shipment.CITY_ID = city.CITY_ID 
AND    city.CITY_NAME LIKE 'L%';

--- What are the names of customers who have sent packages to 
--- Lincoln, NE?
SELECT CUS_LNAME, CUS_FNAME
FROM   customer,shipment,city
WHERE  customer.CUS_ID = shipment.CUS_ID 
AND    shipment.CITY_ID = city.CITY_ID 
AND    city.CITY_NAME = 'Lincoln';

--- Who are the customers having over 5 million in revenue and 
--- have sent less than 100lbs?
SELECT DISTINCT CUS_FNAME, CUS_LNAME
FROM   customer, shipment
WHERE  customer.ANN_REVENUE > 5000000 
AND    shipment.WEIGHT < 100;

--- For each customer what is the average weight of a package, 
--- show name and avg weight?
SELECT   CUS_FNAME, CUS_LNAME, AVG(WEIGHT)
FROM     customer,shipment
WHERE    customer.CUS_ID = shipment.CUS_ID
GROUP BY CUS_FNAME, CUS_LNAME;

--- For each city with a population over 100,000 what is the 
--- minimum weight of a package sent there?
SELECT   CITY_NAME, MIN(WEIGHT)
FROM     city,shipment
WHERE    city.POPULATION >= 100000
AND      city.CITY_ID = shipment.CITY_ID
GROUP BY CITY_NAME;

--- For each city that has recieved at least 2 packages, what is the 
--- average weight of a package sent to that city?
SELECT   CITY_NAME, COUNT(SHIPMENT_ID), AVG(WEIGHT)
FROM     city,shipment
WHERE    shipment.CITY_ID = city.CITY_ID
GROUP BY CITY_NAME
HAVING   COUNT(shipment.CITY_ID) >= 2;
""",

# ------------------------------------------------------------------------------
# Tcl/Tk
# ------------------------------------------------------------------------------
'tcl': """#!/usr/local/bin/wish -f
# Syntax Highlighting Test File for TCL/TK
# Comments are like this
# Hello World in tcl/tk

wm title . "Hello world!"

frame .h -borderwidth 2
frame .q -borderwidth 2
button .h.hello -text "Hello world" \
        -command "puts stdout \"Hello world!\"" -cursor gumby
button .q.quit -text "Quit" -command exit -cursor pirate

pack .h -side left
pack .q -side right
pack .h.hello
pack .q.quit

# Procedure Definition
proc printArguments args {
   foreach arg $args {
      puts $arg
   }
}
""",

# ------------------------------------------------------------------------------
# XML
# ------------------------------------------------------------------------------
'xml': """<!-- Syntax Highlighting Test File for XML -->
<!-- Comments are like this -->
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
   <channel>
    <title>Editra.org</title>
    <link>http://editra.org/index.php</link>
    <description>Editra Text Editor</description>
    <language>en-us</language>
    <generator>Editra.org</generator>
    <item>
        <title>Cleanup Round 2</title>
        <link>http://editra.org/index.php?artical=helloWorld</link>
        <description>Hello XML</description>
        <author>admin@editra.org (cody)</author>
        <pubDate>Sat, 11 Nov 2006 17:47:39 -0800</pubDate>
        <guid isPermaLink="true">http://editra.org/index.php?artical=helloWorld</guid>
    </item>
   </channel>
</rss>
""",

}