# hifis-surveyval
# Framework to help developing analysis scripts for the HIFIS Software survey.
#
# SPDX-FileCopyrightText: 2021 HIFIS Software <support@hifis.net>
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
This module provides functionality to plot survey data.

This module is called by survey analysis scripts and is a helper module
which processes `pandas` data-frames as input and transforms them into
informative plots.
The actual plotting is done by utilizing a separate plotting library called
`matplotlib`.
"""
import logging
import math
from inspect import FrameInfo, getmodulename, stack
from pathlib import Path
from textwrap import wrap
from typing import List, Optional

from matplotlib import colors, pyplot, rcParams
from pandas import DataFrame

from hifis_surveyval.plotting.plotter import Plotter
from hifis_surveyval.plotting.supported_output_format import (
    SupportedOutputFormat,
)


class MatplotlibPlotter(Plotter):
    """Provides standardized plotting functionalities with matplotlib."""

    def _output_pyplot_image(self, output_file_stem: str = "") -> None:
        """
        Render pyplot images depending on output settings.

        Use this after construction a pyplot plot to display the plot or
        render it into an image depending on the application settings.
        (Basically instead of pyplot.show() or pyplot.savefig())

        Args:
            output_file_stem (str):
                The stem of the desired filename (without extension).
                Defaults to an empty string which will prompt the automatic
                generation of a file name from the date of the run and the
                module producing the image.
        """
        if self.OUTPUT_FORMAT == SupportedOutputFormat.SCREEN:
            pyplot.show()
            pyplot.close()
            return

        if not output_file_stem:
            # Auto-generate the file stem

            # Get the calling module's name, assuming this function is called
            # from a survey evaluation script
            # Keep in mind that
            # * FrameInfo is a named tuple in which the second entry is the
            #   fully qualified module name
            # * The first element on the stack is this function, the caller is
            #   the second frame
            calling_module_frame: FrameInfo = stack()[1]
            calling_module_name: str = getmodulename(calling_module_frame[1])

            output_file_stem: str = f"{calling_module_name}"

        file_ending: str = self.OUTPUT_FORMAT.name.lower()
        file_name: str = f"{output_file_stem}.{file_ending}"

        output_path: Path = self.ANALYSIS_OUTPUT_PATH / file_name

        if output_path.exists():
            logging.warning(f"Overriding existing output file {output_path}")

        pyplot.savefig(f"{output_path}")
        pyplot.close()

    @classmethod
    def _set_figure_size(cls, width: float, height: float):
        """
        Set the figure size so the main area fits into the desired space.

        Args:
            width (float):
                Desired plotting space width in inches.
            height (float):
                Desired plotting space height in inches.
        """
        figure = pyplot.gcf()
        left: float = figure.subplotpars.left
        right: float = figure.subplotpars.right
        top: float = figure.subplotpars.top
        bottom: float = figure.subplotpars.bottom
        figure_width: float = float(width) / (right - left)
        figure_height: float = float(height) / (top - bottom)
        figure.set_size_inches(figure_width, figure_height)

    def plot_bar_chart(
        self,
        data_frame: DataFrame,
        plot_file_name: str = "",
        show_legend: bool = True,
        show_value_labels: bool = True,
        round_value_labels_to_decimals: int = 0,
        **kwargs,
    ) -> None:
        r"""
        Plot given data-frame as a (stacked) bar chart.

        A pandas DataFrame is used as input data from which a (stacked) bar
        chart is generated. This DataFrame need be structured in a particular
        way. The actual data values are taken column by column and plotted as
        bars for each index entry.
        In case of a normal bar chart this means each sequence of bars /
        column is put next to each other while each sequence is grouped by the
        series / rows and labeled accordingly in the legend.
        By contrast in case of a stacked bar chart each sequence of bars /
        column is stacked on top of the previous instead of put next to each
        other and labeled accordingly in the legend.
        The index names are used to label the ticks along the x-axis, while the
        column names are used as labels in the legend.

        Args:
            data_frame (DataFrame):
                All data needed for this function to plot a stacked bar
                chart is encapsulated in this DataFrame.
            plot_file_name (str):
                Optional file name which is used to store the plot to a
                file. If this argument is an empty string (Default) for this
                argument, a suitable file name is auto-generated.
            show_legend (bool):
                Used to control whether a legend is included in the plot or
                not. (Default: True)
            show_value_labels (bool):
                Enable or disable labels to show the values of each bar. (
                Default: True)
            round_value_labels_to_decimals (int):
                Round label values to the number of decimals. (Default: 0)
            \*\*kwargs:
                stacked (bool):
                    Prompts the generation of a stacked bar chart instead on
                    bars being grouped side-by-side.
                plot_title (str):
                    The title text for the plot. (Default: "")
                x_axis_label (str):
                    The label for the x-axis. Default: "")
                x_label_rotation (int):
                    Allows to rotate the x-axis labels for better
                    readability. Value is given in degrees. (Default: 0)
                y_axis_label (str):
                    The label for the y-axis. Default: "")
                legend_location (str):
                    Specifies positioning of the plot's legend. (Default:
                    "best") See Also: pandas.Axis.legend(loc)
                legend_anchor (BboxBase):
                    Allows to specify an anchor point for the plot's legend (
                    Default: None) See Also: pandas.Axis.legend(bbox_to_anchor)
                ylim (Set[float]):
                    Allows to specify the maximum and minimum values of the
                    y axis (Default: None) See Also:
                    matplotlib.axes.Axes.set_ylim
        """
        rcParams.update({"figure.autolayout": True})

        # Color map Generation:
        # 1. Pick a suitable predefined colormap. Chose one with light colors
        # so the value labels can stand out by darkening them.
        base_color_map = pyplot.get_cmap("Pastel1")
        color_count = len(base_color_map.colors)
        if len(data_frame.columns) > color_count:
            raise NotImplementedError(
                f"Attempt to plot a bar chart "
                f"with more then {color_count} columns per row."
                f"Color palette has not enough colors for all of them."
                f"(is bar chart a fitting diagram type here?)"
                f"(Would transposing the data frame help?)"
            )
        # 2. Reduce the colormap to have only as much colors as there are
        # columns so each columns color index matches the column index
        # (If the colormap were larger one would have to do linear
        # interpolation to obtain the proper color.)
        color_map = colors.ListedColormap(
            [
                base_color_map.colors[index]
                for index in range(len(data_frame.columns))
            ]
        )
        # This new colormap is handed to the graph and used in the value labels

        plot_stacked: bool = kwargs.get("stacked", False)
        x_rotation: int = kwargs.get("x_label_rotation", 0)

        data_frame.plot(kind="bar", stacked=plot_stacked, cmap=color_map)

        axes = pyplot.gca()

        axes.set_title(kwargs.get("plot_title", ""))
        axes.set_xlabel(kwargs.get("x_axis_label", ""))
        axes.set_ylabel(kwargs.get("y_axis_label", ""))
        axes.set_xticklabels(
            data_frame.index.values,
            rotation=x_rotation,
            ha="right" if x_rotation else "center",
            rotation_mode="anchor",
        )
        if "ylim" in kwargs:
            axes.set_ylim(kwargs.get("ylim"))

        if show_legend:
            axes.legend(
                data_frame.columns.values,
                loc=kwargs.get("legend_location", "best"),
                bbox_to_anchor=kwargs.get("legend_anchor", None),
            )
        else:
            axes.get_legend().remove()

        if show_value_labels:
            self._add_bar_chart_value_labels(
                data_frame,
                color_map,
                plot_stacked,
                round_value_labels_to_decimals,
            )

        self._set_figure_size(len(data_frame.index) * 0.25, 5)
        self._output_pyplot_image(plot_file_name)

    @classmethod
    def _add_bar_chart_value_labels(
        cls,
        data_frame: DataFrame,
        color_map: colors.Colormap,
        plot_stacked: bool,
        round_value_labels_to_decimals: int = 0,
    ) -> None:
        """
        Add value labels to a bar chart.

        This is a helper method and not supposed to be called on its own.

        Args:
            data_frame (DataFrame):
                The data frame providing the data for the chart.
            color_map (Colormap):
                The color map used by the bar chart.
            plot_stacked (bool):
                Whether the chart is a stacked bar chart or not.
            round_value_labels_to_decimals (int):
                Round label values to the number of decimals. (Default: 0)
        """
        default_font_size = rcParams["font.size"]
        axes = pyplot.gca()

        # Loop over the data and annotate the actual values
        column_count: int = len(data_frame.columns)
        row_count: int = len(data_frame.index)

        if plot_stacked:
            sums = data_frame.sum(axis=1)
            minimum_value = sums.min()
            maximum_value = sums.max()

            if minimum_value > 0:
                minimum_value = 0

            # The lower boundary of the plotting area
            y_range = maximum_value - minimum_value

            # The minimum height until which a label can be included
            # directly in the bar as fraction of the plot height
            min_include_height = y_range / 15

            for row in range(row_count):
                row_sum = 0

                for column in range(column_count):
                    value = data_frame.iloc[row, column]

                    # Skip values that can not be plotted in a stacked bar
                    # chart
                    if (value in [0, None]) or math.isnan(value):
                        continue

                    color = color_map.colors[column]
                    # Darken the color by setting each component to 50%
                    color_dark = [0.5 * component for component in color]

                    bar_center_y = row_sum + value / 2

                    # If the value fits inside the bar plot it directly in the
                    # center, otherwise move it to the outside and add a line
                    # as indicator.
                    if value > min_include_height:
                        text_x = row
                        text_y = bar_center_y
                    else:
                        # The label has to go outside the bar
                        # The following numbers come from eyeballing and
                        # implicit knowledge how the x-axis is organized.
                        # See also below in the non-stacked section.

                        # The text goes to the left of the bar if the column
                        # index is an odd number, otherwise the text is offset
                        # to the right.
                        # 0.375 is the middle of the white space between the
                        # section borders (relative coordinates -0.5 … +0.5 )
                        # and bar borders (relative coordinates -0.25 … + 0.25)
                        text_left: bool = bool(column % 2)
                        text_x_offset: float = -0.375 if text_left else 0.375
                        line_x_overhang: float = -0.1 if text_left else 0.1

                        # Move the text_y up a bit so it does not overlap the
                        # indicator line
                        text_y = bar_center_y + min_include_height / 4
                        text_x = row + text_x_offset

                        # Plot the indicator line
                        pyplot.plot(
                            [text_x + line_x_overhang, row],
                            [bar_center_y, bar_center_y],
                            color=color,
                        )

                    # Round values to the number of decimals given in parameter
                    # round_value_labels_decimals.
                    value_rounded = (
                        int(value.round(round_value_labels_to_decimals))
                        if round_value_labels_to_decimals == 0
                        else value.round(round_value_labels_to_decimals)
                    )

                    # Values with more than 2 digits get displayed with smaller
                    # font size to fit them better
                    axes.text(
                        text_x,
                        text_y,
                        value_rounded,
                        ha="center",
                        va="center",
                        color=color_dark,
                        size=default_font_size if value < 100 else "smaller",
                    )
                    # for next row iteration:
                    row_sum += value
        else:

            maximum_value = data_frame.max().max()
            minimum_value = data_frame.min().min()
            # If not stacked, all bar texts share the same y-component
            # This has to account for the possible range of values
            # and negative values.
            # An offset from the x-axis of 1/10th of the most extreme value was
            # chosen for the text labels by iterative eyeballing.
            if abs(maximum_value) >= abs(minimum_value):
                text_y = maximum_value / 10
            else:
                text_y = minimum_value / 10

            # For the x-offset calculation, negative values mean left,
            # positive values mean right.
            # The x-axis is subdivided into <row_count> equal sections
            # Each section has by definition a width of 1 unit
            # The bar area starts at 0.25 units to the left
            # and ends at 0.25 units to the right
            bar_area_offset = 0.25
            bar_area_width = 0.5

            # In case of non-stacked plots, the bar area is equally distributed
            # across <column_count> bars and each label is offset by a half bar
            # width within the bar to center it
            bar_width = bar_area_width / column_count
            bar_offset = bar_width / 2
            for row in range(row_count):
                for column in range(column_count):
                    color = color_map.colors[column]

                    # Darken the color by setting each component to 50%
                    color = [0.5 * component for component in color]

                    # Within each bar area the bar for each column starts at:
                    column_offset = bar_width * column
                    # And thus, the final x-component is distributed around
                    # <row>, which indicates the center of the section.
                    # The bar_area_offset gives the leftmost point of the bar
                    # area, the column_offset yields the leftmost point of the
                    # current column within the bar area and from there out,
                    # the bar_offset gives the center of the bar. So:
                    text_x = row - bar_area_offset + column_offset + bar_offset

                    value = data_frame.iloc[row, column]

                    # Round values to the number of digits given in parameter
                    # round_value_labels_decimals.
                    value_rounded = (
                        int(value.round(round_value_labels_to_decimals))
                        if round_value_labels_to_decimals == 0
                        else value.round(round_value_labels_to_decimals)
                    )

                    # Values with more than 2 digits get displayed with smaller
                    # font size to fit them better
                    axes.text(
                        text_x,
                        text_y,
                        value_rounded,
                        ha="center",
                        va="center",
                        color=color,
                        size=default_font_size if value < 100 else "smaller",
                    )

    def plot_box_chart(
        self,
        data_frame: Optional[DataFrame] = None,
        data_frames: List[DataFrame] = None,
        plot_file_name: str = "",
        **kwargs,
    ) -> None:
        r"""
        Generate a box chart from the provided data.

        Each column in the frame corresponds to one box with whiskers.

        Args:
            data_frame (Optional[DataFrame]):
                A singular data frame. Syntactic sugar for using
                `data_frame=x` instead of `data_frames=[x]`.
            data_frames (List[DataFrame]):
                A list of data frames. The columns with the same column
                index across all the frames are grouped together.
            plot_file_name (str):
                Optional file name which is used to store the plot to a file.
                If this argument is an empty string (Default) for this
                argument, a suitable file name is auto-generated.
            \*\*kwargs:
                plot_title (str):
                    The title text for the plot. (Default: "")
                x_axis_label (str):
                    The label for the x-axis. Default: "")
                x_label_rotation (int):
                    Allows to rotate the x-axis labels for better
                    readability. Value is given in degrees. (Default: 0)
                y_axis_label (str):
                    The label for the y-axis. Default: "")
        """
        rcParams.update({"figure.autolayout": True})
        x_rotation: int = kwargs.get("x_label_rotation", 0)

        # Create a new holder for the data frames to not manipulate the default
        # parameter
        _data_frames: List[DataFrame] = (
            data_frames.copy() if data_frames else []
        )

        if (data_frame is not None) and (not data_frame.empty):
            _data_frames.append(data_frame.copy())

        if not _data_frames:
            logging.warning(
                f"Attempt to create box plot {plot_file_name} without "
                f"data. Skipping this plot."
            )
            return

        column_count: int = max(len(frame.columns) for frame in _data_frames)
        frame_count: int = len(_data_frames)

        figure, axes = pyplot.subplots()
        axes.set_title(kwargs.get("plot_title", ""))
        axes.set_xlabel(kwargs.get("x_axis_label", ""))
        axes.set_ylabel(kwargs.get("y_axis_label", ""))
        axes.grid("on", axis="y", which="major", color="lightgray")

        x_tick_labels: List[str] = []
        for column_index in range(column_count):
            group_position = column_index * frame_count
            data_frame_counter: int = 0
            for frame in _data_frames:

                # Handle frames with fewer columns
                if len(frame.columns) <= column_index:
                    continue

                # Using the factor 0.75 to keep plots of one group closer
                # together
                position = group_position + data_frame_counter * 0.75
                x_tick_labels.append(frame.columns[column_index])
                column_frame = frame.iloc[:, column_index].dropna()
                plot = axes.boxplot(
                    column_frame,
                    positions=[position],
                    widths=0.5,
                    patch_artist=True,
                )

                # Fill the box background so the boxes overlay the grid lines
                for patch in plot["boxes"]:
                    patch.set_facecolor("wheat")
                data_frame_counter += 1

        axes.set_xticklabels(
            x_tick_labels,
            rotation=x_rotation,
            ha="right" if x_rotation else "center",
            rotation_mode="anchor",
        )

        # Adapt the figure to its content
        self._set_figure_size(column_count * frame_count * 0.25, 5)
        self._output_pyplot_image(plot_file_name)

    def plot_matrix_chart(
        self,
        data_frame: DataFrame,
        plot_file_name: str = "",
        invert_colors: bool = False,
        value_label_decimals: int = 2,
        **kwargs,
    ) -> None:
        r"""
        Plot given data frame as matrix chart.

        Args:
            data_frame (DataFrame):
                The data frame to plot.
            plot_file_name (str):
                (Optional) The file name stem for the output file.
            invert_colors (bool):
                (Optional) Use an inverted color scheme for plotting. This
                is recommended for plotting data that represents the absence of
                something. Defaults to False.
            value_label_decimals (int):
                Round label values to the number of decimals. (Default: 2)
            \*\*kwargs:
                plot_title (str):
                    The title text for the plot. (Dafault: "")
                x_axis_label (str):
                    The label for the x-axis. Default: "")
                x_label_rotation (int):
                    Allows to rotate the x-axis labels for better
                    readability. Value is given in degrees. (Default: 0)
                y_axis_label (str):
                    The label for the y-axis. Default: "")
        """
        rcParams.update({"figure.autolayout": True})
        color_map_name = "Blues_r" if invert_colors else "Blues"
        color_map = pyplot.get_cmap(color_map_name)

        column_count: int = len(data_frame.columns)
        row_count: int = len(data_frame.index)

        x_tick_labels = [
            "\n".join(wrap(label, 20)) for label in data_frame.columns.values
        ]

        x_rotation: int = kwargs.get("x_label_rotation", 0)

        figure, axes = pyplot.subplots()
        axes.imshow(data_frame, aspect="auto", cmap=color_map)
        axes.set_title(kwargs.get("plot_title", ""))
        axes.set_xlabel(kwargs.get("x_axis_label", ""))
        axes.set_ylabel(kwargs.get("y_axis_label", ""))
        axes.set_xticks(range(column_count))
        axes.set_yticks(range(row_count))
        axes.set_xticklabels(
            x_tick_labels,
            rotation=x_rotation,
            ha="right" if x_rotation else "center",
            rotation_mode="anchor",
        )
        axes.set_yticklabels(data_frame.index.values)

        # Loop over the data and annotate the actual values
        upper_limit = data_frame.max().max()
        threshold = 0.25 * upper_limit if invert_colors else 0.75 * upper_limit

        for i in range(row_count):
            for j in range(column_count):
                value = round(data_frame.iloc[i, j], value_label_decimals)
                switch_color = bool(
                    (value < threshold)
                    if invert_colors
                    else (value > threshold)
                )
                axes.text(
                    j,
                    i,
                    value,
                    ha="center",
                    va="center",
                    color="white" if switch_color else "black",
                )

        self._output_pyplot_image(plot_file_name)
