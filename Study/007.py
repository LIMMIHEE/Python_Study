#변수의 타입

a = 10
b = 10.1
c = 'mirim'
d = True
e = [100,200,300]
f = (100,200,300)
g = {'one' : 1 , 'two':2}
h = {100,200,300,400}

print(type(a),type(b),type(c),type(d),type(e))
print(type(f),type(g),type(h))

print(c.isalpha) #이게 알파벳으로 구성되어 있느냐

'''
1. 공간 활용
2. 용도에 맞게 사용하며 유용한 기능 사용
3. 변수와 값은 모두 존재함
'''

print(dir(c)) #C 안에 들어있는 거 알려주는 그 타입에서 사용할 수 있는 기능들도 알려준다
