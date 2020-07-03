# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

personal_info = [('pujan', 'gautam', 23), ('ram', 'shrestha', 5), ('aakash',
                                                                        'maharjan', 25), ('sneha', 'bhandari', None), ('bijay', 'khanal', 27)]

sum=0
avg=0.0
count_none=0
for age in personal_info:
    if age[2] == None:
        count_none += 1
    else:
        sum += age[2]
    
avg = sum/(len(personal_info)-count_none)
print("Avearge age is: ",avg)

for name in personal_info:
    if name[2] != None:
        if name[2] >= avg:
            print(name[0] +" is old.")
        else:
            print(name[0]+" is young")
        


