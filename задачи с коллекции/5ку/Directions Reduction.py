def dirReduc(arr):
    a = 'NORTH SOUTH'
    b = 'EAST WEST'
    c = 'SOUTH NORTH'
    d = 'WEST EAST'
    st_arr = ' '.join(arr)
    while (a in st_arr) or (c in st_arr) or (b in st_arr) or (d in st_arr):
        st_arr = ' '.join(st_arr.replace(a, '').replace(b, '').replace(c, '').replace(d, '').split())
    return st_arr.split()


