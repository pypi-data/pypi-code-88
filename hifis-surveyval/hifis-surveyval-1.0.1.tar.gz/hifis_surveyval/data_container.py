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
This module provides the definitions for a data container.

The container is meant to serve as the data source for the individual analysis
functions.

.. currentmodule:: hifis_surveyval.data_container
.. moduleauthor:: HIFIS Software <software@hifis.net>
"""

from logging import warning
from typing import Dict, List, Union

from hifis_surveyval.models.mixins.identifiable import Identifiable
from hifis_surveyval.models.mixins.yaml_constructable import YamlDict, YamlList
from hifis_surveyval.models.question import Question
from hifis_surveyval.models.question_collection import QuestionCollection


class DataContainer(object):
    """The data container holds the data read from the command line."""

    #: Name of the ID column in the Limesurvey CSV data
    ID_COLUMN_NAME: str = "id"

    def __init__(self):
        """Set up an empty data container."""
        self._survey_questions: Dict[str, QuestionCollection] = {}

    @property
    def survey_questions(self) -> List[QuestionCollection]:
        """
        Obtain all survey questions stored in the data container.

        Returns:
            A list of QuestionCollections that contain all the survey
            questions.
        """
        return list(self._survey_questions.values())

    def load_metadata(self, yaml: Union[YamlList, YamlDict]) -> None:
        """
        Load additional metadata from YAML data.

        If the given yaml is valid, the received metadata will be added to the
        known survey questions.
        QuestionCollections that fail to parse will not be added to the survey
        questions and the exception will instead be logged as a warning.
        It is safe to repeatedly call this function, if multiple sources for
        metadata need to be processed.

        Args:
            yaml:
                Either a list of YamlDictionaries or a single YamlDictionary.
                Each YamlDictionary is expected to hold a QuestionCollection,
                Otherwise parsing will fail.
        """
        if not isinstance(yaml, list):
            # in case this is a single value put it in the list for the
            # one-size-fits-all solution below
            yaml = [yaml]

        for new_collection_data in yaml:
            try:
                self._add_collection_from_yaml(new_collection_data)
            except Exception as thrown_exception:
                warning(f"Error while parsing metadata: {thrown_exception}")

    def _add_collection_from_yaml(self, new_collection_yaml: YamlDict) -> None:
        """
        Create a new question collection from YAML and add it to survey data.

        Args:
            new_collection_yaml:
                A YAML mapping containing the data for one question collection.
        """
        new_collection = QuestionCollection.from_yaml_dictionary(
            new_collection_yaml
        )
        if new_collection.full_id in self._survey_questions:
            raise ValueError(
                "Attempt to add QuestionCollection " "with duplicate ID"
            )
        self._survey_questions[new_collection.full_id] = new_collection

    def load_survey_data(self, csv_data: List[List[str]]) -> None:
        """
        Load survey data as given in a CSV file.

        The data is expected to be given in such a way that the outer list
        represents the rows and the inner list the columns within each row
        """
        # Separate the header so it does not get in the way of processing later
        header: List[str] = csv_data[0]
        body: List[List[str]] = csv_data[1:]

        question_cache: Dict[int, Question] = {}
        # The question cache associates column indices with questions
        # It is here to avoid having to constantly look up the questions all
        # over again. This expects that in each row the indices for the
        # questions are identical.

        # Step 1: Find the column for the participant IDs
        id_column_index = header.index(DataContainer.ID_COLUMN_NAME)

        # Step 2: Find the Question for each of the headings
        for index in range(0, len(header)):
            potential_question_id = header[index]
            try:
                question = self.question_for_id(potential_question_id)
                question_cache[index] = question
            except (KeyError, IndexError):
                # TODO: log ignored columns for potential CSV debugging?
                continue

        assert id_column_index not in question_cache

        # Step 3: Iterate through each row and insert the values for answer
        for row in body:
            participant_id = row[id_column_index]

            for (question_index, question) in question_cache.items():
                answer: str = row[question_index]
                question.add_answer(participant_id, answer)

    def collection_for_id(self, full_id: str) -> QuestionCollection:
        """
        Query for a given question collection given by its full ID.

        Args:
            full_id:
                The full ID of the question collection to be returned.
        Returns:
            The question collection for the given ID.
        Raises:
            KeyError - if the collection for the given ID could not be found.
        """
        return self._survey_questions[full_id]

    def question_for_id(self, full_id: str) -> Question:
        """
        Query for a given question given by its full ID.

        This is a shorthand for querying questions directly.

        Args:
            full_id:
                The full ID of the question to be returned.
        Returns:
            The question for the given ID.
        Raises:
            KeyError - if either the collection or the question for the given
            ID could not be found.
        """
        parts: List[str] = full_id.split(Identifiable.HIERARCHY_SEPARATOR)
        collection_id = parts[0]
        question_id = parts[1]
        collection = self.collection_for_id(collection_id)
        return collection.question_for_id(question_id)
