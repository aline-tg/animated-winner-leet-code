class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result_list = []
        for i in range(0, len(accounts)):
            wealth = sum(accounts[i])
            result_list.append(wealth)
        return max(result_list)