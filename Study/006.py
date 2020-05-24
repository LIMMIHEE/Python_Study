name = 'mihee'
age = 15

print('{0:^15}'.format(name)) #15자리 중앙정렬을 해라
print('{0:<15}'.format(name)) #15자리 왼쪽정렬을 해라
print('{0:>15}'.format(name)) #15자리 오른쪽정렬을 해라

print('{0:*^15}'.format(name)) #15자리 중앙정렬을 해라 남은 공간에는 * 넣어라

print(f'제 이름은 {name}입니다 나이는 {age}입니다')