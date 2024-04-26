

def knapsack(w,wt,v,n):
    if(n == 0 or w == 0):
        return 0

    if(wt[n-1]>w):
        return(knapsack(w,wt,v,n-1))

    return(max(knapsack(w,wt,v,n-1), knapsack(w-wt[n-1],wt,v,n-1)+v[n-1]))

if __name__ == '__main__':
    print('0/1 Knapsack Problem using recursion')
    print("Enter the maximum capacity of the knapsack")
    w = int(input())
    v = [int(x) for x in input("Enter the items in value array: ").split()]
    wt = [int(x) for x in input("Enter the weight for the corresponding values: ").split()]
    n = len(v)
    answer = knapsack(w,wt,v,n)
    print("Answer = : ", answer)

#Time complexity = O(2^n)

