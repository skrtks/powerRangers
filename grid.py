grid = []
for j in range(5):
    grid.append([i * j for i in range(5)])

for row in grid:
    print(row)
