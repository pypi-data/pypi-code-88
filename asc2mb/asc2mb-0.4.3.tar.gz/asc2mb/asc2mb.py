"""
A simple script that converts the exported xml from ASC into two files
that is in the format expected to be imported into ManageBac.

USAGE:
asc2mb --help

Copyright 2021 Adam Morris Adam Morris adam.morris@classroomtechtools.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

import xml.etree.ElementTree as ET
import re
import click
import csv

from collections import UserDict
#from simpleeval import simple_eval


class Json(UserDict):
    def __init__(self, data={}, default=''):
        UserDict.__init__(self, data)
        self.default = default

    def __getattr__(self, key):
        """
        Not in here, return the default
        """
        if not self.__dict__['data']:
            return ''
        if key in self.__dict__['data'].keys():
            return self.__dict__['data'][key]
        return self.default


class Teacher(Json):
    def __init__(self, data={}, default=''):
        if not data:
            data = {"name": "Unknown Teacher"}
        Json.__init__(self, data, default)

    @property
    def email(self):
        """
        Conveniently override the email property to use an evaluated string
        """
        if 'email' in self.data:
            return self.data.email
        teacher = self
        pattern = "f'" + self.default + "'"
        return eval(pattern)

class_id_patterns = [
    {"p": "{class_.short}_{division.name}", "n":'default'},
    {"p":"{class_.short} {division.divisiontag if division.divisiontag!='0' else ''}{subject.short}", "n": "dampsdaralmarefa"}
]
pattern_choices = [pattern.get('n') for pattern in class_id_patterns]
class_id_prompt = """


ENTER 'Class ID' pattern.

To export to ManageBac, you need to specify how to map to the class ID (Class Settings -> Class ID) aka "unique ID" (class.uniq_id in the API). This can be done by viewing tHe options below, and choosing between them. If an option you need is not available, you'll need to write to the programmer and request an additional item. (Or, preferred if possible, to initiate a puill request).



"""
for ptn in class_id_patterns:
    class_id_prompt += f'{ptn.get("n")}:\n{ptn.get("p")}\n\n'

section_patterns = [
    {"p": "{int(division.divisiontag)+1}", "n": "default"},
#    {"p": "{teacher.name.split(' ')[0][0] + teacher.name.split(' ')[1][0] if len(teacher.name.split(' '))>1 else ''}", "n": 'teacher_intiails'},
    {"p": "{class_.short if division.divisiontag == '0' else f'{class_.short}({division.divisiontag})'}", 'n': 'dampsdaralmarefa'}
]
section_prompt = """

Enter 'Section' pattern.

Optionally, every class can be assigned a section. It is useful to have idewntifying information; it may be as simple as a number or perhaps the teachers initials

"""
for ptn in section_patterns:
    section_prompt += f'{ptn.get("n")}\n{ptn.get("p")}\n\n'


def get_pattern(patterns, target):
    return 'f"' + [ptn for ptn in patterns if ptn.get('n') == target].pop().get('p') + '"'


@click.command()
@click.argument('xml_file', type=click.Path(exists=True))
@click.argument('timetable_csv', type=click.Path(writable=True))
@click.argument('classes_csv', type=click.Path(writable=True))
@click.option('--class_id_pattern', prompt=class_id_prompt, type=click.Choice(pattern_choices), default='default')
@click.option('--class_id_prefix', prompt="Prefix for class id?", default='')
@click.option('--class_id_suffix', prompt="Suffix for class id?", default='')
@click.option('--section_pattern', prompt=section_prompt, default='default')
@click.option('--teacher_email_pattern', default='{".".join(teacher.name.split(' ')) + "@example.com"}')
def main(xml_file, timetable_csv, classes_csv, class_id_pattern, class_id_prefix, class_id_suffix, section_pattern, teacher_email_pattern):
    mytree = ET.parse(xml_file)
    myroot = mytree.getroot()

    # find the group type, assume grouptype = 1 if not present
    grouptype = 1 if 'groupstype1' in (myroot.attrib.get('options') or ['groupstype1']).split(',') else 2
    lookup = {}

    class NullList(list):
        def __getitem__(self, index):
            if index > len(self)-1:
                return None
            return list.__getitem__(self, index)

    for child in myroot:
        name = child.tag
        lookup[name] = {}
        for grandkid in child:
            values = grandkid.attrib
            id_ = values.get('id')
            if not id_ is None:
                lookup[name][id_] = values
            elif name == 'cards':
                id_ = values.get('lessonid')
                if not id_ in lookup['cards']:
                    lookup['cards'][id_] = []
                lookup['cards'][id_].append(values)


    lessons = lookup.get('lessons')
    subjects = lookup.get('subjects')
    classes_file = []
    timetable_file = []

    if grouptype == 1:
        for lesson_id, lesson in lessons.items():
            subject_id = lesson.get('subjectid')
            subject = Json(lookup.get('subjects').get(subject_id))
            teachers = NullList(lesson.get('teacherids').split(','))
            groups = NullList(lesson.get('groupids').split(','))
            classes = NullList(lesson.get('classids').split(','))

            largest = max(map(lambda x: len(x), [groups, classes]))
            # use this if no teacher provided in subsequent ones...
            teacher_emails_list = []
            for teacher_id in teachers:
                teacher = lookup.get('teachers').get(teacher_id)
                teacher_obj = Teacher(teacher, teacher_email_pattern)
                teacher_emails_list.append(teacher_obj)
            teacher_emails = "|".join([teacher.email for teacher in teacher_emails_list])

            for index in range(largest):
                teacher_id = teachers[index]
                group_id = groups[index]
                class_id = classes[index]

                # if teacher.email not present, it'll return evaluation string
                # teacher = Teacher(lookup.get('teachers').get(teacher_id), teacher_email_pattern) if teacher_id else (first_teacher or Teacher({"name": "Unknown Teacher"}))
                division = Json(lookup.get('groups').get(group_id)) if group_id is not None else Json()
                class_ = Json(lookup.get('classes').get(class_id)) if class_id is not None else Json()

                # all of the card placements
                cards = lookup.get('cards').get(lesson_id)

                # (Class name + divisiontag {if divisiontag=0  then null else divisiontag} + Subject Short name)
                uniq = eval(get_pattern(class_id_patterns, class_id_pattern))
                section = eval(get_pattern(section_patterns, section_pattern))
                match = re.match(r'^[\d]+', class_.short)
                if match is None:
                    print("No grade? Using 0 instead", class_)
                    year = 0
                else:
                    year = match.group()
                classes_file.append([uniq, f"Grade {year}", division.name, subject.short, '', teacher_emails, section])
                for card in cards:
                    classrooms = map(lambda x: lookup.get('classrooms').get(x), card.get('classroomids').split(','))
                    day = card.get('day')
                    period = card.get('period')
                    for classroom in classrooms:
                        timetable_file.append([uniq, day, period, (classroom or {'short': '<>'}).get('short', '')])

    elif grouptype == 2:
        print('not implemented yet')
        exit(0)

    else:
        print("uknown group type")
        exit(0)

    with open(timetable_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Class ID', 'Day', 'Period', 'Classroom'])
        for row in timetable_file:
            writer.writerow(row)

    with open(classes_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Class ID', 'Year', 'Group', 'Subject', 'Name', 'Teacher Email', 'Section'])
        for row in classes_file:
            writer.writerow(row)

    print('Process complete.')


