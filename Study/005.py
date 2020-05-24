name = 'mihee'
age=19
n=99999999999.999999999
print('내 이름은%s 나이는%d 입니다' %(name, age))
print('내 이름은{} 나이는{} 입니다'.format(name,age))
print('내 이름은{0} 나이는{0} 입니다'.format(name,age)) #인덱스 값으로 설정도 가능하다.

s = '제 이름은{name}입니다 제 나이는 {age}입니다'
print(s.format(name='mihee', age=18))

print('{0:4} X {1:4} = {2:4}'.format(2,3,6)) #오른쪽 정렬으로 4칸의 공간에 값을 넣겠다.
print('{0:<4} X {1:<4} = {2:<4}'.format(2,3,6)) #왼쪽 정렬으로 4칸의 공간에 값을 넣겠다.

print('{0:.3f}'.format(1/4.0))
print('{0:.4f}'.format(1/4.0))
print('{0:,.3f}'.format(n)) #3자리마다 ,를 넣겠다?