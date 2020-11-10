from Statistics.Mean import mean
from Calculator.Subtraction import subtraction
import scipy.stats as st


def ConfidenceInterval(Data, ConfidenceLevel):
        # Uses T distribution for under 30
    if len(Data) < 30:
        DegreesOfFreedom = subtraction(len(Data), 1)
        DataMean = mean(Data)
        ans = st.t.interval(alpha=ConfidenceLevel, df=DegreesOfFreedom, loc=DataMean, scale=st.sem(Data))
        return ans

    # Uses Normal distribution for equal to or over 30
    if len(Data) >= 30:
        DataMean = mean(Data)
        ans = st.norm.interval(alpha=ConfidenceLevel, loc=DataMean, scale=st.sem(Data))
        return ans

