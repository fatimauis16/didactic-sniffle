def most_frequent(string):
    D=dict()
    for i in string:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
    return D
var=(most_frequent('Mississippi'))
list =(var.keys())
list =zip(var.values(),var.keys())
print(sorted(list,reverse=True))
