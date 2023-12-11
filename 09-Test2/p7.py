def f(arr: list):
    count = 0 
    for i in arr:
        low = 0
        nums = 0
        if  4 <= len(i) <= 12:
            if '_' in i:
                for j in i:
                    j = str(j)
                    if j.isdigit():
                        nums += 1
                    elif j.isupper():
                        break
                    elif j.lower():
                        low += 1
                if nums != 0 and low != 0:
                    count += 1
    return count

print(f(["an_nm3ay"]))