# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


def convert_to_snakecase(string):
    snakecase= [string[0].lower()]
    kebab_case=[string[0].lower()]
    for s in string[1:]:
        if s == s.upper():
            snakecase.append('_')
            kebab_case.append('-')
            snakecase.append(s.lower())
            kebab_case.append(s.lower())
        else:
            snakecase.append(s)
            kebab_case.append(s)
    print("Snake Case = ",''.join(snakecase))
    print("Kebab Case = ",''.join(kebab_case))




str= input("Enter string in camel case: ")

convert_to_snakecase(str)