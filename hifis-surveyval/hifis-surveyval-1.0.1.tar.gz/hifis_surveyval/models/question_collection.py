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
This module contains classes to represent groups of survey questions.

These can be constructed from YAML through the YamlConstructable abstract
class.
"""
from typing import Dict, List
from typing import Optional as typing_Optional
from typing import Union

from pandas import DataFrame, Series, concat
from schema import Optional, Schema

from hifis_surveyval.models.mixins.identifiable import Identifiable
from hifis_surveyval.models.mixins.yaml_constructable import (
    YamlConstructable,
    YamlDict,
)
from hifis_surveyval.models.question import Question
from hifis_surveyval.models.translated import Translated


class QuestionCollection(YamlConstructable, Identifiable):
    """
    QuestionCollections group a set of questions into a common context.

    This kind of question has no answers by itself. These are to be found in
    the according sub-questions.
    """

    token_ID = "id"
    token_LABEL = "label"
    token_TEXT = "text"
    token_QUESTIONS = "questions"

    schema = Schema(
        {
            token_ID: str,
            token_LABEL: str,
            token_TEXT: dict,
            Optional(token_QUESTIONS, default=[]): list,
            Optional(str): object,  # catchall
        }
    )

    def __init__(
        self,
        collection_id: str,
        text: Translated,
        label: str,
        questions: List[Question],
    ) -> None:
        """
        Initialize an empty question collection.

        It is recommended to refer to from_yaml_dictionary() for constructing
        instances when parsing metadata.

        Args:
            collection_id:
                The unique ID that is to be assigned to the collection.
            text:
                A Translated object representing the text that describes the
                question collection.
            label:
                A short label that can be used in plotting to represent the
                question collection.
            questions:
                A list of questions that are contained within the question
                collection.
        """
        super().__init__(collection_id)  # Question Collections have no parents
        self._text: Translated = text
        self._label: str = label
        self._questions: Dict[str, Question] = {
            question.short_id: question for question in questions
        }

    def question_for_id(self, question_short_id: str) -> Question:
        """
        Obtain a question from the collection for a given short ID.

        Args:
            question_short_id:
                The short id used within the collection for this question.
        Returns:
            The question for the given ID.
        Raises:
            KeyError - if no question with the given ID did exist.
        """
        return self._questions[question_short_id]

    def as_data_frame(
        self, exclude_labels: typing_Optional[Union[str, List[str]]] = None
    ) -> DataFrame:
        """
        Gather the answers given to each question as a data frame.

        Args:
            exclude_labels:
                A short label or a list of short labels for questions that
                are to be excluded from the data frame.

        Returns:
            A pandas data frame with participants in the rows and the
            questions of this collection in the columns. The fields in
            the data frame then contain the answer to a question for a
            given participant.
        """
        excluded = []
        if isinstance(exclude_labels, str):
            excluded.append(exclude_labels)
        elif isinstance(exclude_labels, list):
            excluded.extend(exclude_labels)
        # Nothing to do in any other case

        question_series: List[Series] = []
        for (label, question) in self._questions.items():
            if label in excluded:
                continue
            question_series.append(question.as_series())
        return concat(question_series, axis=1)  # Note (0)

    # Note (0) The series are joined row-wise, so each participant in the
    # row labels (aka indexes) is associated with each answer according to
    # the question (Question ID in the column labels).

    @staticmethod
    def _from_yaml_dictionary(
        yaml: YamlDict, **kwargs
    ) -> "QuestionCollection":
        """
        Generate a new QuestionCollection-instance from YAML data.

        Args:
            yaml:
                A YAML dictionary describing the Question
            **kwargs:
                Only here to satisfy the inherited method signature.
        Returns:
            A new Question containing the provided data
        """
        collection_id = yaml[QuestionCollection.token_ID]

        questions = [
            Question.from_yaml_dictionary(
                yaml=question_yaml, parent_id=collection_id
            )
            for question_yaml in yaml[QuestionCollection.token_QUESTIONS]
        ]

        text = Translated.from_yaml_dictionary(
            yaml[QuestionCollection.token_TEXT]
        )

        return QuestionCollection(
            collection_id=collection_id,
            text=text,
            label=yaml[QuestionCollection.token_LABEL],
            questions=questions,
        )
