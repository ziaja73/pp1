def f(arr: list):
    count = 0 
    for i in arr:
        low = 0
        nums = 0
        if  4 <= len(i) <= 12:
            if '_' in i:
                for j in i:
                    if j.isdigit():
                        nums += 1
                    elif j.lower():
                        low += 1
                if nums != 0 and low != 0:
                    count += 1
    return count

print(f(["uek","water_2_x","an_nam3ay","a_b_c_d_e_f"]))