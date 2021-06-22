import hashlib
from typing import Union
import datetime
from difflib import SequenceMatcher
from functools import partial
import pandas as pd


class ModelComparer:
    """The class contains several methods of comparing data frames which are the result of extracting data
    from the "Hypatos Document Extractor".

    Args:
        left_dataframe: self explanatory
        right_dataframe: self explanatory
        left_matching_index: name of index which should be used for match in left dataset
        right_matching_index: name of index which should be used for match in left dataset

    """

    def __init__(self,
                 left_dataframe: pd.DataFrame,
                 right_dataframe: pd.DataFrame,
                 left_matching_index: str = "file_name",
                 right_matching_index: str = "file_name"
                 ):

        self.left_dataframe = left_dataframe
        self.right_dataframe = right_dataframe
        self.left_matching_index = left_matching_index
        self.right_matching_index = right_matching_index

    def _levenshtein_join(
            self,
            left_dataframe: pd.DataFrame,
            right_dataframe: pd.DataFrame,
            left_matching_index="file_name",
            right_matching_index="file_name",
    ) -> pd.DataFrame:
        """Performs a left-join on two dataframes using approximate matches of the columns that are used for the join.
        Levenshtein distance is used to determine the best match for the join.
        """

        def match_and_eliminate(df: pd.DataFrame, per_index: str) -> pd.DataFrame:

            # introduce empty DataFrame at the beginning
            best_results = pd.DataFrame()

            # copy a dataset that we will working with
            dataset = df

            # execute in loop until dataset would have no possible matches
            while not dataset.empty:
                # collect the best match
                best_match = dataset.loc[dataset["distance"].idxmin()]
                best_results = best_results.append(best_match)

                index_to_be_removed = best_match.index_x
                corresponding_field = best_match.index_y

                # perform elimination within dataset
                dataset = dataset.drop(
                    dataset[dataset["index_x"] == index_to_be_removed].index
                )
                dataset = dataset.drop(
                    dataset[dataset["index_y"] == corresponding_field].index
                )

            # if there are more items on a left dataset than in the right dataset
            # collect not matched records from left dataset (x) and place them in a results as non matched
            if per_index == "index_x":
                not_matched_results = df[~df.index_x.isin(best_results.index_x)]
                if not not_matched_results.empty:
                    dummy_indexes = not_matched_results["index_x"].unique()
                    dummy_records = filtered_file_name[
                        filtered_file_name.index_x.isin(dummy_indexes)
                    ]
                    old_columns = dummy_records.columns
                    new_columns = [
                        column + "_x"
                        if (column != "file_name" and column != "index_x")
                        else column
                        for column in old_columns
                    ]
                    dummy_records.columns = new_columns
                    best_results = best_results.append(dummy_records)

            return best_results

        # Prepare data
        left_dataframe[left_matching_index] = left_dataframe[
            left_matching_index
        ].astype(str)
        left_dataframe["artificial_key"] = left_dataframe.astype(str).values.sum(axis=1)
        right_dataframe["artificial_key"] = right_dataframe.astype(str).values.sum(
            axis=1
        )

        file_names = left_dataframe.groupby(left_matching_index)[
            left_matching_index
        ].count()
        results = pd.DataFrame()

        for file_name, v in file_names.to_dict().items():

            filtered_file_name = left_dataframe[left_dataframe.file_name == file_name].copy()

            # prepare indexes for artificial_keys
            filtered_file_name["index_x"] = [
                # this lib is not used for any encrypting data but only for making short unique key based on records
                hashlib.md5(val.encode("utf-8")).hexdigest()
                for val in filtered_file_name["artificial_key"]
            ]
            right_dataframe["index_y"] = [
                # this lib is not used for any encrypting data but only for making short unique key based on records
                hashlib.md5(val.encode("utf-8")).hexdigest()
                for val in right_dataframe["artificial_key"]
            ]

            # create cartesian product for file
            cartesian = pd.merge(
                filtered_file_name,
                right_dataframe,
                left_on=left_matching_index,
                right_on=right_matching_index,
            )

            if not cartesian.empty:
                # how many records we have on _x
                records_on_x = filtered_file_name["file_name"].count()
                # how many records we have on _y
                records_on_y = right_dataframe[right_dataframe.file_name == file_name][
                    "file_name"
                ].count()

                cartesian["distance"] = cartesian.apply(
                    partial(
                        self.calculate_distance,
                        a="artificial_key_x",
                        b="artificial_key_y",
                    ),
                    axis=1,
                )

                matches = (
                    match_and_eliminate(cartesian, "index_x")
                    if records_on_x >= records_on_y
                    else match_and_eliminate(cartesian, "index_y")
                )

            else:
                matches = pd.merge(
                    filtered_file_name, right_dataframe, on="file_name", how="left"
                )

            matches.drop(["artificial_key_x"], axis=1, inplace=True)
            matches.drop(["artificial_key_y"], axis=1, inplace=True)
            matches.drop(["index_x"], axis=1, inplace=True)
            matches.drop(["index_y"], axis=1, inplace=True)

            results = results.append(matches)

        return results

    def compare(self, comparison_type: str) -> Union[pd.DataFrame, None]:

        """Compare dataframes
        Returns: Comparisons represented as a pandas dataframe or None
        """

        if comparison_type == "single":
            comparison = pd.merge(
                self.left_dataframe, self.right_dataframe, left_on=self.left_matching_index,
                right_on=self.right_matching_index, how="outer"
            )

        elif comparison_type == "multi":
            comparison = self._levenshtein_join(self.left_dataframe, self.right_dataframe, self.left_matching_index,
                                                self.right_matching_index)
        else:
            comparison = None

        return comparison

    @staticmethod
    def calculate_distance(df: pd.DataFrame, a: str, b: str, error_tolerance=0.05) -> float:
        """Applies difference ratio (from 0 to 1) between each record on given pandas DataFrame
            using Levenshtein distance.
            Difference is calculated between x column and y column.

        Args:
            df: given dataset of iteration
            a: column_x name
            b: column_y name
            error_tolerance: the tolerance is used for comparing numbers. Difference ratio for numbers can be 0, 1 or
            number between 0 and the tolerance. By default its set to 0.05.

        Returns:
            Difference ratio represented in a float number
        """

        try:
            # if both numbers are equal then return difference = 0
            if df[a] == df[b]:
                difference = 0
                return difference

            # if both datatype are null return difference = 0
            if pd.isna(df[a]) and pd.isna(df[b]):
                difference = 0
                return difference

            else:
                # if one of the datatype is null then treat is as a 0
                if pd.isna(df[a]):
                    df[a] = 0

                if pd.isna(df[b]):
                    df[b] = 0

                # if one of the datatype is datetime then treat is as a "strformat"
                if isinstance(df[a], datetime.datetime):
                    df[a] = df[a].strftime("%Y-%m-%d")

                if isinstance(df[b], datetime.datetime):
                    df[b] = df[b].strftime("%Y-%m-%d")

                # For comparing numbers
                if all(
                        [
                            isinstance(df[a], (int, float, bool)),
                            isinstance(df[b], (int, float, bool)),
                        ]
                ):
                    higher_value = float(max([df[a], df[b]]))
                    lower_value = float(min([df[a], df[b]]))
                    if lower_value == 0:
                        lower_value = 0.01

                    difference = round(abs(1 - higher_value / lower_value), 2)

                    if difference > error_tolerance:
                        difference = 1

                # For comparing strings
                else:

                    similarity = SequenceMatcher(
                        None, str(df[a]).lower(), str(df[b]).lower()
                    ).ratio()

                    if similarity < 0.6:
                        difference = 1
                    else:
                        difference = round(1.00 - similarity, 2)

                return difference
        except KeyError:
            # In case there is no counterpart column
            return 1

    def compute_distances(self, df: pd.DataFrame) -> pd.DataFrame:

        # Calculate distance for each column
        for _ in df.columns:

            if _[-2:] == "_x":  # for each _x column (ground truth)
                x_column = _  # column which has _x suffix (from ground truth)
                new_column = ("diff_" + _[:-2])  # column which has diff_ prefix with calculated difference
                y_column = _[:-2] + "_y"  # column which has _y suffix (some dataset)

                # Calculate Levenshtein difference between each record in column x and column y
                df[new_column] = df.apply(
                    partial(self.calculate_distance, a=x_column, b=y_column), axis=1
                )

        return df

    @staticmethod
    def sort_columns(df: pd.DataFrame) -> list:
        """Performs sorts operation on comparison dataframe in order of file_name, distance, diff_total, col_1_x,
            col_1_y, diff_col_1 ... diff_col_n

        Args:
            df: Pandas Dataframe object containing comparison results

        Returns: List of sorted columns

        """
        arr = ["file_name", "distance", "diff_total"]
        for _ in df.columns:

            if _[-2:] == "_x":
                arr.append(_)
                arr.append(_[:-2] + "_y")
                arr.append("diff_" + _[:-2])

        return arr
