# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

def paranthesis_validation(str):
    brackets=['()','{}','[]']
    while any(x in str for x in brackets): 
        for br in brackets:
            str=str.replace(br,'')
    return not str


braces=input('Enter the braces:')
print(braces,'-','Balanced'if paranthesis_validation(braces) else "Unbalanced")
