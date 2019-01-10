'''
Nikki Agrawal
Python for Social Good Intersession

The Point of the Program is to analyze essays and determine whether they are formal or informal. If they are informal they are thrown
away, and if they are formal they are kept for others to read and maybe publish. This could be used in the real world to help
newspapers sort through the articles that are submitted to them so they don't have to read every single one.
'''

#to make it easier to split things up
import re

#the variable to mark down how many black points the essay has. Too many and it gets thrown away
mark = 0

#the list of informal variables
informal = ["wow", "like", "!!", "?!", " I ", "my", "you", "whoa", "great", "awesome" "...", "really", "cool", "get", "ugh", "dude",
            "gawd", "rad", " i "]

acronyms = ["omg", "btw", "ttyl", "l8r", "gtg", "idk", "idc", "lol", "lmao"]

#the essay to be analyzed

essay = input ("Insert Essay for Checking")

#to check how many informal variables there are so I can run each one by the essay, and how many acronyms
x = len(informal)
z = len(acronyms)

#the variable to run each informal[variable] by, and each acryonym
informalVar = 0
acr = 0

#to check the code for punctuation and split it up
a = re.findall(r"[\w']+|[.,!?;]", essay)

#a variable for how long it is so that I can run a if command to analyze the words for different marks
b = len(a)

#the variable to run each CAPS check by
caps = 0

#to run each word by my informal list and see how many times an informal word is used
for i in informal:
        if informal[informalVar] in a:
                mark = mark + 1
                informalVar = informalVar + 1

        else:
                informalVar= informalVar + 1

#to run each word by my acronym list
for w in acronyms:
        if acronyms[acr] in a:
                mark = mark + 1
                acr = acr + 1

        else:
                acr= acr + 1


#to check for words that are in all CAPS
for j in a:
        if a[caps].isupper() == True:
                mark = mark + 1
                caps = caps + 1
        else:
                caps = caps + 1

#to calculate the grade based on how long the essay is
percent = (10/100 * b) / 2

if mark < 3:
        print ("Formal")

elif mark > percent:
        print ("Informal")

else:
        print ("Formal")

#Give the Essay a Grade
grade = (100 - 2*(int(x) / int(b)))
print(str(grade) + "%")