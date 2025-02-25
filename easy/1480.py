class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums)):
            soma = sum(nums[:i+1])
            result.append(soma)
        return result