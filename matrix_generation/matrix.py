import random


def generate_three_digit_codes(total):
    rep_num = random.randint(1, 10)

    find_num = random.randint(100, 999)

    final = []
    for _ in range(0, total):
        new_num = random.randint(100, 999)
        final.append(new_num)

    for _ in range(0, rep_num):
        rand_pos = random.randint(0, total - 1)
        final[rand_pos] = find_num

    return final, find_num


def generate_matrix(total_mat, rounds):
    nums = {}
    finds = []
    for i in range(1, rounds + 1):
        nums[i], find = generate_three_digit_codes(total_mat)
        finds.append(find)

    print(nums)
    print(finds)


def print_checkbox(num):
    for i in range(0, num):
        print("cb_" + str(i) + " = make_checkbox()")


rounds = 100
max_size = 17 * 17
generate_matrix(max_size, rounds)
print_checkbox(max_size)
