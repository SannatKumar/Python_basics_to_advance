# Here we add the two list and square the sum and add it again to gain a single value
first_list=[2, 4, 8]
second_list=[5, 2, 1]
final_list=0
for i,j in zip(first_list, second_list):
    sum = (i+j)**2
    final_list = final_list+sum
print(final_list)
