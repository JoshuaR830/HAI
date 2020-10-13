myString = "0123456789"

# String can be sliced in steps
# [Start, End, Step size]
# Will give result from start (included) to end (excluded) with the step size

print(myString[::-1])

# This is a reasonable result
# : indicates to the start/end
# So this is basically saying from the first number to the last number slice in steps of -1
# This only makes sense in reverse
# Starting at the beginning -1 is the last item in the string
# So it starts by giving the last item and counts down