# Q1. Find all pairs of an integer array whose sum is equal to a given number
def find_pairs_with_sum(arr, target):
    pairs = []
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

arr = list(map(int, input("Enter an integer array separated by spaces: ").split()))
target_sum = int(input("Enter the target sum: "))
pairs = find_pairs_with_sum(arr, target_sum)
print("Pairs with the target sum:", pairs)



# Q2. Reverse an array in place
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = list(map(int, input("Enter an integer array separated by spaces: ").split()))
reverse_array(arr)
print("Reversed array:", arr)




# Q3. Check if two strings are a rotation of each other
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    concatenated = str1 + str1
    return str2 in concatenated

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = are_rotations(str1, str2)
if result:
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")



    # Q4. Print the first non-repeated character from a string
def first_non_repeated_char(string):
    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    for char in string:
        if char_count[char] == 1:
            return char
    return None

string = input("Enter a string: ")
result = first_non_repeated_char(string)
if result:
    print("The first non-repeated character is:", result)
else:
    print("No non-repeated characters found.")



# Q5. Recursive function to check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

string = input("Enter a string: ")
result = is_palindrome(string)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



    # Q6. Convert a postfix expression to a prefix expression
def postfix_to_prefix(postfix):
    stack = []

    for symbol in postfix:
        if symbol.isalnum():
            stack.append(symbol)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = symbol + operand1 + operand2
            stack.append(expression)

    if len(stack) != 1:
        return "Invalid postfix expression"
    else:
        return stack[0]

postfix = input("Enter a postfix expression: ")
prefix = postfix_to_prefix(postfix)
print("Prefix expression:", prefix)



# Q7. Convert a prefix expression to an infix expression
def prefix_to_infix(prefix):
    stack = []

    for symbol in reversed(prefix):
        if symbol.isalnum():
            stack.append(symbol)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = operand1 + symbol + operand2
            stack.append(expression)

    if len(stack) != 1:
        return "Invalid prefix expression"
    else:
        return stack[0]

prefix = input("Enter a prefix expression: ")
infix = prefix_to_infix(prefix)
print("Infix expression:", infix)


# Q8. Check if all the brackets are closed in a code snippet
def are_brackets_closed(code):
    stack = []

    for char in code:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False

    return not stack

code = input("Enter a code snippet: ")
if are_brackets_closed(code):
    print("All brackets are closed properly.")
else:
    print("Some brackets are not closed properly.")



# Q9. Reverse a stack
def reverse_stack(stack):
    if not stack:
        return
    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

stack = list(map(int, input("Enter the stack elements separated by spaces: ").split()))
reverse_stack(stack)
print("Reversed stack:", stack)



# Q10. Find the smallest number using a stack
class StackWithMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

stack = StackWithMin()

elements = list(map(int, input("Enter the stack elements separated by spaces: ").split()))
for element in elements:
    stack.push(element)

min_element = stack.get_min()
if min_element is not None:
    print("Smallest element in the stack:", min_element)
else:
    print("The stack is empty.")
