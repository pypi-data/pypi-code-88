def augment_dataframe_with_control_statistics(df, calibration_data_df):

    calibration_values_series = calibration_data_df[calibration_data_df.columns[0]]
    df['x_bar'] = __compute_x_bar(calibration_values_series)
    df['sigma'] = __compute_sigma(calibration_values_series)

    return df

def __compute_x_bar(calibration_data_series):
    return calibration_data_series.mean()


def __compute_sigma(calibration_data_series):

    moving_ranges = calibration_data_series.rolling(window=2) \
                                           .apply(lambda x: abs(x.iloc[1] - x.iloc[0]))
    moving_range_bar = moving_ranges.mean()
    return 2.66 * moving_range_bar / 3.0


def augment_dataframe_with_western_electric_results(df):

    values_series = df[df.columns[0]]

    # x_bar and sigma have already been computed for the dataframe and are the same for every point -- so just take the
    # values in the first row.
    x_bar = df.iloc[0].x_bar
    sigma = df.iloc[0].sigma

    # For each rule to check, create a rolling window of the datapoints and process the rule's evaluation func for each window.
    # Each evaulation func accepts the window as the first argument and x_bar and sigma as additional arguments.
    for rule_id, rule in __the_rules.items():
        df[rule_id] = values_series.rolling(rule['rolling_window_size']) \
                                               .apply(rule['rule_evaluation_func'],
                                                      kwargs={'x_bar': x_bar, 'sigma': sigma}) \
                                               .map(__parse_boolean)

    # For each datapoint, compute whether or not it passes every rule.
    df['passes_all_rules'] = True
    for rule_id, rule in __the_rules.items():
        df['passes_all_rules'] = df['passes_all_rules'] & df[rule_id]

    df['rule_failure_explanation_html'] = df.apply(__get_datapoint_level_rule_failure_explanation_html, axis='columns')

    return df


# Western Electric rules #1, #2 and #3: Fail if a single point is unnaturally far from the centerline, or if n out of n+1
# consecutive points are unnaturally far from the centerline and on the same side of the centerline.
def __does_window_pass_standard_western_electric_rule(values, x_bar, sigma):

    if not (len(values) == 1 or len(values) == 3 or len(values) == 5):
        raise ValueError("Western Electric rules #1-3 should only be run against windows of 1, 3 or 5 datapoints.")

    # By convention, consider "this particular point" to be the furthest to right in this window. That is,
    # we are computing whether this particular point and its immediate predecessors pass the rule together.
    this_point_value = values.iloc[-1]

    acceptable_difference_from_x_bar = __get_western_electric_acceptable_distance_from_x_bar(len(values), sigma)

    # Set the thresholds of the acceptable range depending on whether this particular point is above or below the x_bar centerline.
    min_threshold = float('-inf')
    max_threshold = float('inf')
    if this_point_value >= x_bar:
        max_threshold = x_bar + acceptable_difference_from_x_bar
    else:
        min_threshold = x_bar - acceptable_difference_from_x_bar

    # If this particular point is within the acceptable range, the window passes the rule.
    if min_threshold <= this_point_value <= max_threshold:
        return True

    # If this window is of size 1 and execution has reached this point, then the point is outside of the acceptable range.
    if len(values) == 1:
        return False

    # If at least two points are within the acceptable range, the window passes the rule.
    passed_points = [v for v in values if min_threshold <= v <= max_threshold]
    return len(passed_points) >= 2


def __get_western_electric_acceptable_distance_from_x_bar(num_values_in_rolling_window, sigma):
    if num_values_in_rolling_window == 1:
        return 3.0 * sigma
    elif num_values_in_rolling_window == 3:
        return 2.0 * sigma
    elif num_values_in_rolling_window == 5:
        return sigma


# Western Electric rule #4: Fail if eight consecutive points are on one side of the centerline.
def __does_window_pass_western_electric_rule_4(values, x_bar, sigma):

    return not all(value > x_bar for value in values) and \
           not all(value < x_bar for value in values)


# Nelson Rule #5: Fail if seven consecutive points are either monotonically increasing or decreasing.
def __does_window_pass_nelson_rule_5(values, x_bar, sigma):

    return not values.is_monotonic_increasing and \
           not values.is_monotonic_decreasing


# Westgard Rule #9: Fail if for two consecutive points, one is more than 2 * sigma above x_bar and the other
# is 2 * sigma below x_bar.
def __does_window_pass_westgard_rule_9(values, x_bar, sigma):

    min_threshold = x_bar - (2 * sigma)
    max_threshold = x_bar + (2 * sigma)

    value_0 = values.iloc[0]
    value_1 = values.iloc[1]

    # If either value lies within 2 * sigma of x_bar, the window passes the rule.
    if (min_threshold <= value_0 <= max_threshold) or (min_threshold <= value_1 <= max_threshold):
        return True

    # If the two values are on the same side of x_bar, the window passes the rule.
    return (value_0 < x_bar and value_1 < x_bar) or (value_0 > x_bar and value_1 > x_bar)


__the_rules = {
    'passes_western_electric_rule_1': {
        'pretty_name': "Western Electric rule #1",
        'failure_message': "Datapoint is outside of 3σ.",
        'rolling_window_size': 1,
        'rule_evaluation_func': __does_window_pass_standard_western_electric_rule
    },
    'passes_western_electric_rule_2': {
        'pretty_name': "Western Electric rule #2",
        'failure_message': "Two of three consecutive datapoints are outside of 2σ on the same side of the centerline.",
        'rolling_window_size': 3,
        'rule_evaluation_func': __does_window_pass_standard_western_electric_rule
    },
    'passes_western_electric_rule_3': {
        'pretty_name': "Western Electric rule #3",
        'failure_message': "Four of five consecutive datapoints are outside of 1σ on the same side of the centerline.",
        'rolling_window_size': 5,
        'rule_evaluation_func': __does_window_pass_standard_western_electric_rule
    },
    'passes_western_electric_rule_4': {
        'pretty_name': "Western Electric rule #4",
        'failure_message': "Eight consecutive datapoints are on the same side of the centerline.",
        'rolling_window_size': 8,
        'rule_evaluation_func': __does_window_pass_western_electric_rule_4
    },
    'passes_nelson_rule_5': {
        'pretty_name': "Nelson rule #5",
        'failure_message': "Seven consecutive datapoints are trending in the same direction.",
        'rolling_window_size': 7,
        'rule_evaluation_func': __does_window_pass_nelson_rule_5
    },
    'passes_westgard_rule_9': {
        'pretty_name': "Westgard rule #9",
        'failure_message': "Two consecutive datapoints are outside of 2σ on opposite sides of the centerline.",
        'rolling_window_size': 2,
        'rule_evaluation_func': __does_window_pass_westgard_rule_9
    },
}


def __parse_boolean(passed_rule_float):

    if passed_rule_float == 0.0:
        return False

    return True


def __get_datapoint_level_rule_failure_explanation_html(datapoint):

    if datapoint.passes_all_rules:
        return ""

    rule_failures = []

    for rule_id, rule in __the_rules.items():
        if not datapoint[rule_id]:
            rule_failures.append(rule['failure_message'])

    return __get_datapoint_level_html_for_rule_failures(rule_failures)


def __get_datapoint_level_html_for_rule_failures(failures):

    if len(failures) == 1:
        return failures[0]

    html_failures = "".join([f"<li>{failure}</li>" for failure in failures])
    return f"<div>Rule failures:</div><ul>{html_failures}</ul>"


def get_dataframe_level_rule_performance_summary_html(df):

    ret_val = "<div style='padding-left: 25px'>" + \
              "<div style='font-size: 13px; font-weight: bold; font-color: gray; margin-bottom: 10px;'>Control chart stability test summary</div>"

    for rule_id, rule in __the_rules.items():
        ret_val += __get_dataframe_level_rule_performance_html_for_rule(df, rule_id, rule)

    ret_val += "</div>"

    return ret_val


def __get_dataframe_level_rule_performance_html_for_rule(df, rule_id, rule):

    rule_series = df[rule_id]
    num_failed_points = rule_series[rule_series == False].count()
    did_rule_pass = num_failed_points == 0

    html_template = """
    <div>
        <span style='color: |symbol_color|; font-size: 13px; font-weight: bold;'>|symbol_text|</span>
        <span style='font-size: 13px;'>|rule_pretty_name| |failed_rule_reason|</span>
    </div>
    """

    html_template = html_template.replace('|symbol_color|', 'forestgreen' if did_rule_pass else  'tomato')
    html_template = html_template.replace('|symbol_text|', '&#10003;' if did_rule_pass else  '&cross;')
    html_template = html_template.replace('|rule_pretty_name|', rule['pretty_name'])
    html_template = html_template.replace('|failed_rule_reason|', "" if did_rule_pass else f"({num_failed_points} point{'' if num_failed_points == 1 else 's'} failed)")

    return html_template
