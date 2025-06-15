arr = [1, 2, 3, 4, 5]
inv_arr = arr[ : :-1]
#             | |  |
#     beggining |  step
#              end
# if the fields are blank the default is
# beggining = 0
# end = end (position -1)
# step = one by one backwards


print(inv_arr)
print(arr[0:4])
