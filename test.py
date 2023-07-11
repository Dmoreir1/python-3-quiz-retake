from ValidationException import ValidationException

def test(file_path):
    result = []
    file = open(file_path, 'r')
    for count, line in enumerate(file, start=2):
        user_data = line.strip().split(',')
        if len(user_data) == 1:
            first_name, rewards = user_data
        print(user_data)





        #
        # if count != 0:
        #     line_values = line.split(',')
        #     try:
        #         int(line_values[0])
        #         print(line_values[0])
        #     except:
                # raise ValidationException("--")

    file.close()


def ex():
    try:
        test("users.txt")
    except ValidationException as ve:
        print(ve)
ex()