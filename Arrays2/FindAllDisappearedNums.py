class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [] # Create an empty array
        
        for i in range(len(nums)):  # Run until the length
            index = abs(nums[i])-1  # Create index with absolute value of nums[i]-1
            
            if nums[index] < 0: # if the nums[index] is less than 0
                continue
            nums[index] *= -1   # multiply nums[index] with -1
                
        for j in range(len(nums)):  # run until the length
            if nums[j] > 0: # if nums[j] is greater than 0 
                result.append(j+1)  # append the values in the array
        return result   # return result
        
