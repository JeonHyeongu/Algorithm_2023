n, s = int(input()), list(input())
score, bonus = 0, 0
# print(s)

for i in range(len(s)):
    if s[i] == 'X':
        bonus = 0
    else:
        bonus += 1
        score += i + bonus

print(score)