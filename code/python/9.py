# 내장함수
number = [10, 20, 30, 40]
print(sum(number))

scores = {"국어" : 83, "영어" : 90, "수학" : 95}
print(scores.values())
total_score = sum(scores.values())
print(total_score)

print(max(number))
print(min(number))

print(max(scores.values()))
print(min(scores.values()))

names = ["Alice", "Bob", "Charlie","Lily"]
scores = [85, 90, 95, 100, 105]
zipped = list(zip(names, scores))
zipped2 = dict(zip(names, scores))
print(zipped)
print(zipped2)