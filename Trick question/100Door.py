dict1 = {d : 'close' for d in range(1, 101)}
 
for k in range(1, 101):
    for key in dict1:
        if key % k == 0:
            dict1[key] = "open" if dict1[key] == "close" else "close"

open_door = [key for key, value in dict1.items() if value=="open"]
close_door = [key for key, value in dict1.items() if value=="close"]

print(f" Open Door ==> {open_door}")
print(f" close door ==> {close_door}")