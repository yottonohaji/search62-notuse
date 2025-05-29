import random
# 配列 0 番地使用
# データを配列に設定する
Num = [100, 228, 237, 290, 315, 358, 409, 413, 626, 631, 927, 962, 967, 988]
print(f'データの確認: {Num[0:11]}')
n = len(Num) 
print(f'探索するデータは、{n} 件です')

Str = int(input('数値を入力:'))
Lo = 0
Hi = n - 1
Mid = (Hi + Lo) // 2
print(f'上限:{Hi} 下限:{Lo} 中央:{Mid} 中央値:{Num[Mid]} 数値:{Str}')

# while Num[Mid] != Str and Lo <= Hi:
while Lo <= Hi:  
  if Num[Mid] == Str:
    print("データを見つけたよ!")
    break
  
  if Num[Mid] > Str:
    Hi = Mid - 1
  else:
    Lo = Mid + 1
  Mid = (Hi + Lo) // 2
  print(f'上限:{Hi} 下限:{Lo} 中央:{Mid} 中央値:{Num[Mid]} 数値:{Str}')

if Hi >= Lo:
    print("該当データあり")
else:
    print("該当データなし")
