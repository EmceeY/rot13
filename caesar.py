
def alphabet_position(letter):
        all_lower = letter.lower()
        position = ord(all_lower[0]) - 97
        return(position)

def rotate_character(char, rot):
        if char.isalpha():
                new_Val = ((alphabet_position(char)+ int(rot)) % 26)
                if char.islower():
                        new_Val = new_Val + 97
                        return(chr(new_Val))
                elif char.isupper:
                        new_Val = new_Val + 65
                        return(chr(new_Val))        
        else:
                return(char)

def encrypt(text, rot):
#        user_input_is_valid(argv)
#        rot = int(argv[1])
        new_text = ("")
        for char in text:
                if char.isalpha():
                        new_val = rotate_character(char, rot)
                        new_text = (new_text + new_val)
                else:
                        new_text = new_text + char
        return(new_text)        


