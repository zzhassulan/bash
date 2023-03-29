# def main(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#     return kwargs

# print(main(name= 'olzhas',age= 20, i=123 , a=123.123 , b=[1,2,3]))

# рекурсия 
# def rec():
#     return rec()
# rec()
# a = 10
# for i in a:
#     print(i)

# def rec_num(number:int):
#     if number == 0:
#         return 1
#     return number * rec_num(number - 1) 
# # print(rec_num(5))
# num = int(input("Введите число "))
# factorial = rec_num(num)
# print('Факториал числа', num, "равен", factorial)


def max_find_number(lists: list , n):
    if n == 0:
        return 'kuasyn da'
    
    if n == 1:
        return lists[0]
    
    return max(lists[n-1], max_find_number(lists, n-1))


arr = [1,2,3,4,5,6,7]
n = len(arr)
print(max_find_number(arr, n))

