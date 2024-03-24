PA3 - Luci Parser Project

Designing and building an interpreter for a programming language. This program is specifically the parsing portion of the interpreter. Our language is called Luci.

This program parses through tokens made from our custom lexer. This lexer has tokens of custom-chosen data types and keywords, and are defined for our project. This program specifcially parses those custom tokens, creating an AST from the tokens.

To use this program, one must have Python installed on their machine. Everything else is included in the files.

The project contains three folders: a docs folder, a example folder, and a src folder. 
The docs folder contains the readme file, as well as the presentation slides for the project. 
The example folder contains example files that can be used to test the lexer.
The src folder contains one subfolder: a ply folder that contains the generator files. The src folder also contains the lexer.py file, which holds the Luci lexer/parser.

To use, simply open the file and run it. A prompt will appear in the command line, and you can enter your desired input to be tokenized then parsed. An AST will be returned, generated from your input.

Example files are included in the example folder, the contents can be used to test the parser.

CREDITS

This project uses the PLY python lexical analyzer generator. The link to the page is below.
https://www.dabeaz.com/ply/

Team is comprised of Dani Strausburger and Isabel Pacheco Mattivi
