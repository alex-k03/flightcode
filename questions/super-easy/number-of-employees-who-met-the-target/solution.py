def number_of_employees_who_met_the_target(hours, target):
    return sum(hour >= target for hour in hours)
