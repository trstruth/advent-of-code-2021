fish_counts = [0] * 9

map(lambda x: fish_counts[x].increment, [int(x) for x in input().split(',')])

for _ in range(256):
    spawners = fish_counts.pop(0)
    fish_counts[6] += spawners
    fish_counts.append(spawners)

print(sum(fish_counts))
