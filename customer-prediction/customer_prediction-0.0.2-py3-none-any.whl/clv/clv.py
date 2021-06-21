from lifetimes import BetaGeoFitter, GammaGammaFitter
import seaborn as sns


class CustomerLifeTimeValue:
    def __init__(self, lifetimes_dataframe, penalizer_coef=0.0):
        """Constructor"""
        self.lifetimes_dataframe = lifetimes_dataframe

        self.bgf = BetaGeoFitter(penalizer_coef=penalizer_coef)
        self.bgf.fit(lifetimes_dataframe['frequency'], lifetimes_dataframe['recency'], lifetimes_dataframe['T'])

        self.ggf = GammaGammaFitter(penalizer_coef=penalizer_coef)
        self.ggf.fit(lifetimes_dataframe['frequency'],
                     lifetimes_dataframe['monetary_value'])
        self.lifetimes_values = []

    def customer_lifetime_value(self, time=1, discount_rate=0.1):
        self.lifetimes_values = self.ggf.customer_lifetime_value(
            self.bgf,
            self.lifetimes_dataframe['frequency'],
            self.lifetimes_dataframe['recency'],
            self.lifetimes_dataframe['T'],
            self.lifetimes_dataframe['monetary_value'],
            time=time,
            discount_rate=discount_rate
        )
        return self.lifetimes_values

    def customer_lifetime_value_countplot(self, round_value):
        sorted_values = self.lifetimes_values.round(int('-' + str(round_value))).sort_values()

        step = 1
        for _ in range(round_value):
            step *= 10

        sns.countplot(x="value",
                      data=sorted_values.apply(lambda x: str(int(x)) + "-" + str(int(x) + step)).to_frame(name='value'))
