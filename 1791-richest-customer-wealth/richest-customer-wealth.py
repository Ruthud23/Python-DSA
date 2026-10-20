class Solution:
    def maximumWealth(self, accounts):
        maximum = 0

        for customer in accounts:
            total = sum(customer)

            if total > maximum:
                maximum = total

        return maximum