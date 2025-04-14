
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


#ListSort

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        length = len(arr)
        begin = 0
        end = length - 1
        mid = 0
        
        while mid <= end:
           # mid -left + (right - left) //2
            
            if arr[mid] == 0:
                arr[begin], arr[mid] = arr[mid], arr[begin]
                begin = begin + 1
                mid = mid + 1
            elif arr[mid] == 1:
                mid = mid + 1
            else: 
                arr[end], arr[mid] = arr[mid], arr[end]
                end = end -1
        return arr

obj = Solution()
arr =  [0,1,2,0,1,2]
arr = obj.sort012(arr)
alist = []   
for i in arr:
    alist.append(i)

#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        begin = 0
        end = len(arr) - 1
        result = -1
    
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