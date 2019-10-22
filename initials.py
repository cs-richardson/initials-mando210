'''
This program takes the user's full name and output the initials of the user.

Miki Ando
'''

#Gets the full name from the user 
fullname = str(input("Enter full name: "))

#Stores the first letter of the name in the initials variable
initials = fullname[0]

#finds space in the name and gets the letter that is after the space and
#stores in the initials variable 
for i in range(len(fullname)):
    letter = fullname[i]
    if letter == " ":
        initials = initials + fullname[i+1]

#prints the user's initials in upper case
print (initials.upper())      
    
    
