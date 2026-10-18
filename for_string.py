""" Kirjutage programm, mis käib läbi iga tähe sõnes ja prindib selle välja. """

# text = "Python"

# for letter in text:
#     print(letter)

# sone = "Tere, ma olen Python!"
# for taht in sone:
#     print(taht)

""" Kirjutage programm, mis prindib sõne tagurpidi (viimasest tähemärgist esimese juurde), nii et iga täht kuvatakse eraldi reale. """

# text = "Python"

# for letter in reversed(text):
#     print(letter)

# sone = "Tere, ma olen Python!"
# for taht in reversed(sone):
#     print(taht)

# text = "Python"

# for letter in range(5, -1, -1):
#     print(text[letter])

text = "lauri"

length = len(text)
print(length)
for letter in range(len(text) - 1, -1, -1):
    print(text[letter])