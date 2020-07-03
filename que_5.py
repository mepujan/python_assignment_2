# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

personal_info=('pujan','gautam',23)
people=[]
people.append(personal_info)
people.append(('ram','shrestha',20))
people.append(('aakash','maharjan',25))
people.append(('sneha','bhandari',18))
people.append(('bijay','khanal',27))
print("Before Sorting : ",people)
people.sort(key= lambda x: x[2])  #Sorting using age
print('After Sorting: ',people)



