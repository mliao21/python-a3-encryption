# encryption.py
# AUTHOR NAME: MELISSA LIAO
#
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import re

class Encode:
    """ A class used to create Encode object.

        Attributes:
        input_value (str): String that represents user's input text
        cipher_value (str): String that represents cipher value input by user

    """

    def __init__(self, input_value, cipher_value):
        self.__input_val = input_value
        self.__cipher_val = cipher_value

    @property #decorator
    def input_value(self):
        return self.__input_val

    @property #decorator
    def cipher_value(self):
        """ User needs to input a valid cipher value to encode within criteria.

            Returns:
            Input cipher value must return with only 26 alphanumeric elements, all in lowercase.
            Otherwise, it will trigger a ValueError message.

        """

        try:
            if not (self.__cipher_val.isalnum() == True and len(self.__cipher_val) == 26 and self.__cipher_val.islower() == True):
                raise ValueError()
            else:
                return self.__cipher_val
        except ValueError:
            print("Please re-enter a valid cipher. Your cipher must be in lowercase and be 26 elements of a-z or 0-9.")

    def result_val(self):
        """ Function compiles the inputted text by the user and filters in all alphabetical elements only.
            Inputted elements are converted to lowercase.

            Returns:
            Filtered and converted alphabetical elements are encoded by cipher code.
            This is done by taking each processed element and compare it with the index value of the alphabet.
            Then this index value takes as reference value to select the element of the cipher code.

        """

        regex = re.compile(r'[a-zA-Z]+')
        alpha_input_val = regex.findall(self.input_value)
        concat_input_val = "".join(alpha_input_val)
        processed_val = concat_input_val.lower()        
        print("***Processed string for demo only: ", processed_val)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        print("Your output is: " + ("".join(self.cipher_value[alphabet.index(processed_val[i])] for i in range(len(processed_val)))))

class Decode:
    """ A class used to create Decode object.

        Attributes:
        input_value (str): String that represents the encoded text input by the user
        cipher_value (str): String that represents the cipher value that was used to encode

    """

    def __init__(self, input_value, cipher_value):
        self.__input_val = input_value
        self.__cipher_val = cipher_value

    @property #decorator
    def input_value(self):
        return self.__input_val

    @property #decorator
    def cipher_value(self):
        """ User needs to input a valid cipher value to encode within criteria.

            Returns:
            Cipher value must return with only 26 alphanumeric elements, all in lowercase.
            Otherwise, it will trigger a ValueError message.
            Here we assume that cipher value contains elements of input_value.

        """

        try:
            if not (self.__cipher_val.isalnum() == True and len(self.__cipher_val) == 26 and self.__cipher_val.islower() == True):
                raise ValueError()
            else:
                return self.__cipher_val
        except ValueError:
            print("Please re-enter a valid cipher. Your cipher must be in lowercase and be 26 elements of a-z or 0-9.")

    def result_val(self):
        """ Function decodes the encoded text value inputted by the user.

            Returns:
            Each encoded element are compared with the index value of the cipher code.
            Then this index value takes as reference value to select the letter from the alphabet in order.

        """

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        print("Your output is: " + ("".join(alphabet[self.cipher_value.index(self.input_value[i])] for i in range(len(self.input_value)))))
    
     
def main():
    """ main() function declares steps and process of how it is displayed in the terminal for encryption application.
        User will need to choose whether they want to encode or decode the text value that they will input.

        Returns:
        If user chooses to encode text value, it will encrypt the inputted values.
        If user chooses to decode encrypted value: it will look for the "original" text message.
        Both returns are based on cipher code inputted by the user.

    """

    print("ENSF 592 Encryption Program")

    # First step:
    # User must input correct choice with an integer value, either 1 or 2, to select encoding or decoding process, respectively.
    # Otherwise, it will keep asking the user for valid choice.
    while True:
        test_type = input("Please select 1 if you wish to encode otherwise select 2 to decode: ")
        if test_type not in ('1','2'):
            print("You must select either 1 or 2.")
        elif test_type in ('1','2'):
            break

    # Second step: User must input the text they want to encode or decode.
    # If user choose to encode, they can input any type of text they want.
    # If user choose to decode, we assume that all elements of input text are contain in the cipher code.
    input_val = input("Please enter text to be processed: ")

    # Third step: User must input a cipher text. Text must contain only 26 alphanumeric elements in lowercase.
    # It will keep prompting the user to input a valid cipher text until criteria is met.
    while True:
        cipher_val = input("Please enter your cipher text: ")
        if not (cipher_val.isalnum() == True and len(cipher_val) == 26 and cipher_val.islower() == True):
            print("ValueError: Please re-enter a valid cipher. Your cipher must be in lowercase and be 26 elements of a-z or 0-9.")
        elif cipher_val.isalnum() == True and len(cipher_val) == 26 and cipher_val.islower() == True:
            break

    # Last block step to process output result
    alphabet = "abcdefghijklmnopqrstuvwxyz" # alphabet must be included for index reference
    if test_type == '1': 
        # If user chooses to encode: It filters in only letters from the text inputted in step #2.
        # It then concatenates the values into one single string and converts it all in lowercase.
        regex = re.compile(r'[a-zA-Z]+') 
        alpha_input_val = regex.findall(input_val) 
        concat_input_val = "".join(alpha_input_val) 
        processed_val = concat_input_val.lower()
        print("***Processed string for demo only: " + processed_val)

        # Each processed element of the string is compared with the index value of the alphabet.
        # Then this index value takes as reference value to select the element of the cipher text.
        print("Your output is: " + ("".join(cipher_val[alphabet.index(processed_val[i])] for i in range(len(processed_val)))))
    
    elif test_type == '2':
        # If user chooses to decode: It will automatically take each encrypted element input by the user in step #2. 
        # And compared it with the index value of the cipher text. With this index value, it takes as reference to find elements from the alphabet.
        print("Your output is: " + ("".join(alphabet[cipher_val.index(input_val[i])] for i in range(len(input_val)))))
    

    # Use of classes are included to bypass user input and output results automatically. Four examples are shown below.
    print('\n')
    print("***Example test cases to bypass user input")

    print('\n')
    test1 = Encode("This is an example sentence with 098273409870 and @#($*&@)#(*$", "2cd8fghijk7mn1pq9st3vwx0za")
    print("Test 1, Encoding: " + test1.input_value)
    print("Cipher 1: " + test1.cipher_value)
    test1.result_val()

    print('\n')
    test2 = Decode("ifmmpxpsm8", "2cd8fghijk7mn1pq9st3vwx0za")
    print("Test 2, Decoding: " + test2.input_value)
    print("Cipher 2: " + test2.cipher_value)
    test2.result_val()

    print('\n')
    test3 = Encode("Tell me and I forget, teach me and I may remember, involve me and I learn” by Benjamin Franklin", "2cd8fghijk7mn1pq9st3vwx0za")
    print("Test 3, Encoding: " + test3.input_value)
    print("Cipher 3: " + test3.cipher_value)
    test3.result_val()

    print('\n')
    test4 = Decode("3fmmnf218gpshf33f2dinf218n2zsfnfncfsj1wpmwfnf218mf2s1czcf1k2nj1gs217mj1", "2cd8fghijk7mn1pq9st3vwx0za")
    print("Test 4, Decoding: " + test4.input_value)
    print("Cipher 4: " + test4.cipher_value)
    test4.result_val()

if __name__ == '__main__':
    main()

