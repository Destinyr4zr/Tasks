stri = input()
i=1
j=1
base ={0:stri[0]}
while i<=len(stri)-2:
    if(stri[i-j]==stri[i+j]):
        while not i-j==0 and not i+j==len(stri)-1 and stri[i-j]==stri[i+j]:
            j+=1
        if (stri[i-j]!=stri[i+j]):
            j-=1
        base[i-j]=stri[i-j:i+j+1]
        j=1
    i+=1
maxi=-1
reskey=-1
for key,el in base.items():
    if(len(el)>maxi):
        reskey=key
        maxi=len(el)
print(maxi)
print(base[reskey])
