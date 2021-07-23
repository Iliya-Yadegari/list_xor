def list_xor(n,lst1,lst2):
    score_counter = 0   
    for i in lst2: 
        lst1.append(i) 
    for i in lst1:
        if i == n:
            score_counter += 1
    if score_counter != 1:
        print('False')
    else:
        print('True')

list_xor(1,[1,2,3],[1,5,6])