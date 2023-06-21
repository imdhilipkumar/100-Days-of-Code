
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(e_text,e_shift):
    ciper=""
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    # for my porsonal understand i have alphabets , direction, text,shit
    # to get the each letter index we use for loop
    for letter in text:
        #to store the string result
        #to check the letter in alphabet value index mean it look the letter in alphabet that we enter in the text and stor to position
        # remeber this step we to get the index value value only not the alphabet letter
        position=alphabet.index(letter)
        # this line explained the postion of alphabet and shift amount
        new_position=position+shift
        # this line conside the index value of letter 
        new_letter=alphabet[new_position]
        ciper+=new_letter
    print(f"The encoded text is {ciper}")        

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

# Decrypt function
def decrypt(d_text,d_shift):
    d_cipher=""
    for letter in d_text:
        position=alphabet.index(letter)
        new_position=position-d_shift
        new_letter=alphabet[new_position]
        d_cipher+=new_letter
    print(f"The decoded text is {d_cipher}")
        
    
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction=="encode":
    encrypt(e_text=text,e_shift=shift)
elif direction=="decode":
    decrypt(d_text=text,d_shift=shift)