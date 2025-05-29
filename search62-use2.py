import random
# 配列 0 番地未使用
# ランダムな51件のデータを生成し、ソートする
Cod = sorted(random.sample(range(100, 1000), 51))
# 0番地未使用のため、最初の要素は0にする
Cod[0] = 0
print(f'生成されたデータ（最初の50件のみ表示）: {Cod[1:51]}')
n = len(Cod) - 1
print(f'生成されたデータは、{n} 件です')

Str = int(input('数値を入力:'))
Lo = 1
Hi = n
Mid = (Hi + Lo) // 2
print(f'上限:{Hi} 下限:{Lo} 中央値:{Mid} 数値:{Str}')

# while Cod[Mid] != Str and Lo <= Hi:
while Lo <= Hi:
  if Cod[Mid] == Str:
    break

  if Cod[Mid] > Str:
    Hi = Mid - 1
  else:
    Lo = Mid + 1
  Mid = (Hi + Lo) // 2
  print(f'上限:{Hi} 下限:{Lo} 中央値:{Mid} 数値:{Str}')

if Hi >= Lo and Cod[Mid] == Str:
  print("該当データあり")
else:
  print("該当データなし")