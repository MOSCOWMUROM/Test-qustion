def min_paint_cells(n, k, stripe):
    min_white = float('inf')
    current_white = 0

    # Первоначальный подсчет белых клеток в первоночальном окне длиной k
    for i in range(k):
        if stripe[i] == 'W':
            current_white += 1

    min_white = current_white

    # Использование скользящего окна для подсчета белых клеток в каждом окне длиной k
    for i in range(k, n):
        if stripe[i] == 'W':
            current_white += 1
        if stripe[i - k] == 'W':
            current_white -= 1

        min_white = min(min_white, current_white)

    return min_white


# Чтение входных данных
t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    stripe = input().strip()
    result = min_paint_cells(n, k, stripe)
    results.append(result)

# Вывод результатов
for res in results:
    print(res)
