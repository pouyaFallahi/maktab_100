import sys
my_list = [float(arg) for arg in sys.argv[1:]]
print('Average: {}'.format(sum(my_list) / len(my_list)))