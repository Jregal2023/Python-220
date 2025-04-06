
#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        begin = 0
        end = len(arr) - 1
        result = 1
    
        while begin <= end:
            mid = begin + (end - begin) //2
        
            if arr[mid] == k:
                result = mid
                end = mid -1
            elif arr[mid] < k:
                begin = mid + 1
            else:
                end = mid -1
    
        return result
            


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends