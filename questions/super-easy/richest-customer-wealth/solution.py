def richest_customer_wealth(accounts):
    return max(sum(account) for account in accounts)
