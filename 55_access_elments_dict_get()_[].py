#get vs [] for retrieving elements
my_dict = {'name':'jack','age':26}

#output:jack
print(my_dict['name'])

#output:26
print(my_dict.get('age'))

#trying to access keys which doesn't exist throws error
#output none
print(my_dict.get('address'))

#keyError
print(my_dict['address'])
