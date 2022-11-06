def run():
    my_list = [1,2,4,6,7,9]

    odd = list(map(lambda x: x**2,my_list))

    print(odd)


if __name__ =='__main__':
    run()