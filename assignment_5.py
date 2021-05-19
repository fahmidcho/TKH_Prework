names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
even= []
odd = []
def even_odd_list(n):
    for x in n:
        if len(x)%2 == 1:
            odd.append(x)
        else:
            even.append(x)


even_odd_list(names_list)

new_even = []
new_odd = []

for ne in even:
    ne = "b" + ne[1:]
    new_even.append(ne)

for no in odd:
    x = len(no)-1
    no = no[0:x] + "c"
    new_odd.append(no)

print(new_even)
print(new_odd)