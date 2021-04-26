
'''
Nikki Agrawal
Computer Security Block 8
Wes Chao
September 23, 2020

Assignment: User Input Validation
'''

#code to be hacked into
calculator = input("I am a friendly calculator. Give me a math problem to solve!")
solution = eval(calculator)
print (solution)

'''
This could easily be hacked into by putting some sort of code that could delete files or destroy something instead of a calculator command!
To fix it, eval shouldn't be used in the program.
'''

#possible program to hack into the code above
fakeInput = #rm -rf/
#or any other type of clearing command would be super dangerous


#fixed code that shouldn't be hacked into as easily
number1 = int(input("what is the first number?"))
number2 = int(input("what is the second number?"))
operation = input("what operation? addition, subtraction, multiplication, division, exponent")

if operation == "addition":
    print (number1 + number2)

elif operation == "subtraction":
    print (number1 - number2)

elif operation == "multiplication":
    print (number1 * number2)

elif operation == "division":
    print (number1 / number2)

elif operation == "exponent":
    print (number1 ** number2)

'''
If you did misuse eval in the format that it is above, a person could get into huge trouble for
hacking into a device. You could delete all files, or code in a bug that changes all the words
to something else, or generally mess with someone. You could also use it to steal
sensitive information, in which case you would be breaking privacy laws.

'''

#Methods for Protecting against Eval
'''
1. Change the code so that it doesn't use eval in the first place
2. I was doing research and I read somewhere that there are lines of Javascript
that would protect someone from taking over the system. It basically used a UserID
variable with their computer's unique password/ID and said that unless the user running
the program had that UserID, not to run any eval commands for them.

Is eval even necessary?
Yes, I believe so. Research says that there are some things that cannot be done without eval,
and coders just have to take the proper precautions and look through the code before evaluating it
to make sure it is fine. But, writing code that does the same thing and doesn't use eval would take
WAY too long and be hard.
'''

#Notes based on Comments for Resubmission
'''
Comment: find specific laws for criminal liability of using eval
Source: https://www.cga.ct.gov/2012/rpt/2012-r-0254.htm#:~:text=The%20law%20punishes%20hacking%20under,to%20%2415%2C000%2C%20or%20both).

By using eval to remove a computer's information, or to cause the computer to malfunction, or to alter or erase information
because of the permissions that eval gives,

Class B misdemeanor - up to 6 months in prison and/or a fine of $1000
if they cause over $2,500 in property damage,
Class A misdemeanor if they acted with reckless disregard
Class D felony if they acted maliciously or with malicious intent - up to 5 years in prison and/or a fine of $5000

There are a bunch of really specific spectrums of misdemeanors and felonies depending on what a person does
and why they did it.
'''

#More info on UserID
'''
UserID is specific to Javascript. Because this language is many times used to run games or codes with screens/users,
different users can have different IDs.

I was in the web development class last year and coded a minor coloring game,
and while I was the only user who was storing stuff in the back-end, it was possible for multiple users to have run the program
played the game and stored their information. In this case, there would be different UserIDs stored.

A protocol could getElementById from the document for the username.

Or more specifically, it is like the idea of a username, and not being able to see a program like my emails
without having logged into my account. A person would be unable to run the eval program without having a certain
userID.

It is like a method of authorization, basically, to stop anyone without the authority to from misusing eval.
'''
