transactions = [5000, -2000, 3000, -1000, -500, 7000]

# 4. Create separate lists for deposits and withdrawals
deposits = [t for t in transactions if t > 0]
withdrawals = [t for t in transactions if t < 0]

# 1. Calculate the current balance
current_balance = sum(transactions)

# 2. Count total deposits and withdrawals
total_deposits = len(deposits)
total_withdrawals = len(withdrawals)

# 3. Find the largest deposit and largest withdrawal
largest_deposit = max(deposits) if deposits else 0
largest_withdrawal = min(withdrawals) if withdrawals else 0

# Display results
print(f"Current Balance: {current_balance}")
print(f"Total Deposits: {total_deposits}")
print(f"Total Withdrawals: {total_withdrawals}")
print(f"Largest Deposit: {largest_deposit}")
print(f"Largest Withdrawal: {largest_withdrawal}")
print(f"Deposits List: {deposits}")
print(f"Withdrawals List: {withdrawals}")