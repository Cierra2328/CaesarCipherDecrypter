letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z']

encrypted = input("Enter the encrypted plaintext: ")

decrypted = '';
encrypted1 = encrypted.lower()

for i in range(26):
    for letter in encrypted1:
        if letters.count(letter) < 1:
            decrypted += letter 
        else:
            index = letters.index(letter)
            new_index = index - i
            decrypted += letters[new_index]
    print(decrypted)
    decrypted = ''
