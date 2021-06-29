# Load libraries ---------------------------------------------

import pandas as pd

from roomsage_simulator.simulator.modules.conversion_rate.conversion_rate_base_module import ConversionRateFlatModule

# ------------------------------------------------------------


def get_single_prior(attribute_prior, prob_df, attributes_set, noise_level, noise_type):
    attribute_prior_df = pd.DataFrame(attribute_prior)
    level_dfs = []
    for level in range(attribute_prior_df.columns.nlevels):
        df = attribute_prior_df.sum(axis=1, level=level).T.reset_index()
        df.columns = ['attribute_value', 'attribute_value_probability']
        df['attribute'] = level
        level_dfs.append(df)
    df = pd.merge(prob_df, pd.concat(level_dfs))
    df = df.set_index(['attribute', 'attribute_value'])
    conversion_probabilities = df.assign(
        conversion_probability_partial=df['conversion_probability_given_attribute_value'] * df[
            'attribute_value_probability']).groupby('attribute')['conversion_probability_partial'].sum()
    conversion_probability = conversion_probabilities[0]
    # assert np.allclose(conversion_probabilities, conversion_probability)

    df['attribute_value_probability_given_conversion'] = df['conversion_probability_given_attribute_value'] * df[
        'attribute_value_probability'] / conversion_probability
    df['attribute_value_probability_given_no_conversion'] = (1.0 - df[
        'conversion_probability_given_attribute_value']) * df['attribute_value_probability'] / (
                                                                    1.0 - conversion_probability)

    conversion_probability_per_attributes_map = {}
    for attributes in attributes_set:
        conversion_probability_per_attributes = conversion_probability
        no_conversion_probability_per_attributes = 1 - conversion_probability
        for attribute, attribute_value in enumerate(attributes):
            conversion_probability_per_attributes *= df.loc[attribute, attribute_value][
                'attribute_value_probability_given_conversion']
            no_conversion_probability_per_attributes *= df.loc[attribute, attribute_value][
                'attribute_value_probability_given_no_conversion']
        conversion_probability_per_attributes_map[attributes] = conversion_probability_per_attributes / (
                conversion_probability_per_attributes + no_conversion_probability_per_attributes)

    Params = ConversionRateFlatModule.Params

    attribute_prior_dict = {}

    for attrs, conversion_probability in conversion_probability_per_attributes_map.items():
        attribute_prior_dict[attrs] = Params(cvr=conversion_probability,
                                             noise_level=noise_level,
                                             noise_type=noise_type)
    return attribute_prior_dict
