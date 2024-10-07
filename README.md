# PRODIGY_CS_01
**INTRODUCTION**
Caeser Cipher is a cryptographic technique used to encrypt and decrypt messages(data). this techique was brought up by Julius Caeser to send confidential messages. As at now this cryptographic techniques is still been used.
The Caeser Cipher has alternative names of which some include shit Caeser, Caeser shift, Ceaser code, etc 

**HOW IT WORKS**
In this technique, each character is substituted by a letter certain fixed number position it's later or before the alphabet for encryption(from plaintext to cipher text) and decryption (from cipher text to plaintext). 
for example:
ABCD using a shift of 1 will turn to BCDE and with a shift of 2 becomes CDEF

encryption function: (x) = (x + n)mod26
decryption function: (x) = (x - n)mod26
where x is the alpharbet numbr and m is the shift value 

**NOTE**
the shift represent the number of position to move a letter to get it's cipher 
