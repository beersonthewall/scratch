def exist(board, word):
  delta = [(1,0), (-1, 0), (0, 1), (0, -1)]
  for x in range(len(board)):
    for y in range(len(board[x])):
      if bfs((x,y), board, word):
        return True
  return False

def bfs(pt, board, word):
  pts = [pt]
  pos = 0
  seen = set()
  while pts:
    (x,y) = pts[-1]
    seen.add((x,y))
    print((x,y))
    if board[x][y] == word[pos] and pos == len(word) - 1:
      # found
      return True
    elif board[x][y] == word[pos]:
      # add pts
      pos += 1
      next_pts = map(lambda delta: (x + delta[0], y + delta[1]), [(1,0), (-1,0), (0,1), (0,-1)])
      valid_pts = filter(
        lambda p: 0 <= p[0] < len(board) \
                  and 0 <= p[1] < len(board[p[0]]) \
                  and (p[0],p[1]) not in seen, next_pts)
      pts.extend(next_pts)
    else:
      pts.pop()
  return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
