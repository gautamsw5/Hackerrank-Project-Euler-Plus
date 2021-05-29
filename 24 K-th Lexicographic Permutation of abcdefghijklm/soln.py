# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
1. Build a list of all elements in ascending order.
The length of this list is n (i.e. not the original input size).
2. Given k we know what the first element will be in the kth permutation of the current list.
There are n groups in the lexicographical order of all permutations of the list. Inside a group each permutation's first element is the same. Each group has (n-1)! elements, so an easy k / (n-1)! will give us the index.
3. Append the selected element to the result, i.e. the next element in the kth permutation.
4. Remove the selected element from the list.
5. Now the list has one less elements (n has decremented) and we can repeat from Step 2 with k' = k % n!,
that is the k'th permutation of the reduced list.
'''
fact=[0,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020799]
def kthPerm(s,k,ans):
    if len(s)==0:
        #print("0",ans)
        return ans
    if len(s)==1:
        ans.append(s[0])
        #print("1",ans)
        return ans
    i=k//fact[len(s)-1]
    ans.append(s[i])
    s=s[:i]+s[i+1:]
    #print(ans)
    return kthPerm(s,k%fact[len(s)],ans)
t=int(input())
for i in range(t):
    n=int(input())-1
    s="abcdefghijklm"
    ans=kthPerm(list(s),n,[])
    s=""
    for i in ans:
        s=s+i
    print(s)
