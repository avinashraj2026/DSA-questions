#In the recursive solution we saw that the value of w and n were changing so we create a 2D array to store these changes
def knapsack(w,wt,v,n):
    dp = [[0 for j in range(w+1)] for i in range(n+1)] #i is outer loop j is inner loop
    #[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #dp[i][j] -> maximum value that we can first i items and knapsack capacity j
    #columns represent knapsack capacity and rows represent number of items

    #Using the same recursion logic in a loop
    for i in range(1,n+1):
        for j in range(1,w+1):
            if(wt[i-1]>j):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],v[i-1] + dp[i-1][j-wt[i-1]])
    return dp[n][w]

if __name__ == '__main__':
    print('0/1 Knapsack Problem using recursion')
    print("Enter the maximum capacity of the knapsack")
    w = int(input())
    v = [int(x) for x in input("Enter the items in value array: ").split()]
    wt = [int(x) for x in input("Enter the weight for the corresponding values: ").split()]
    n = len(v)
    answer = knapsack(w,wt,v,n)
    print("Answer = ", answer)

#Time complexity = O(n*w)
#For very large values of w the recursive solution is faster
