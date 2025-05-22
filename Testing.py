def spiral_order_matrix(N):
  matrix=[[0] * N for _ in range(N)]
  top,bottom= 0,N-1
  left,right = 0,N-1
  num=1

  while top<=bottom and left<=right:
    for i in range(left,right + 1 ):
      matrix[top][i]=num
      num=num+1
    top=top+1

    for i in range(top,bottom + 1):
      matrix[i][right]=num
      num=num+1
    right=right-1

    if top<=bottom:
      for i in range(right,left-1,-1):
        matrix[bottom][i]=num
        num=num+1
      bottom=bottom-1

    if left<=right:
      for i in range(bottom,top-1,-1):
        matrix[i][left]=num
        num=num+1
      left=left+1
  
  return matrix 


result=spiral_order_matrix(5)
for row in result:
  print(row)
