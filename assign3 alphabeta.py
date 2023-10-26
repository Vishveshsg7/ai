#ASMT 3
MAX, MIN = 1000, -1000

def minimax(depth, depth_limit, nodeIndex, maximizingPlayer,
   values, alpha, beta):


   if depth == depth_limit:
       return values[nodeIndex]

   if maximizingPlayer:
   
       best = MIN

       # Recur for left and right children
       for i in range(0, 2):

           val = minimax(depth + 1, depth_limit, nodeIndex * 2 + i,
                   False, values, alpha, beta)
           best = max(best, val)
           alpha = max(alpha, best)

           # Alpha Beta Pruning
           if beta <= alpha:
               break

       return best

   else:
       best = MAX

       # Recur for left and
       # right children
       for i in range(0, 2):

           val = minimax(depth + 1, depth_limit, nodeIndex * 2 + i,
                       True, values, alpha, beta)
           best = min(best, val)
           beta = min(beta, best)

           # Alpha Beta Pruning
           if beta <= alpha:
               break

       return best


values = []
depth_limit = int(input("Enter the depth of tree: "))
for i in range(0,2**depth_limit):
   value = int(input(f"Enter value {i+1}: "))
   values.append(value)

print("The optimal value is :", minimax(0, depth_limit, 0, True, values, MIN, MAX))