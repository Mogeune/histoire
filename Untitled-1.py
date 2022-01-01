def cree_list_iter(n):
    result=[0]
    while result != n:
        result = cree_list(n-1)
        return result+[n]
    return result  

def cree_list(n):
    result=[0]
    if n>=1:
        result = cree_list(n-1)
        return result+[n]
    return result

result = cree_list_iter(6)
assert result == [0,1,2,3,4,5,6]