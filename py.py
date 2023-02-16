N_str_origin = input()
N_int = int(N_str_origin)
N_str = N_str_origin


N_cut_int = []
i = 0
j = 0
k = 0
cnt = 0
hap = 0
if N_int < 10:
    N_str = N_str + str(0)


while cnt<10:

    cnt = cnt + 1
    for i in range(len(N_str)):
        N_cut_int.append(int(N_str[i]))

    for j in range(len(N_cut_int)):
        hap = hap + N_cut_int[j]
    hap_str = str(hap)

    if len(hap_str) < 2:
        N_str_new = N_str[1] + hap_str
        # print(N_str_new)
        # breakpoint()
        if N_str_new != N_str_origin:
            N_str = N_str_new

        else:
            break
    elif len(hap_str) == 2:
        N_str_new = N_str[1] + hap_str[1]
        if N_str_new != N_str_origin:
            N_str = N_str_new
        else:
            break

print(cnt)


