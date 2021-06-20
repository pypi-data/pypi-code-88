"""
A simple script that converts the exported xml from ASC into two files
that is in the format expected to be imported into ManageBac.

USAGE:

poetry run asc2mb XML_FILE TIMETABLE_CSV CLASSES_CSV

XML_FILE is path to the XML file
TIMETABLE_CSV is path where the timetable csv will be written to
CLASSES_CSV is path where the classes csv will be written to

Copyright 2021 Adam Morris Adam Morris adam.morris@fariaedu.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

import xml.etree.ElementTree as ET
import re
import click


@click.command()
@click.argument('xml_file', type=click.Path(exists=True))
@click.argument('timetable_csv', type=click.Path(writable=True))
@click.argument('classes_csv', type=click.Path(writable=True))
def main(xml_file, timetable_csv, classes_csv):
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
    timetable_file= []

    if grouptype == 1:
        for lesson_id, lesson in lessons.items():
            subject_id = lesson.get('subjectid')
            subject = lookup.get('subjects').get(subject_id)
            teachers = NullList(lesson.get('teacherids').split(','))
            groups = NullList(lesson.get('groupids').split(','))
            classes = NullList(lesson.get('classids').split(','))

            largest = max(map(lambda x: len(x), [groups, classes]))

            for index in range(largest):
                teacher_id = teachers[index]
                group_id = groups[index]
                class_id = classes[index]

                teacher = lookup.get('teachers').get(teacher_id) if teacher_id is not None else {}
                group = lookup.get('groups').get(group_id) if group_id is not None else {}
                class_ = lookup.get('classes').get(class_id) if class_id is not None else {}
                if class_.get('short') == '6A1':
                    pass #print(lesson)

                cards = lookup.get('cards').get(lesson_id)
                divisiontag = group.get('divisiontag', '0')

                df = '<>'

                # (Class name + divisiontag {if divisiontag=0  then null else divisiontag} + Subject Short name)
                uniq = f"{class_.get('short')} {divisiontag if divisiontag!='0' else ''}{subject.get('short')}"
                section = class_.get('short', df) if divisiontag == "0" else f"{class_.get('short', df)}({divisiontag})"
                year = re.match(r'^[\d]+', class_.get('short', '0'))

                classes_file.append([uniq, class_.get('name', df), f"Grade {year.group()}", subject.get('short', df), '', section])

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

    import csv
    with open(timetable_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Class ID', 'Day', 'Period', 'Classroom'])
        for row in timetable_file:
            writer.writerow(row)


    with open(classes_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Class ID', 'Year', 'Group', 'Subject', 'Name', 'Section'])
        for row in classes_file:
            writer.writerow(row)

    print('Process complete.')


