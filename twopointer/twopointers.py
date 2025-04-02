class TwoPointer:
    
    def __init__(self):
        pass

    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = len(nums)
        result = set()
        for i in range(0,l-2):
            low = i+1 
            high = l-1 
            if nums[i] > 0:
                break 
            while low < high:
                sum = nums[i]+ nums[high] + nums[low]
                if sum >0:
                    high = high -1 
                elif sum < 0:
                    low = low+1 
                else:
                    if sum ==0:
                        result.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low = low+1 
                    while low < high and nums[high] == nums[high-1]:
                        high = high-1 
            return list(result)


if __name__ == "__main___":
    tp = TwoPointer()
    tp.three_sum