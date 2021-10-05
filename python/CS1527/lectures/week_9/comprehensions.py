input_strings = ['1', '5', '28', '131', '3']

# complex
output_integers = []
for num in input_strings:
    output_integers.append(int(num))

# using list comprehension
# very well optimised -> more efficient
output_integers = [int(num) for num in input_strings]

# using 'if'
output_integers = [int(n) for n in input_strings if len(n) < 3]
