import json
import re
import sys

def add_toc(input):
    """ Function to include a table of content on a jupyter notebook based on its
        markdown. It receives a file path as input, and creates a new notebook
        file that includes the table of content in the same path.
        It performs some style fix during the process. For more information see
        the attached notebook example.

    Args:
        input ([strin]): The notebook file to be formated
    """
    try:
        with open(input) as f:
            notebook = json.load(f)

        cells = notebook['cells']

        head_cell = cells[0]

        part = 0
        section = 0
        exercise = 0

        toc = ['\n', '## Outline\n']

        for cell in cells[1: len(cells)]:
            if cell['cell_type'] == 'markdown':
                source_array = cell['source']
                row = 0
                skip = False
                for source in source_array:
                    if not skip:
                        if re.search('^[#]+ Introduction', source, re.IGNORECASE):

                            html_tag = '<a name="0"></a>\n'
                            if row > 0 and source_array[row - 1].find('<a name=') >= 0:
                                source_array[row - 1] = html_tag
                            else:
                                source_array.insert(row, html_tag)
                                row += 1

                            toc.append('- [Introduction](#0)\n')
                            source_array[row] = '# Introduction\n'
                            skip = True

                        if isPart(source):
                            part += 1
                            name = partName(source)
                            html_tag = '<a name="' + str(part) + '"></a>\n'

                            if row > 0 and source_array[row - 1].find('<a name=') >= 0:
                                source_array[row - 1] = html_tag
                            else:
                                source_array.insert(row, html_tag)
                                row += 1

                            toc.append('- [Part ' + str(part) + ': ' +
                                       name + '](#' + str(part) + ')\n')
                            # Fix source line if needed
                            source_array[row] = '# Part ' + \
                                str(part) + ': ' + name + '\n'

                            section = 0
                            skip = True

                        if re.search('^## [0-9]+.[0-9]+', source, re.IGNORECASE):
                            section += 1  # Increase section

                            label = str(part) + '.' + str(section)
                            name = sectionName(source)
                            html_tag = '<a name="' + label + '"></a>\n'

                            if row > 0 and source_array[row - 1].find('<a name=') >= 0:
                                source_array[row - 1] = html_tag
                            else:
                                source_array.insert(row, html_tag)
                                row += 1

                            toc.append(
                                '    - [' + label + ' ' + name + '](#' + label + ')\n')

                            # Fix source line if needed
                            source_array[row] = '## ' + \
                                label + ' ' + name + '\n'

                            skip = True

                        if re.search('^### Exercise [0-9]', source, re.IGNORECASE):
                            exercise += 1
                            label = "{:02d}".format(exercise)
                            html_tag = '<a name="ex' + label + '"></a>\n'

                            if row > 0 and source_array[row - 1].find('<a name=') >= 0:
                                source_array[row - 1] = html_tag
                            else:
                                source_array.insert(row, html_tag)
                                row += 1
                            ident = '\t\t'
                            if section == 0:  # There is not subsection
                                ident = '\t'

                            toc.append(
                                ident + '- [Exercise ' + label + '](#ex' + label + ')\n')

                            source_array[row] = '### Exercise ' + label + '\n'
                            skip = True
                    else:
                        skip = False
                        row -= 1
                    row += 1
            # Clear outputs and reset the execution count
            if cell['cell_type'] == 'code':
                cell['execution_count'] = 0
                cell['outputs'] = []

        # Remove the old toc
        toc_line = 0
        for line in head_cell['source']:
            if re.search('^## Outline', line, re.IGNORECASE):
                head_cell['source'] = head_cell['source'][0: toc_line]
                break
            toc_line += 1

        head_cell['source'] = head_cell['source'] + toc

        with open(input.replace('.ipynb', '_toc.ipynb'), 'w') as file:
            file.write(json.dumps(notebook, indent=2))

    except ValueError:
        print("Error during deployment")
        print(ValueError)


def isPart(line):
    if re.search('^# Part [0-9]+:', line, re.IGNORECASE) \
            or re.search('^# [0-9]+', line, re.IGNORECASE):
        return True
    return False


def partName(line):
    title_search = re.search('^# Part [0-9]+:', line, re.IGNORECASE)
    if title_search:
        return re.sub(r'# Part [0-9]+:', '', line).replace('\n', '')

    else:
        title_search = re.search('^# [0-9]+', line, re.IGNORECASE)
        if title_search:
            return re.sub(r'# [0-9]+', '', line).replace('\n', '')


def sectionName(line):
    title_search = re.search('^## [0-9]+.[0-9]+', line, re.IGNORECASE)
    if title_search:
        return re.sub(r'## [0-9]+.[0-9]+', '', line).replace('\n', '')


if __name__ == "__main__":
    add_toc(sys.argv[1])