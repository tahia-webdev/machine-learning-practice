# Create acronyms
# take input string
text = input("Enter the text that you want acronym of: ")
splited_text = text.split(" ")
acronym = ""
for i in splited_text:
    acronym += i[0].upper()
print(splited_text)
print(acronym)
