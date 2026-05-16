# # List comprehension practice
# # dictionary comprehension practice
# result = {x**2 for x in range(10) if x%2 == 0}
# print(result)

# list1=['id', 'name', 'age']
# list2=[1, 'John', 25]
# result={k:v for k,v in zip(list1,list2)}
# print(result)
# result1={list1[i]:list2[i] for i in range(len(list1))}
# print(result1)

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# flat=[]
# for row in matrix:
#     for num in row :
#         flat.append(num)
# print(flat)

# names=['Alice', 'Bob', 'Charlie']
# for name in names:
#    if len(name)>3:
#       print(name.upper())
# upper_names = [name.upper() for name in names if len(name) > 3]
# print(upper_names)

# lambda function practice
# square = lambda x: x**2
# print(square(10))

# add = lambda a,b:a+b
# print(add(5,8))

# odd = lambda x: x%2 !=0
# print(odd(7))

# # Sort a list of tuples based on the second element
# data = [(1, 'apple'),  (2, 'cherry'),(3, 'banana'),(4, 'date')]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)

# # Map  apply function to each element in a list
# prices= [10, 20, 30, 40]
# discounted_prices = lambda x: x*0.9
# print(discounted_prices(prices[1]))

# discounted_prices_list = [x * 0.9 for x in prices if x % 20 == 0]
# print(discounted_prices_list)

# discounted_prices_map = list(map(lambda x:x*0.9,prices))
# print(discounted_prices_map)

# original_values = {"a": 1, "b": 2, "c": 3}
# swapped = {v:k for k,v in original_values.items()}
# print (swapped)

# Iterators and generators practice

# nums = [1, 2, 3, 4, 5]
# it = iter(nums)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break


class countdown:
    def __init__(self,start,stop=0):
        self.current=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <=self.stop:
            raise StopIteration
        val = self.current
        self.current -=1
        return val

for num in countdown(10,5):
    print(num,end=' ')    