def get_longest_name(names_list):

    longest_name = ""
    for name in names_list:
        if len(name)>len(longest_name):
            longest_name = name

    return longest_name

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

big_name = get_longest_name(names_list)
print(big_name)






