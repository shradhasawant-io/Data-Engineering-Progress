class InsufficientBalanceError(Exception):
    pass
balance = 100
withdraw_amount = 1000
if withdraw_amount > balance:
    raise InsufficientBalanceError("Not enough balance") 