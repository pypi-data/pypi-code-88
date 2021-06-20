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
    '''
    **Given:** CSV, passed as the name of the file in the present directory
    **Returns:** Lysis curve line graph
    *This function always assumes your first column is your time column (x-axis).*
    *Your x-axis data must also be ints not strings if you want the annotations to work properly*
    '''
    import pandas as pd
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots

    # Converts csv to Dataframe object
    data = pd.read_csv(csv)

    # Gets column names as list
    columns = list(data.columns)

    # Removes the background color
    # layout = go.Layout(plot_bgcolor='rgba(0,0,0,0)')

    # Creates the plot
    fig = go.Figure()

    if colors:
        colors = colors
    else:
        colors = [
            'rgb(31, 119, 180)',  # blue
            'rgb(255, 127, 14)',  # orange
            'rgb(44, 160, 44)',  # green
            'rgb(214, 39, 40)',  # red
            'rgb(227, 119, 194)',  # pink
            'rgb(127, 127, 127)',  # grey
            'rgb(188, 189, 34)',  # mustard
            'rgb(23, 190, 207)',
            'rgb(36, 224, 165)']

    if subplots:
        fig = make_subplots(rows=3, cols=3,
                            subplot_titles=columns[1:],
                            # shared_xaxes=True,
                            shared_yaxes=True,
                            )

        # positions order for adding the subplot traces to the figure

        positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

        for i, col in enumerate(columns[1:]):
            fig.add_trace(go.Scatter(
                x=data[columns[0]],
                y=data[col],
                name=col,
                connectgaps=True,
                marker_size=6,
                line={'color': colors[i],
                      'width': 2.5,
                      },
            ),
                row=positions[i][0],
                col=positions[i][1],
            )
        # Smaller text layout settings for subplots

        fig.update_layout(font_size=10,
                          title_font_size=16.5, )

        # Sets subplot title font size. Plotly subplot titles are coded as annotations!
        fig.update_annotations(font_size=10.5)


    elif group:
        # This allows the user to color certain (related) line data the same color, but with different line markers
        # User should pass a list of groups as a str, separating each column by a comma as such:
        # ex: [ '1', '2|3', '4|5', '6|7', '8|9' ]

        groups = [x.split('|') for x in group]

        for i, grp in enumerate(groups):
            group_color = colors[i]
            for k, col in enumerate(grp):
                linemarkers = ['solid', 'dash', 'dot', 'dashdot']
                fig.add_trace(go.Scatter(
                    x=data[columns[0]],
                    y=data[columns[int(col)]],
                    name=columns[int(col)],
                    connectgaps=True,
                    marker_size=7,
                    line={'color': group_color,
                          'width': 3,
                          'dash': linemarkers[k]
                          }
                )
                )
    else:
        # Adds each column to the plot without grouping

        for i, col in enumerate(columns[1:]):
            fig.add_trace(go.Scatter(
                x=data[columns[0]],
                y=data[col],
                name=col,
                connectgaps=True,
                marker_size=7,
                line={'color': colors[i],
                      'width': 3,
                      }
            )
            )

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

    fig.update_yaxes(type='log',
                     ticks='inside',
                     showgrid=False,
                     linecolor='black',
                     zeroline=False,
                     mirror=True,
                     range=[-2, 1]
                     )
    fig.update_xaxes(title_text='Time (min)',
                     # showgrid=False,
                     linecolor='black',
                     zeroline=False,
                     ticks='inside',
                     tick0=0,  # Starting point for first tick
                     dtick=20,  # Interval for each tick
                     mirror=True,
                     # Sets range of the x-axis +0.1 b/c the graph border was cutting off markers
                     range=[0, (data[columns[0]].max() + 0.1)],
                     constrain="domain",
                     )
    if not subplots:
        fig.update_layout(font_size=13.5, )
        fig.update_yaxes(title_text='A550 (log)')

    # Adds annotations to the graph based on the user's input data

    if annotate:
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

    if not legend:
        fig.update_layout(showlegend=False)
        fig.update_layout(width=square)

    # Gives user the option to enter a custom graph title. By default, uses the filename
    if title:
        fig.update_layout(
            title={
                'text': f'{title}',
                'y': 0.91,
                'x': 0.44,
                'xanchor': 'center',
                'yanchor': 'top'})
    else:
        # Gets csv filename by indexing all but the last 4 characters, the ".csv" part
        csv_name: str = csv[:-4]
        fig.update_layout(
            title={
                'text': f'{csv_name}',
                'y': 0.91,
                'x': 0.44,
                'xanchor': 'center',
                'yanchor': 'top'})

    csv_name: str = csv[:-4]

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