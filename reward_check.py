
def find_best_user(file_path):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            fields = line.split(',')
            str = fields[5]
            print(str)
            result.append(str)

    print(result)
    print(max(result))
        # result = max(str)
        # print(result)




def test():
    result = find_best_user("users.txt")
    print(result)

test()



#read python files and start from last column to add numbers and add to array
# take max of array to find out the highest score