# Basic solution:
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return less + equal + greater
    
## Intermediate solution:
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        pivot_count = nums.count(pivot)
        
        left = 0
        right = 0
        
        for num in nums:
            if num < pivot:
                result[left] = num
                left += 1
            
        right = left + pivot_count
        
        for num in nums:
            if num > pivot:
                result[right] = num
                right += 1
                
        while pivot_count:
            result[left] = pivot
            left += 1
            pivot_count -= 1
        
        return result
    
## Advanced solution:
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
                n = len(nums)
        result = [pivot] * n

        left = 0
        right = n - 1

        for i in range(n):
            if nums[i] < pivot:
                result[left] = nums[i]
                left +=1

        for i in range(n-1, -1, -1):
            if nums[i] > pivot:
                result[right] = nums[i]
                right -= 1
        return result