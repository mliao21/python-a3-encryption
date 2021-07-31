## 📚 Learning Outcomes
* Accept user input through varied menu options
* Validate user input through exception handling
* Process data according to specifications
* Iterate through varied values using compound data types
* Manipulate strings and apply regular expressions
* Develop and implement user-defined classes
* Print formatted output according to given specifications

## 💻 Program Specifications
A cipher is an algorithm used for encrypting or decrypting information. You are being asked to design a terminal-based application for encoding and decoding text based on a provided cipher algorithm.
Your application must meet the following design specifications:
* Your user interface should prompt the user to input the following information:
  1. Whether they would like to encode or decode their text
  2. Enter their text to be encoded/decoded
  3. Enter their cipher
* You may prompt for the input to be entered in any form or order you like, but be sure to give the user clear instructions.
* You must validate that the provided cipher is exactly 26 elements long and only contains lowercase characters from a to z or digits from 0 to 9.
* If the cipher does not meet the criteria, you must handle a ValueError exception by providing a message back to the user and allow them to re-enter their cipher without terminating the program.
* Any entered string is valid for encoding/decoding, however:
  * Any punctuation/spaces/etc. within the text should be removed- only letters are encoded/decoded.
  * The resulting coded or decoded message must be all lowercase letters with no spaces in between.
* Your code should include and use at least two classes of your own creation, at least three user-defined functions aside from \_\_init\_\_ or main(), at least one iterable object, and at least one regular expression.
* Your code must follow the conventions discussed so far in the course (names_with_underscores, ClassNames, four spaces for indentations, spaces between variables/operators, comments throughout, etc.)
* All classes and functions must contain docstring documentation.


### Example Tests
Text to be encoded: “abcde”<br>
Cipher: “bcdefghijklmnopqrstuvwxyza”<br>
Code result: “bcdef”<br>

Text to be decoded: “abcde”<br>
Cipher: “bcdefghijklmnopqrstuvwxyza”<br>
Code result: “zabcd”<br>

Text to be encoded: “Tell me and I forget. Teach me and I remember. Involve me and I learn. - Benjamin Franklin”<br>
Cipher: “bcdefghijklmnopqrstuvwxyza”<br>
Code result: “ufmmnfboejgpshfuufbdinfboejsfnfncfsjowpmwfnfboejmfbsocfokbnjogsbolmjo”<br>

Text to be decoded: “uifcftuboenptucfbvujgvmuijohtjouifxpsmedboopucftffopsfwfoupvdifeuifznvtucfgfmuxjuiuififbsuifmfolfmmfs”<br>
Cipher: “bcdefghijklmnopqrstuvwxyza”<br>
Code result: “thebestandmostbeautifulthingsintheworldcannotbeseenoreventouchedtheymustbefeltwiththehearthelenkeller”<br>
