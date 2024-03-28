# custion function


developer = ['imran ', 'saqlain', 'rashid', 'irfan']

def reverse(str):
    return str[::-1]


all_developer = map(reverse, developer )

# for x in all_developer:
    # print(x)


# build in  function 


# print(sorted(developer))


# pure function 

global_list = [1,2,3]

# def add(item):
#     global_list.append(item)

# add(4)
# print(global_list)
# so this is a not pure function because it make changes to global_list


def add(gl , item):
    nl = gl.copy()
    nl.append(item)
    return nl

new_list =  add(global_list,4)
print(global_list)
print(new_list)