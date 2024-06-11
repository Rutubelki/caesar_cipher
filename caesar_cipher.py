# def greet(name,loc):
#     print("hello:",name,"you are from",loc)
# greet(loc="Delhi",name="rutu")

#////////////////////////////////// paint coverage ////////////
# import math
# def paint_calc(height,width,cover):
#     test_h=int(input())
#     test_w=int(input())
#     cover=5
#     no_cans=(test_h*test_w)/cover
#     round_up= math.ceil(no_cans)
#     print("number of cans needed=",round(round_up))
# paint_calc(height="test_h",width="test_w",cover="cover")

#////////////////////////////////////////////prime or not////////////////////////

# def prime(num):
#     is_prime=True
#     for i in range(2,num):
#         if n%i==0:
#             is_prime=False
#     if is_prime:
#         print("prime")
#     else:
#         print("not prime")
# n=int(input())
# prime(n)

#///////////////////////////////////// caesar cipher /////////////////////////////////
from logo import logo
print(logo)
caesar_cipher=True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while caesar_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>26:
        shift=shift%26

    def caesar(start_text,shift_amount,cipher_direction):
        end_text=""
        for char in start_text:
            if char in alphabet:
                index_letter=alphabet.index(char)
                if cipher_direction=="encode":
                    shift_left=index_letter+shift_amount
                elif cipher_direction=="decode":
                    shift_left=index_letter-shift_amount
                shift_letter=alphabet[shift_left]
                end_text+=shift_letter             
        print(end_text)
    caesar(text,shift,direction)

    con=input("yes to continue or no?")
    if con=="no":
        caesar_cipher=False


            
            
# def encrypt(text_e,shift_e):
#     encrypt_text=""
#     for char in text_e:
        
#         index_letter=alphabet.index(char)
#         shift_left=index_letter+shift_e
#         shift_letter=alphabet[shift_left]
#         encrypt_text+=shift_letter  
        
# def dencrypt(text_e,shift_e):
#     dencrypt_text=""
#     for char in text_e: 
#         index_letter=alphabet.index(char)
#         shift_left=index_letter-shift_e
#         shift_letter=alphabet[shift_left]
#         dencrypt_text+=shift_letter         
#     print(dencrypt_text)
# if direction=="encode":
#     encrypt(text,shift)
# elif direction=="decode":
#     dencrypt(text,shift)



            
        

    
