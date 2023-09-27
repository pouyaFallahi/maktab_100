import argparse
parser = argparse.ArgumentParser(description='average numbers')
parser.add_argument('-g', '--grades',help= 'pleas enter your numbers', type= int, nargs= '+')
parser.add_argument('-f', '--float', help= 'Display the decimal number of the answer (decimal by default = 2)',type= int, default=2)
arg = parser.parse_args()

number = sum(arg.grades) / len(arg.grades)
print(round(number,arg.float))



