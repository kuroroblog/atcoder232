import collections

# 標準入力を受け付ける。
H, W = map(int,input().split())
C = [input() for _ in range(H)]

ans = 1
seen = [list(-1 for _ in range(W)) for _ in range(H)]
todo = collections.deque()
todo.append((0, 0))
seen[0][0] = 1

while len(todo) != 0:
    # 参考 : https://note.nkmk.me/python-collections-deque/
    h, w = todo.popleft()
    for d in [[1, 0], [0, 1]]:
        if h + d[0] < H and w + d[1] < W:
            # なぜ一度確認した箇所を確認しなくていいのか？ ⏩ 左や上へ戻る操作がないため。一度踏んでいた場合、再度同じ箇所を踏んだとしても同じ回数でたどり着いたことになるので、確認する必要がない。
            if seen[h + d[0]][w + d[1]] != -1 or C[h + d[0]][w + d[1]] == '#':
                continue
            else:
                todo.append((h + d[0], w + d[1]))
                seen[h + d[0]][w + d[1]] = seen[h][w] + 1
                ans = max(ans, seen[h + d[0]][w + d[1]])

print(ans)
