# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

even_list =list(filter(lambda x:(x%2 ==0) , my_list)) 
odd_list = list(filter(lambda x: (x%2 == 1) , my_list))

print("Even Numbers are",even_list)
print("Odd Numbers are",odd_list)
