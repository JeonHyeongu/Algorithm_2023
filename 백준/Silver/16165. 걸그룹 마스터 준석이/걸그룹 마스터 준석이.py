n, m = map(int, input().split())
group_name, name_group = {}, {}

for i in range(n):
    group, count = input(), int(input())
    group_name[group] = []
    for j in range(count):
        name = input()
        group_name[group].append(name)
        name_group[name] = group

for k in range(m):
    q_name, q_num = input(), int(input())
    if q_num == 1:
        print(name_group[q_name])
    else:
        for m in sorted(group_name[q_name]):
            print(m)