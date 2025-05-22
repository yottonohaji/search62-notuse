import random
# 配列 0 番地未使用
# データを配列に設定する
# 0番地未使用のため、最初の要素は0にする
Cod = [0, 228, 237, 290, 358, 409, 413, 626, 631, 927, 962]
print(f'データの確認: {Cod[1:11]}')
n = len(Cod) - 1
print(f'探索するデータは、{n} 件です')

Str = int(input('数値を入力:'))
Lo = 1
Hi = n
Mid = (Hi + Lo) // 2
print(f'上限:{Hi} 下限:{Lo} 中央:{Mid} 中央値:{Cod[Mid]} 数値:{Str}')

# while Cod[Mid] != Str and Lo <= Hi:
while Lo <= Hi:  
  if Cod[Mid] == Str:
    print("データを見つけたよ!")
    break
  
  if Cod[Mid] > Str:
    Hi = Mid - 1
  else:
    Lo = Mid + 1
  Mid = (Hi + Lo) // 2
  print(f'上限:{Hi} 下限:{Lo} 中央:{Mid} 中央値:{Cod[Mid]} 数値:{Str}')

if Hi >= Lo:
    print("該当データあり")
else:
    print("該当データなし")
