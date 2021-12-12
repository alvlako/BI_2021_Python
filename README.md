## Python-written analoques of Unix utilities

## Installation

The scripts used to reconstruct Unix commands can be cloned via git clone from the branch:

`git clone https://github.com/alvlako/BI_2021_Python.git`

Alternatively, the zip folder can be downloaded from GitHub visual interface and unzip:

`gunzip my_folder`

Scripts can be run from the command line:

`./command_name.py`

Info and help are accessible via 

`./command_name.py -h`

### wc.py

This script allows to reproduce original wc command results with -l, -c and -w flags. -l is used to count lines, -c and -w are used for counting bytes and words respectively.

Examples:

Input (content of the ex.txt file):

touch

read

head

`./wc.py -l ex.txt`

Output: 3

`./wc.py -c ex.txt`

Output: 16

`./wc.py -w ex.txt`

Output: 3

These outputs are consistent with the output from original Unix utility.

### ls.py

The script allows to list files and directories in the defined directory (current directory set up as a default). -a option is used to list only non-hidden objects. In the default mode without flags all the files are listed

### sort.py

The script allows to sort lines in the input file. 

Input (content of the ex.txt file):

touch

read

head

`./sort.py ex.txt`

Output:

head

read

touch

### rm.py

Allows to remove the defined file. With the flag -r, allows to remove directory recursevely.

### uniq.py

Allows to print only unique lines from the defined file.

Input (content of the ex.txt file):

touch
read
head
read

`./uniq.py ex.txt`

Output:

head
read
touch

### cat.py

Allows to print the content of a file out.

Input (content of the ex.txt file):

touch
read
head
read

`./uniq.py ex.txt`

Output:

head
read
touch
read

### tail.py

Allows to print from n lines from a file before the end. By default, number of lines is set to 10 but can be changed with the -n flag.

Input (content of the ex.txt file):

touch
read
head
read
why
so
uhhh
task
let
my
people
go

`./tail.py ex.txt`

Output:

head
read
why
so
uhhh
task
let
my
people
go

Input (content of the ex.txt file):

touch
read
head
read
why
so
uhhh
task
let
my
people
go

`./tail.py -n 3 ex.txt`

Output:

my
people
go

## Compatibility with command line stdin and usage in single-liners with multiple pipes

All the commands can read the input from stdin. In these cases positional arguments requirements (file, folder) are suspended.
Generally, multiple-line stdin inputs are supported (handled via internal cat analogue).

`./tail.py ex.txt | ./wc.py -l`

Output: 10

Multiple lines stdin usage.

`ls *txt`

Output: 
11.txt  111.txt

`ls *txt | ./wc.py -l`

Output: 2
