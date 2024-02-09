import sys



args = [int(arg) for arg in sys.argv[1:] if arg.isnumeric()==True]
print(sum(args))

