from functools import reduce
def run():
    my_list = [2,2,2,2,2]

    all_multiplied = reduce(lambda a,b: a * b,my_list)
    print(all_multiplied)

if __name__=='__main__':
    run()