# kwrags = key words aguments
# Args = non key word arguments  any number of arguments

# def sum_of (a,b):
#     return a + b

# print(sum_of(4,5,6))

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4,5,6,4,5,6))


def sum_of(**kwrags):
    sum = 0
    for x in kwrags.items():
        sum += x
    return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.99))

