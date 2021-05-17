import numpy_financial as np
import platform

def calcula_fv():
    rate = 3 / 100  # Given that fund is projected to earn 3% annually
    number_periods = 7  # Given that the client stays invested for 7 years
    pmt = 0  # Zero because there are no intermediate payments
    initial_investment = -2000000  # Negative because it's a cash outflow

    fv_of_portfolio = np.fv(rate=rate, nper=number_periods, pmt=pmt, pv=initial_investment)

    print('${:,.2f}'.format(fv_of_portfolio))

def calcula_pv():
    rate = 6 / 100  # Given that the investment earns 6% annually
    number_periods = 5  # 5 years of investment
    pmt = 0  # No intermediate payments; hence, zero
    expected_value = 75000  # Expected value at end of investment period

    present_value = np.pv(rate=rate, nper=number_periods, pmt=0, fv=expected_value)

    print('${:,.2f}'.format(-present_value))



def calcula_i():
    number_periods = 5
    pmt = 0
    investment = -100000
    fv = 155000

    rate_of_growth = np.rate(nper=number_periods, pmt=pmt, pv=investment, fv=fv)

    print('{:.2f}%'.format(rate_of_growth * 100))


def calcula_pmt():
    rate = (2.59 / 12) / 100  # Divided by 12 to account for monthly compounding
    nper = 30 * 12  # Monthly payments each year for 30 years

    # Loan amount = Purchase price less down payment; negative sign to indicate cash outflow
    loan_amount = -(600000 - 120000)

    future_value = 0  # Zero because the loan is fully paid off at the end of the 30th year

    monthly_payment = np.pmt(rate=rate, nper=nper, pv=loan_amount, fv=future_value)

    print('${:,.2f}'.format(monthly_payment))

calcula_pmt()