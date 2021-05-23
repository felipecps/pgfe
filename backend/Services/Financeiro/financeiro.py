#VER: https://cmdlinetips.com/2020/02/useful-personal-finance-functions-numpy-financial/
# https://numpy.org/numpy-financial/latest/

import numpy_financial as np
interestRate = 0.02  # Annual interest rate
compoundingFrequency = 2  # Twice an year
futureLumpSum = 100
presentValue = np.pv(interestRate / compoundingFrequency, compoundingFrequency, 0,
                     futureLumpSum,
                     when='end');
print("Interest rate:%2.2f" % interestRate);
print("Compounding Frequency:%d" % compoundingFrequency);
print("Future value:%5.2f" % futureLumpSum);
print("Present value:%5.2f" % presentValue);
