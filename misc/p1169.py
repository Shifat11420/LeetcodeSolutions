# A transaction is possibly invalid if:
# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.
# Return a list of transactions that are possibly invalid. You may return the answer in any order.

# Example 1:
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

# Example 2:
# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]

# Example 3:
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]

# Time: O(n), Space: O(n)
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions.sort(key = lambda t: int(t.split(",")[1]))
        name2q = defaultdict(lambda : deque())
        invalid = [False]*len(transactions)
        res = []

        for i in range(len(transactions)):
            t = transactions[i]
            name, time, amount, city = t.split(",")
            time = int(time)
            amount = int(amount)

            q = name2q[name]
            while q and time-q[0][0]>60:
                q.popleft()

            curInvalid = amount>1000
            for t, othercity, j in q:
                if city != othercity:  
                    curInvalid = True
                    if not invalid[j]:
                        invalid[j] = True
                        res.append(transactions[j])

            if curInvalid:
                invalid[i] = True
                res.append(transactions[i])          

            name2q[name].append((time, city, i))
        return res    


        