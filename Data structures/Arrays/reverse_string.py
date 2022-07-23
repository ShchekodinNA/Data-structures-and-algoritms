from numpy import split


def reverse(str:str) ->str:
    if len(str) < 2:
        return str
    res = []
    for i in range(len(str)-1, -1, -1):
        res.append(str[i])
    return "".join(res)



newstr = reverse("te")

print(newstr)