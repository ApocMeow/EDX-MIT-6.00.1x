import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
       
        # Hard copy of alphabet that should NOT be changed
        lowerAlpha = string.ascii_lowercase
        upperAlpha = string.ascii_uppercase
        
        # Empty starting Dictionaries we will build up through iteration
        lowerDict = {}
        upperDict = {}

        # Our iteration counter which starts at 0
        n = 0
        
        # Adding values to dictionary for lowercase characters and their starting position in the alphabet
        for i in lowerAlpha:
            n += 1
            lowerDict[i] = n  

        # Now we can update the values based on the shift integer and then replace 
        # those with the letter from that position in the alphabet
        for i, v in lowerDict.items():
            if v + shift >= 26:
                lowerDict[i] = lowerAlpha[((v + shift) % 26) - 1]
            elif v + shift < 26:
                lowerDict[i] = lowerAlpha[v + shift - 1]

        # Resetting Our iteration counter which starts at 0
        n = 0

        # Adding values to dictionary for uppercase characters and their starting position in the alphabet
        for i in upperAlpha:
            n += 1
            upperDict[i] = n
  
        # Now we can update the values based on the shift integer and then replace 
        # those with the letter from that position in the alphabet
        for i, v in upperDict.items():
            if v + shift >= 26:
                upperDict[i] = upperAlpha[((v + shift) % 26) - 1]
            elif v + shift < 26:
                upperDict[i] = upperAlpha[v + shift - 1]

        # Create the final dictonairy as a copy of the shifted lowercase dictionary
        finalDict = lowerDict.copy()
    
        # Then add the shifted uppercase dictionary to it
        finalDict.update(upperDict)
    
        # Finally the function returns the full shifted dictionary
        return(finalDict)   
    
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
       
        # Variable containing our shifted Dictionary
        shiftDict = self.build_shift_dict(shift)
        
        # Variable containg the unshifted message
        preShiftMessage = self.get_message_text()
        
        # Variable that we will build with shifted characters
        postShiftMessage = ''
        
        # Now we need to iterate over preshift string and append the new values
        # to the postshift string to build it up
        for c in preShiftMessage:
            if c not in shiftDict.keys():
                postShiftMessage += str(c)
            else:
                v = shiftDict[c]
                postShiftMessage += str(v)
        
        # Finally the function returns the shifted message
        return(postShiftMessage)
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. elf.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)        

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        # Temporary variables that we will build up and evetually return
        validCount = 0
        validShift = 0
        testCount = 0
        testShift = 1     
        
        # Set up while loop
        while (26 - testShift) > 1:        
            # Apply shift to message
            testString = self.apply_shift(testShift)
            # Split message into string
            splitString = testString.split()   
            # Process to check if each item in the split string is a valid word
            for word in splitString:
                # increase count for each valid word
                if is_word(self.valid_words, word) == True:
                    testCount += 1              
            # Store count and shift value if count greater than existing
            if testCount > validCount:
                validCount = testCount
                validShift = testShift
            # Increment shift value
            testShift += 1
            # Reset testCount value
            testCount = 0
            
        # Function returns a Tuple containing the final shift value used to
        # decrypt the message and the decrypted message using the final shift
        return(validShift, self.apply_shift(validShift))
        
        
        

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage("The tweet came as Mr Trump's running mate Mike Pence said he would stand by him despite an outcry over the remarks.", 9)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage("Cqn cfnnc ljvn jb Va Cadvy'b adwwrwp vjcn Vrtn Ynwln bjrm qn fxdum bcjwm kh qrv mnbyrcn jw xdclah xena cqn anvjatb")
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
