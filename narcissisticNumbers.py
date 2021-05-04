'''
Nikki Agrawal
Narcissistic Numbers Code

some digit abcd such that a^4 + b^4 + c^4 + d^4 = abcd
narcissitic numbers
'''

#the list upon which the narcissistic numbers that are found will be saved
savedNumbers = []

for i in range(1000, 9999):
    b = [int(digit) for digit in str(i)]
    d = ((b[0]**4) + (b[1]**4) + (b[2]**4) + (b[3]**4))

    if i==d:
        savedNumbers.append(i)

print(savedNumbers)
