#-*-coding:utf-8-*-
# Author:Lu Wei
'''
v = 'ALEX'
v1 = v.upper()
print(v1)
v2=v.isupper()# 判断是否全部是大写
v2=v.islower()
print(v2)

############ 了解即可
v = 'ß'
# 将字符串变小写（更牛逼）
v1 = v.casefold()
print(v1) # ss
v2 = v.lower()
print(v2)


#v='1'
#v='一'
v='A'
v1=v.isdigit()      #'1'-->True，'一'-->False，'①'-->True
v2=v.isdecimal()    #'1'-->True，'一'-->False，'①'-->False
v3=v.isnumeric()    #'1'-->True，'一'-->True，'①'-->True
print(v1,v2,v3)

v='alexok\t'
print(v.strip())
v='alexok\n'
print(v.strip())
v='alexok     '
print(v.strip())


v='asdwqexzc'
v1='QasaWd'
v='asdwqexzc'
print(v.capitalize())
v1='QasaWd'
print(v1.casefold())#返回将字符串中所有大写字符转换为小写后生成的字符串。

v='lasdsadasdw'
index=v.index('a',2)
print(index)
print(v.count('a'))
print(v.center(20,'+'))
print(v.ljust(20,'+'))

v='我是{0}，今年{1}'.format('luwei',18)
print(v)
v='我是{k1}，今年{k2}'.format_map({'k1':'luwei','k2':'18'})
print(v)
v='asd12jkgygfj1fgfgj1jhg'
print(v.partition('1'))

v='AJaw'
print(v.zfill(10))

a='1234'
b='abcd'
table=str.maketrans(b,a)
v='asdawqeqrqasdasdaswq'
r=v.translate(table)
print(r)


# l=[]
# v='asdqwe'
# for i in v:
#     l.append(i)
# print(l)

l=['a', 's', 'd', 'q', 'w', 'e']
l.reverse()
print(l)

l1=['1','2',1,2,3]
l2=['a','v','g']
l1.extend(l2)
print(l1)
l=['a', 's', 'd', 'q', 'w', 'e']
l.sort(reverse=True)
print(l)


d={'k1':'v1','k2':'v2','k3':'v3'}
d.pop('k1')
print(d)

d={'k1':'v1','k2':'v2','k3':'v3'}
d.clear()
print(d)


l=['a', 's', 'd', 'q', 'w', 'e']
del l[0]
print(l)

s={'a','v','b','q','w'}
s1={'q','v','b','w','k'}
s.discard(s1)
print(s)

obj=open('a.text',mode='a',encoding='utf-8')
while True:
    val=input('----')
    obj.write(val)
    obj.flush()
obj.close()
'''

with open('a.text',mode='r',encoding='utf-8') as f1:
    data=f1.read()
    new_data=data.replace('达啊','666')
with open('a.text',mode='w',encoding='utf-8') as f2:
    f2.write(new_data)



