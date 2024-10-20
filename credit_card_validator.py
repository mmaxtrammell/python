# Credit card validator using the Luhn Algorithm
# Inspired by James Hamblin's YouTube video: https://youtu.be/PNXXqzU4YnM?si=DuD8f1mNuvk_MQ-g

credit_card_number = input("Please enter your credit card number: ")
digit_array = [int(digit) for digit in str(credit_card_number)]
weight_array = [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
product_list = []

def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def sum_of_array(arr):
    sum = 0
    for n in arr:
        num_str = str(n)
        for digit in num_str:
            sum += int(digit)
    return sum

n = len(weight_array)

for i in range(n):
    product = digit_array[i] * weight_array[i]
    if len(str(product)) >= 2:
        print(str(product) + " is over 2 digits, so add digit sum the list: ")
        product = sum_of_digits(product)
        print(product)
        product_list.append(product)
    else:
        print(str(product) + " is less than 2 digits, so add it to the list.")
        product_list.append(product)

print("The list of products is:")
print(product_list)
print("The sum of all products is " + str(sum_of_array(product_list)) + ".")
if (sum_of_array(product_list) % 10) == 0:
    print(str(sum_of_array(product_list)) + " ends in zero, so the credit card number is valid.")
else:
    print(str(sum_of_array(product_list)) + " does NOT end in zero, so the credit card number is NOT valid.")
