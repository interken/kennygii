print("hello world")
#the list for the wedding
items = ['yam', 'rice', 'cow', 'palmoil']
print(items)
items.append ('groundnut oil')
print(items)
items.insert (0,'chicken')
print(items)
del items[2]
print(items)
del items[4]
print(items)
items.remove('palmoil')
print(items)
#sorting a list
fruits=['apple', 'pineapple', 'orange', 'strawberry', 'banana']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#slice
fruits=['apple', 'pineapple', 'orange', 'strawberry', 'banana']
print(fruits[:4])
print(fruits[1:])
#for loop
students=['femi', 'emmanuel', 'kenny', 'john']
for student in students:
    print(student)
for value in range (1,11):
    print(value)
    numbers=list(range(0,10))
    print(numbers)
    even_numbers=list(range(2,11,2))
    print(even_numbers)
    odd_numbers=list(range(1,15,2))
    print(odd_numbers)   
    dimension=('john', 'esther') 
    print(dimension)
    
