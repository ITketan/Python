""" 7)
Create simple set and add value,
remove specific value(using discard and remove both function),
clear set(using it's function)
"""
#create simple set and add value
set1 = set(["ketan","gohel","Hello"])
print(set1)

#remove specific value(using discard and remove both function)
def Remove(set1):
    set1.discard("gohel")
    print(set1)
Remove(set1)

def Remove(set1):
    set1.remove("ketan")
    print(set1)
Remove(set1)


