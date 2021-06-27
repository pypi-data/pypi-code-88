import sys
import os
import subprocess
from texsurgery.texsurgery import TexSurgery
import argparse
import shutil

parser = argparse.ArgumentParser(
    description='TexSurgery passes code from latex files to jupyter kernels, '
                'and substitutes it by the corresponding output.'
)
parser.add_argument("input_file",
                    default=None,
                    nargs='?',
                    help="file to parse. Uses stdin if none given.")
parser.add_argument("-pdf",
                    action="store_true",
                    help="create a pdf file from the modified latex (requires pdflatex installed).")
parser.add_argument("-tex",
                    action="store_true",
                    help="just produce the modified latex (default).")
parser.add_argument("-replace",
                    nargs=2,
                    dest='replace',
                    help="finds a selector, replaces the first match with the replacement text, outputs the result")
parser.add_argument("-find",
                    nargs=1,
                    dest='find',
                    help="finds a selector, output the code for the innermost part of the selector")
parser.add_argument("-shuffle",
                    nargs=2,
                    dest='shuffle',
                    help="finds a parent selector, and shuffles all matches of the children selector within the parent, then outputs the result")
parser.add_argument("-randomseed",
                    nargs=1,
                    dest='randomseed',
                    default=1,
                    help="randomseed for -shuffle")
parser.add_argument("--output_file", "-o", help="file to write the output to.")
parser.add_argument('--pdflatex-options',
                    default=None,
                    nargs=argparse.REMAINDER,
                    help="options to pass to pdflatex (requires the -pdf option)")

def main():
    args = parser.parse_args()
    if args.pdflatex_options and not args.pdf:
        print("--pdflatex-options requires -pdf.")
        quit()
    if args.tex and args.pdf:
        print("Only one option among -pdf and -tex can be used.", file=sys.stderr)
        quit()
    if not args.input_file and not args.output_file and args.pdf:
        print("Can't determine pdf file to write to", file=sys.stderr)
        quit()
    if args.input_file:
        with open(args.input_file) as fd:
            tex_source = fd.read()
    else:
        tex_source = sys.stdin.read()
    ts = TexSurgery(tex_source, verbose=False)
    if args.find:
        found = ts.find(' '.join(args.find))
        if found:
            innermost = found[-1]
            modified_tex = str(innermost)
        else:
            modified_tex = ''
    elif args.replace:
        modified_tex = ts.replace(args.replace[0], args.replace[1]).src
    elif args.shuffle:
        modified_tex = ts.shuffle(
            args.shuffle[0], args.shuffle[1], randomseed=int(args.randomseed[0])).src
    else:
        modified_tex = ts.code_surgery().src
    if args.pdf:
        if args.output_file:
            outfile = args.output_file
        else:
            outfile = args.input_file
            if len(outfile) > 4 and outfile[-4:].lower() == '.tex':
                outfile = outfile[:-4]+'.pdf'
            else:
                outfile = outfile + '.pdf'
        out_base_name = os.path.basename(outfile)
        temp_file = out_base_name+'.temp.tex'
        with open(temp_file, 'w') as fd:
            fd.write(modified_tex)
        if args.pdflatex_options:
            pdfcommand = ['pdflatex'] + args.pdflatex_options + [temp_file]
        else:
            pdfcommand = ['pdflatex', temp_file]
        subprocess.run(pdfcommand)
        shutil.move(out_base_name+'.temp.pdf', outfile)
        os.remove(temp_file)
        quit()
    if args.output_file:
        with open(args.output_file, 'w') as fd:
            fd.write(modified_tex)
    else:
        sys.stdout.write(modified_tex)
