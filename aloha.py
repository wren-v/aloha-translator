#Combo dictionary
combo_vow_dict = {'AI': 'eye-', 'AE': 'eye-', 'AO': 'ow-',
              'AU': 'ow-', 'EI': 'ay-', 'EU': 'eh-oo-',
              'IU': 'ew-', 'OI': 'oy-', 'OU': 'ow-', 'UI': 'ooey-',}
#Regular consonants dictionary
reg_consonants_dict = {'P': 'p', 'K': 'k', 'H': 'h',
                       'L': 'l', 'M': 'm', 'N':'n',
                       "'": "'", 'W': 'w'}
#Regular vowels
reg_vow_dict = {'A': 'ah-', 'E': 'eh-', 'I': 'ee-', 'O': 'oh-', 'U': 'oo-'}

#W list
w_list = {'IW': 'v', 'EW': 'v'}

def run_phonetic_translator():
    '''
    Run the main translation task which repeatedly asks the user to enter a
    valid Hawaiian word, make the translation, and then ask if the user
    wants to repeat the process. If the user wants to continue, they can
    enter another word to be converted, and if they do not want to
    continue, the program ends.

    Args:
        None
    Returns:
        None
    '''
    while True:
        word = input("Enter a Hawaiian word to pronounce ==> ")
        if is_valid_hawaiian(word):
            print(convert_word(word))
            run = ask_run_again()
            if not run:
                break
        else:
            print("Word contains an invalid Hawaiian charater, please try again \n")

def ask_run_again():
    '''
    Prompt the user to ask if they would want to enter another word.
    Return True if the user types Y or YES, and return False if the user
    types N or NO. For any other response, they should be asked again.

    Args:
        None
    Returns
        (boolean) True if user wants to run again, False if not
    '''

    while True:
        user_response = input("\nDo you want to enter another word? (Y/n): ")
        user_response_low = user_response.lower()
        if user_response_low in ["yes", "y"]:
            return True
        elif user_response_low in ["no", "n"]:
            return False
        else:
            print("Y/n")
            
def convert_word(word):
    '''
    This function will return the phonetic guide for a given Hawaiian
    word or phrase. Use the rules listed above to make the translation,
    including hyphens after each vowel sound.

    Args:
        word (str): the Hawaiian word to convert
    Returns:
        (str) - the phonetic guide for the given word
    '''
    word = word.upper()
    newstring = ''
    position = 0
    
    while position < len(word): #iterates until goes through all letters in word
        letter_1 = word[position]

        if position < len(word) - 1: #If not in final position
            next_letter  = word[position + 1]
            combo = letter_1 + next_letter
        else:
            combo = False #skips the rest in final position
            next_letter = False
            
        if combo in combo_vow_dict: #Checks if two characters in combo list
            newstring += combo_vow_dict[(combo)]
            position += 1 #skips next iteration if double char combo
                
        elif combo in w_list: #deals with w's
            newstring += w_list[combo]
            
        elif letter_1 in reg_vow_dict: #concerns regular vowels
            newstring += reg_vow_dict[(letter_1)]
            
        elif letter_1 in reg_consonants_dict: #concernts regular consonants
            newstring += reg_consonants_dict[(letter_1)]
        position += 1 #counts at end
        
    return word+" is pronounced "+(newstring[0].upper() + newstring[1:-1])
            
def is_valid_hawaiian(word):
    '''
    Check if the given word is valid Hawaiian word.

    Args:
        word (str): the word to be checked
    Returns:
        (boolean) - True if word has all valid Hawaiian characters,
                    False if not
    '''
#checks if theres letters in the input and if they are allowable
    for letter in word:
        if letter.upper() not in "WPKHLMNAEIOU' " and len(word) > 0:
            return False
    return True

#Run Translator
print("Aloha Phonetic Translator by Wren Vogelschmidt\n")
run_phonetic_translator()

