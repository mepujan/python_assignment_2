# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

list_of_friends=['john','ram','hari','shyam','pujan','sneha','santosh','John']
count=-1
for name in list_of_friends:
    count += 1
    if 'John' == name:
        print('found')
        break
    else:
        if count == len(list_of_friends)-1:
            print("Not found")
            break
