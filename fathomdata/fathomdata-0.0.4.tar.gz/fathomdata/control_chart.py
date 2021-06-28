from bokeh.plotting import figure
from bokeh.models import BoxAnnotation, Range1d, HoverTool, Span, Label, Div
from bokeh.layouts import row

from .western_electric_rules import augment_dataframe_with_control_statistics, \
                                    augment_dataframe_with_western_electric_results, \
                                    get_dataframe_level_rule_performance_summary_html

def control_chart(df, calibration_set=None):

    calibration_data_df = __get_calibration_data(df, calibration_set)

    df = augment_dataframe_with_control_statistics(df, calibration_data_df)
    df = augment_dataframe_with_western_electric_results(df)

    the_chart = __construct_chart(df, calibration_data_df)
    rules_summary = Div(text=get_dataframe_level_rule_performance_summary_html(df))

    return row(the_chart, rules_summary)


def __get_calibration_data(df, calibration_set):

    if calibration_set is None:
        return df

    if len(df) != len(calibration_set):
        raise ValueError("If a calibration set is provided, it must have the same length as the dataframe itself.")

    return df[calibration_set]


def __construct_chart(df, calibration_data_df):

    the_parameter_name = df.columns[0]

    the_chart = figure(title=f"{the_parameter_name} control chart",
                       x_axis_label="Batch",
                       y_axis_label=df.iloc[0].units,
                       y_range=__get_pretty_y_range(df),
                       plot_width=900,
                       plot_height=350)

    the_chart.line(x='index',
                   y=the_parameter_name,
                   source=df,
                   legend_label=the_parameter_name,
                   line_color='dodgerblue',
                   line_width=2)

    __plot_passed_points(df, the_parameter_name, the_chart)
    __plot_failed_points(df, the_parameter_name, the_chart)
    __plot_control_annotations(df, the_chart)
    __plot_calibration_demarcation(df, calibration_data_df, the_chart)

    return the_chart


def __get_pretty_y_range(df):

    x_bar = df.iloc[0].x_bar
    sigma = df.iloc[0].sigma
    operating_limits = __get_operating_limits(x_bar, sigma)

    values_series = df[df.columns[0]]

    lowest_relevant_point = min(values_series.min(), operating_limits['lower'])
    highest_relevant_point = max(values_series.max(), operating_limits['upper'])

    return Range1d(lowest_relevant_point - (2 * sigma),
                   highest_relevant_point + (2 * sigma))


def __get_operating_limits(x_bar, sigma):
    return {'lower': x_bar - (3.0 * sigma), 'upper': x_bar + (3.0 * sigma)}


def __plot_passed_points(df, the_parameter_name, the_chart):

    passed_points = df.query("passes_all_rules == True")
    the_chart.circle(x='index', y=the_parameter_name, source=passed_points, fill_color='dodgerblue', size=6)


def __plot_failed_points(df, the_parameter_name, the_chart):

    failed_points = df.query("passes_all_rules == False")
    failed_points_renderer = the_chart.x(x='index',
                                         y=the_parameter_name,
                                         source=failed_points,
                                         color='tomato',
                                         size=20,
                                         line_width=4,
                                         hit_dilation=5)
    failed_points_tooltips = f"""
                <div style='font-size:13px; font-family: Menlo, Consolas, monospace;'>
                    <div>
                        <span>{the_parameter_name}:</span>
                        <span style='color: tomato; font-weight: bold;'>@{the_parameter_name}</span>
                    </div>

                    <div>
                        <span>@batch_date{"{%F}"} (batch @batch_number)</span>
                    </div>

                    <div style='margin-top: 5px'>
                        @rule_failure_explanation_html{"{safe}"}
                    </div>            
                </div>
            """
    failed_points_hover_tool = HoverTool(renderers=[failed_points_renderer],
                                         tooltips=failed_points_tooltips,
                                         formatters={'@batch_date': 'datetime'})
    the_chart.add_tools(failed_points_hover_tool)


def __plot_control_annotations(df, the_chart):

    x_bar = df.iloc[0].x_bar
    sigma = df.iloc[0].sigma
    operating_limits = __get_operating_limits(x_bar, sigma)

    in_control_area = BoxAnnotation(bottom=operating_limits['lower'],
                                    top=operating_limits['upper'],
                                    fill_color='limegreen',
                                    fill_alpha=0.1,
                                    line_color='forestgreen',
                                    line_alpha=0.75,
                                    line_dash='dashed')
    centerline = Span(dimension='width',
                      location=x_bar,
                      line_color='forestgreen',
                      line_alpha=0.75)

    the_chart.add_layout(in_control_area)
    the_chart.add_layout(centerline)


def __plot_calibration_demarcation(df, calibration_data_df, the_chart):

    # If the entire dataset was used to calibrate what is normal, then no demarcation should be shown.
    if len(df) == len(calibration_data_df):
        return

    calibration_right_edge = calibration_data_df.index[-1]
    calibration_demarcation = Span(dimension='height',
                                   location=calibration_right_edge + 0.5,
                                   line_color='black',
                                   line_alpha=0.5,
                                   line_dash='dashed')

    demarcation_label = Label(text='Calibration cutoff',
                              text_font_size='13px',
                              text_alpha=0.75,
                              text_font_style='italic',
                              text_align='right',
                              x=calibration_right_edge + 0.3,
                              x_units='data',
                              y=15,
                              y_units='screen')

    the_chart.add_layout(calibration_demarcation)
    the_chart.add_layout(demarcation_label)
