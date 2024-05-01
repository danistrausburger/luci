PA2 - Luci Lexer Project

Designing and building an interpreter for a programming language. This program is specifically the lexer analysis portion of the interpreter. Our language is called Luci.

This program generates tokens based off of custom-chosen data types and keywords. They are personally defined and customized for our interpreter.

To use this program, one must have Python installed on their machine. Everything else is included in the files.

The project contains three folders: a docs folder, a example folder, and a src folder. 
The docs folder contains the readme file, as well as the presentation slides for the project. 
The example folder contains example files that can be used to test the lexer.
The src folder contains one subfolder: a ply folder that contains the generator files. The src folder also contains the lexer.py file, which holds the Luci lexer.

To use, simply open a new bash terminal and type the following:

cd src

python ./lexer.py

After entering that, you will be prompted to enter a file name, which would look like:

 ../example/yourfile

Replace "yourfile" with the name of the file you wish to pass into the program. Change the file path as needed, the path above works for any tests provided in our example file.

Four example files are provided in the example folder.
You may have anything in the inputted file, including but not limited to numbers, operators, conditionals, and characters.

Remember when creating input files to follow the Luci syntax.

CREDITS

This project uses the PLY python lexical analyzer generator. The link to the page is below.
https://www.dabeaz.com/ply/

Team is comprised of Dani Strausburger and Isabel Pacheco Mattivi
