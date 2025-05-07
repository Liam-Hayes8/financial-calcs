#calculators.py

def mortgage_payment(principal, annual_rate, years):

    """
    Return the monthly principal and interest payment

    :param principal:           --The loan the amount in dollars
    :param annual_rate:         --APR as a percent (Ex: 6.5 for 6.5%)
    :param years:               --The loan term in years
    :return:
    """
    monthly_rate = annual_rate / 100 / 12               #Percent to decimal to monthly
    months = years * 12

    if monthly_rate == 0:                               #0 % loan edge case
        return principal / months

    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)

def retirement_401k(balance, yearly_contrib, annual_return, years):

    """
    The future value of a 401k with annual contributions

    :param balance:             --Current balance
    :param yearly_contrib:      --Dollars added each year
    :param annual_return:       --Expected annual return, percent
    :param years:               --Years until retirement
    :return:
    """

    r = annual_return / 100

    #Growth on existing balance
    fv_balance = balance * (1 + r) ** years

    #Future value of a series of equal yearly contributions
    fv_contrib = yearly_contrib * (((1 + r) ** years - 1) / r)

    return fv_balance + fv_contrib

def tax_liability(income, status="single"):
    """
    Simple 2024 U.S. federal tax (just a few brackets).

    :param income:              --Taxable income in dollars
    :param status:              --"single" or "married"
    :return:
    """

    brackets = {
        "single": [
            (11_000, 0.12),             # 10%
            (44_725, 0.22),             # 12%
            (95_375, 0.24),             # 22%
            (float('inf'), 0.24)        # 24%
        ],
        "married": [
            (22_000, 0.12),
            (89_450, 0.22),
            (190_750, 0.24),
            (float('inf'), 0.24),
        ],
    }

    owed = 0
    last_cut = 0

    #Loop through tax brackets in ascending order, calculate tax owed
    for upper, rate in brackets[status]:
        taxable = min(income, upper) - last_cut
        if taxable > 0:
            owed += taxable * rate
            last_cut = upper
        if income <= upper:
            break

    return owed
