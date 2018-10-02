import sys

if len(sys.argv) == 1:
    print("You need to specify a link")
    sys.exit(1)

for x in range(1, 51):
    print('{}&s={}'.format(sys.argv[1], x))
