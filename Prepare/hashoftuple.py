#in python2 input is written as raw_input

n = int(input())
integer_list = map(int, input().split())
t  = tuple(integer_list)
print(hash(t))
