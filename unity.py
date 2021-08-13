# author : Sarvin Nami
names = ['Sarvin','Abtin','Nazanin','Arash','Tufan','Baran','Ahu','Sepehr','Sahel','Darya']
secondNames = [ ]
# for x in names :
#     if x[-1] == 'n':
#         secondNames.append(x)
# print(secondNames)
thirdNames = ['Sarvin','Abtin','Ahu','Siavash','Mozhgan','Bahram']
for x in names :
    for y in thirdNames:
        if x == y :
            secondNames.append(x)
print(secondNames)