#Binary       '0b' or '0B'
#Octal        '0o' or '0O'
#Hexadecimal  '0x' or '0X'
str = input("Binary,Octal,Hexadecimal. Convert Text here: ")
print(" ".join(f"{ord(i):08b}" for i in str))
print(" ".join(f"{ord(i):0o}" for i in str))
print(" ".join(f"{ord(i):0x}" for i in str))
if str == "":
    print("Please enter your text.")
