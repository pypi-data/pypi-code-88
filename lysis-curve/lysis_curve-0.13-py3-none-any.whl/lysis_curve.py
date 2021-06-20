def lysis_curve(csv,
                annotate=False,
                title=False,
                group=False,
                subplots=False,
                square=630,
                legend=True,
                colors=False,
                png=False,
                svg=False,
                save=False):
    """
    Return a lysis curve line graph

    *This function always assumes your first column is your time column (x-axis).*
    *Your x-axis data must also be ints not strings for annotations *
    """
    import pandas as pd
    import plotly.graph_objs as go

    # Converts csv to Dataframe object
    global data
    data = pd.read_csv(csv)

    # Gets column names as list
    global columns
    columns = list(data.columns)

    # Removes the background color
    # layout = go.Layout(plot_bgcolor='rgba(0,0,0,0)')

    # Creates the plot
    global fig
    fig = go.Figure()

    global markers
    markers = [
        'square',
        'circle',
        'diamond-tall',
        'star-square',
        'diamond-wide',
        'star',
        'hash',
        'cross',
        'x'
    ]

    global base_colors
    if colors:
        base_colors = colors

    else:
        base_colors = [
            'rgb(0, 0, 0)',  # black
            'rgb(211, 211, 211)',  # grey
            'rgb(19, 197, 89)',  # bright green
            'rgb(0, 0, 255)',  # bright blue
            'rgb(31, 119, 180)',  # blue
            'rgb(255, 127, 14)',  # orange
            'rgb(214, 39, 40)',  # red
            'rgb(227, 119, 194)',  # pink
            'rgb(127, 127, 127)',  # grey
            'rgb(188, 189, 34)',  # mustard
            'rgb(23, 190, 207)',
            'rgb(36, 224, 165)']

    if subplots:
        # make_custom_subplots(data, columns, markers) <-- Cannot get this modularization working for some reason
        from plotly.subplots import make_subplots
        import plotly.graph_objs as go

        fig = make_subplots(rows=3, cols=3,
                            subplot_titles=columns[1:],
                            shared_yaxes=True,
                            )

        # Order for adding the subplot traces to the figure
        positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

        for i, col in enumerate(columns[1:]):
            fig.add_trace(go.Scatter(
                x=data[columns[0]],
                y=data[col],
                name=col,
                connectgaps=True,
                marker_symbol=markers[i],
                marker_size=10,
                marker_opacity=0.9,
                marker_line_width=2,
                marker_line_color='black',
                line={'color': base_colors[i],
                      'width': 5,
                      }
            ),
                row=positions[i][0],
                col=positions[i][1],
            )

        # Smaller text layout settings for subplots
        fig.update_layout(
            font_size=9,
            title_font_size=16.5, )

        # Sets subplot title font size. Plotly subplot titles are coded as annotations!
        fig.update_annotations(font_size=9)
        fig.update_layout(font_size=10.5, )

        # Subplot axes settings
        fig.update_yaxes(
            # title_text='A550',
            type='log',
            ticks='inside',
            showgrid=False,
            linecolor='black',
            zeroline=False,
            tickwidth=2,
            tickcolor='black',
            linewidth=2,
            mirror=True,
            range=[-2, 1]
        )
        fig.update_xaxes(
            title_text='Time (min)',
            showgrid=False,
            linecolor='black',
            zeroline=False,
            ticks='inside',
            tick0=0,  # Starting point for first tick
            dtick=20,  # Interval for each tick
            tickwidth=2,
            tickcolor='black',
            linewidth=2,
            mirror=True,
            # Sets range of the x-axis +0.1 b/c the graph border was cutting off markers
            range=[0, (data[columns[0]].max() + 0.1)],
            constrain="domain",
        )

    elif group:
        global groups
        groups = group
        make_groups(markers=markers, columns=columns)

    else:
        make_base_case_plot(base_colors, columns)

    # Graph layout settings for both standard and subplot graphs
    fig.update_layout(
        yaxis=dict(
            tickmode='array',
            tickvals=[0.01, 0.1, 1.0, 10],
            ticktext=[0.01, 0.1, 1.0, 10]
        ),
        width=square + 75,  # corrects for legend width
        height=square,
        # Font settings for axes and legend
        font_color="navy",
        # Font settings for graph title
        title_font_color="navy",
    )
    if not subplots:
        fig.update_layout(font_size=10.5, )
        fig.update_yaxes(
            title_text='A550',
            type='log',
            ticks='inside',
            showgrid=False,
            linecolor='black',
            zeroline=False,
            tickwidth=5,
            tickcolor='black',
            linewidth=5,
            mirror=True,
            range=[-2, 1]
        )
        fig.update_xaxes(
            title_text='Time (min)',
            showgrid=False,
            linecolor='black',
            zeroline=False,
            ticks='inside',
            tick0=0,  # Starting point for first tick
            dtick=20,  # Interval for each tick
            tickwidth=5,
            tickcolor='black',
            linewidth=5,
            mirror=True,
            # Sets range of the x-axis +0.1 b/c the graph border was cutting off markers
            range=[0, (data[columns[0]].max() + 0.1)],
            constrain="domain",
        )

    if annotate:
        make_annotations()

    if not legend:
        fig.update_layout(showlegend=False)
        fig.update_layout(width=square)

    # Gives user the option to enter a custom graph title. By default, uses the filename
    csv_name: str = csv[:-4]
    if title:
        fig.update_layout(
            title={
                'text': f'{title}',
                'y': 0.91,
                'x': 0.44,
                'xanchor': 'center',
                'yanchor': 'top'})
    else:
        # Default title
        fig.update_layout(
            title={
                'text': f'{csv_name}',
                'y': 0.91,
                'x': 0.44,
                'xanchor': 'center',
                'yanchor': 'top'})

    if save:
        # Saves three versions:
        # (1).png w/ legend (2).svg w/ legend (not square) (3).svg without legend (a square graph)
        fig.write_image(f"{csv_name}.svg")
        fig.write_image(f"{csv_name}.png")
        fig.update_layout(showlegend=False)
        fig.update_layout(width=square)  # b/c by default width is +75 to somewhat correct for legend width
        fig.write_image(f"{csv_name}_no_legend.svg")
        return fig.show()
    if png:
        # Saves the graph as a png in the current directory
        fig.show()
        return fig.write_image(f"{csv_name}.png")
    elif svg:
        fig.show()
        return fig.write_image(f"{csv_name}.svg")
    else:
        # Shows the graph (for jupyter or a web page)
        return fig.show()


def make_custom_subplots(data, columns, markers):
    """
    Split line graph into 3x3 subplots.

    Subplots are not intended to be compatible with grouping.
    """


def make_groups(markers, columns):
    """Match traces such that they have the same color, but different line markers.

    User should pass a list of groups as a str, separating each column by a comma as such:
    ex: [ '1', '2|3', '4|5', '6|7', '8|9' ]
    """
    import plotly.graph_objs as go

    groups_ = [x.split('|') for x in groups]

    for i, grp in enumerate(groups_):
        group_color = base_colors[i]
        group_marker = markers[i]
        for k, col in enumerate(grp):
            linemarkers = ['solid', 'dash', 'dot', 'dashdot']
            marker_variant = ['', '-open', '-open-dot']
            fig.add_trace(go.Scatter(
                x=data[columns[0]],
                y=data[columns[int(col)]],
                name=columns[int(col)],
                connectgaps=True,
                marker_symbol=group_marker + marker_variant[k],
                marker_size=20,
                marker_opacity=0.9,
                marker_line_width=2,
                marker_line_color='black',
                line={'color': group_color,
                      'width': 5,
                      'dash': linemarkers[k]
                      }
            )
            )


def make_annotations():
    """
    Add annotations to the graph.
    """
    num_annotations: int = int(
        input(
            '''Enter the number of annotations to add (Ex: if you added DNP to any samples at 10 min and 20 min, enter 2): '''))
    annotation_timepoints = [
        input('Enter your timepoints (Ex: if you added DNP at 40 min and 50 min, enter 40 then 50): ') for i in
        range(num_annotations)]
    annotation_text: str = input('Enter the annotation text (Ex: if DNP added enter DNP): ')

    # creates list of dictionaries for update_layout() detailing where on the x-axis to place the annotations
    annotations = [dict(x=i, y=0.3, text=annotation_text, showarrow=True, arrowhead=4, ax=0, ay=-40) for i in
                   annotation_timepoints]

    fig.update_layout(annotations=annotations)


def make_base_case_plot(base_colors, columns):
    # Generate base case plot - no grouping, no subplots.
    import plotly.graph_objs as go

    for i, col in enumerate(columns[1:]):
        fig.add_trace(go.Scatter(
            x=data[columns[0]],
            y=data[col],
            name=col,
            connectgaps=True,
            marker_symbol=markers[i],
            marker_size=20,
            marker_opacity=0.9,
            marker_line_width=2,
            marker_line_color='black',
            line={'color': base_colors[i],
                  'width': 5,
                  }
        )
        )
