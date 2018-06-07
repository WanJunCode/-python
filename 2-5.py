
# 使用 *3 +1 都会返回新的对象
board = [['_']*3 for i in range(3)]
print(board)
board[0][0]='x'
print(board)

print()
# ['_'] 不是引用 [['_','_','_']] 是引用
# 后面的 *3 会导致三个相同的引用
weird_board = [['_']*3] *3
print(weird_board)
weird_board[0][2]='x'
print(weird_board)

print()
# 列表中保存的是三个相同的引用
row = ['_']*3
board =[]
# 这种方式会 添加三个相同的引用
for i in range(3):
    board.append(row)
print(board)
board[0][0]='x'
print(board)

# 这种方式不会有错误
row = ['_']*3
print(row)
row[0]='x'
print(row)

print()
board=[]
for i in range(3):
    row = ['_']*3
    board.append(row)
print(board)
board[0][0]='x'
print(board)