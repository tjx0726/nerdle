import itertools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers = list(map(str, numbers))
ops = ["+", "-", "*", "/"]

def check_op(l):
    l = list(l)
    if l[0] in ops:
        return True
    for i in range(len(l)-1):
        if l[i] in ops and l[i+1] in ops:
            return True
    return False

def check_zero(l):
    l = list(l)
    for i in range(len(l)-1):
        if l[i] == "0" and l[i+1] == "0":
            if i == 0 or l[i-1] in ops:
                return True
    return False



all_list = []
for i in range(1, 7):
    print(f"i={i}")
    iterList1 = []
    for j in range(i):
        iterList1.append(numbers+ops)
    for l in itertools.product(*iterList1):

        if check_op(l) or check_zero(l):
            pass
        else:

        
            try:
                temp = eval("".join(l))
                round_temp = round(temp)
                if abs(temp-round_temp) < 0.00001:
                    if len(l) + len(str(round_temp)) == 7 and temp > 0 :
                        all_list.append((l, round_temp))
            except:
                pass


print(len(all_list))


import pickle

with open("all_list.pkl", "wb") as f:
    pickle.dump(all_list, f)



