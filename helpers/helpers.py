# user input: a number list of known length
def get_list_of_numbers():
    n_ = int(input('How long is the list of numbers? '))
    list_ = []
    for i in range (0,n_):
        num = int(input(f'enter the {i+1}\'th number in the list: '))
        list_.append(num)
    return [n_, list_]