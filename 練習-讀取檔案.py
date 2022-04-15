data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
print('檔案讀取完成，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])  # 列印第一筆有GOOD的留言
