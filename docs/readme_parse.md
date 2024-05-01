PA3 - Luci Parser Project

Designing and building an interpreter for a programming language. This program is specifically the parsing portion of the interpreter. Our language is called Luci.

This program parses through tokens made from our custom lexer. This lexer has tokens of custom-chosen data types and keywords, and are defined for our project. This program specifcially parses those custom tokens, creating an AST from the tokens.

To use this program, one must have Python installed on their machine. Everything else is included in the files.

The project contains three folders: a docs folder, a example folder, and a src folder. 
The docs folder contains the readme file, as well as the presentation slides for the project. 
The example folder contains example files that can be used to test the lexer.
The src folder contains one subfolder: a ply folder that contains the generator files. The src folder also contains the lexer.py file, which holds the Luci lexer/parser.

To use, simply open a new bash terminal and type the following:

cd src

python ./lexer.py

After entering that, you will be prompted to enter a file name, which would look like:

 ../example/yourfile

Replace "yourfile" with the name of the file you wish to pass into the program. Change the file path as needed, the path above works for any tests provided in our example file.

Example files are included in the example folder, the contents can be used to test the parser.

Custom test cases can also be created and passed into the program. Remember when creating tests to follow our syntax, specifically remembering that for if, switch, while, and for code blocks, keep everything on one line.

CREDITS

This project uses the PLY python lexical analyzer generator. The link to the page is below.
https://www.dabeaz.com/ply/

Team is comprised of Dani Strausburger and Isabel Pacheco Mattivi
