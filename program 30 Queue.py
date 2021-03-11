from collections import deque
bank =deque (['bijoy','joy','jui','rahat'])
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()
#print(bank)
if not bank:
    print("not there")