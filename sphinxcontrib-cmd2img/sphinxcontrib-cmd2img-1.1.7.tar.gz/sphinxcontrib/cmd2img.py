# -*- coding: utf-8 -*-
"""
    sphinxcontrib.cmd2img
    ~~~~~~~~~~~~~~~~~~~~~

    Allow cmd2img commands be rendered as nice looking images
    

    See the README file for details.

    :author: Vadim Gubergrits <vadim.gubergrits@gmail.com>
    :license: BSD, see LICENSE for details

    Inspired by ``sphinxcontrib-aafig`` by Leandro Lucarella.
"""

import re, os
import posixpath
from os import path
import shutil
import copy
from subprocess import Popen, PIPE
import shlex
import imghdr

try:
    # Python 2.
    from StringIO import StringIO
    # Python 3.
except ImportError:
    from io import StringIO

try:
    from hashlib import sha1 as sha
except ImportError:
    from sha import sha

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.errors import SphinxError
from sphinx.util import ensuredir, relative_uri

OUTPUT_DEFAULT_FORMATS = dict(html='svg', latex='pdf', text=None)
OWN_OPTION_SPEC = dict( { 'caption': str,
    'size': str,
    'suffix': str,
    'convert': str,
    'show_source': str,
    })

class Cmd2imgError(SphinxError):
    category = 'cmd2img error'

class Cmd2figDirective(directives.images.Figure):
    """
    Directive that builds figure object.
    """
    has_content = True
    required_arguments = 0
    option_spec = directives.images.Figure.option_spec.copy()
    option_spec.update(OWN_OPTION_SPEC)
  
    def run(self):
        self.arguments = ['']
        total_options = self.options.copy()

        cmd = self.content[0]
        text = '\n'.join(self.content[1:])
        own_options = dict([(k,v) for k,v in self.options.items() 
                                  if k in OWN_OPTION_SPEC])

        # Remove the own options from self-options which will be as figure
        # options.
        for x in own_options.keys():
            self.options.pop(x)

        # don't parse the centent as legend, it's not legend.
        self.content = None

        (node,) = directives.images.Figure.run(self)
        if isinstance(node, nodes.system_message):
            return [node]

        node.cmd2img = dict(cmd=cmd,text=text,options=own_options,suffix="cmd2img",
                directive="cmd2fig", total_options=total_options)
        return [node]

class Cmd2imgDirective(directives.images.Image):
    """
    Directive that builds image object.
    """
    has_content = True
    required_arguments = 0
    option_spec = directives.images.Image.option_spec.copy()
    option_spec.update(OWN_OPTION_SPEC)
  
    def run(self):
        self.arguments = ['']
        #print ("%s start!self.options: %s" %(self.__class__.__name__, self.options))
        total_options = self.options.copy()

        # Parse the cmd/options/text
        cmd = self.content[0]
        own_options = dict([(k,v) for k,v in self.options.items() 
                                  if k in OWN_OPTION_SPEC])
        text = '\n'.join(self.content[2:])

        # Remove the own defined options from self-options, which will be as
        # figure options.
        for x in own_options.keys():
            self.options.pop(x)

        (node,) = directives.images.Image.run(self)
        if isinstance(node, nodes.system_message):
            return [node]

        node.cmd2img = dict(cmd=cmd,text=text,options=own_options,suffix="cmd2img",
                directive="cmd2img", total_options=total_options)
        return [node]

# http://epydoc.sourceforge.net/docutils/
def render_cmd2img_images(app, doctree):

    for fig in doctree.traverse(nodes.figure):
        if not hasattr(fig, 'cmd2img'):
            continue

        cmd = fig.cmd2img['cmd']
        text = fig.cmd2img['text']
        options = fig.cmd2img['options']

        try:
            #relfn, outfn, relinfile = cmd_2_image(app, fig.cmd2img)
            out = cmd_2_image(app, fig.cmd2img)
            caption_node = nodes.caption("", options.get("caption", cmd))
            fig += caption_node
            fig['ids'] = "cmd2fig"
            #img = fig.children[fig.first_child_matching_class(nodes.image)]
            for img in fig.traverse(condition=nodes.image):
                img['uri'] = out["outrelfn"]
                if out["outreference"]:
                    reference_node = nodes.reference(refuri=out["outreference"])
                    reference_node += img
                    fig.replace(img, reference_node)
                #img['candidates']={'*': out["outfullfn"]}

            #if options.get("show_source", False):
            #    # rendere as a text
            #    fig["align"] = "left"
            #    fig.insert(0, nodes.literal_block("", "%s\n%s" %(cmd, text), align = "left"))
            #print("rending figure: %s" %(fig))
        except Cmd2imgError as err:
            #app.builder.warn('cmd2img error: ')
            print(err)
            fig.replace_self(nodes.literal_block("", "%s\n%s" %(cmd, text)))
            continue

    for img in doctree.traverse(nodes.image):
        if not hasattr(img, 'cmd2img'):
            continue

        text = img.cmd2img['text']
        options = img.cmd2img['options']
        cmd = img.cmd2img['cmd']
        try:
            #relfn, outfn, relinfile = cmd_2_image(app, img.cmd2img)
            out = cmd_2_image(app, img.cmd2img)
            img['uri'] = out["outrelfn"]
            if out["outreference"]:
                reference_node = nodes.reference(refuri=out["outreference"])
                img.replace_self(reference_node)
                reference_node.append(img) 
            #if options.get("show_source", False):
            #    img.insert(0, nodes.literal_block("", "%s\n%s" %(cmd, text)))
        except Cmd2imgError as err:
            #app.builder.warn('cmd2img error: ')
            print(err)
            img.replace_self(nodes.literal_block("", "%s\n%s" %(cmd, text)))
            continue

def cmd_2_image (app, cmd2img):
    """Render cmd2img code into a PNG output file."""
    #print("app.builder.format: %s" %(app.builder.format))
    #print("app.builder.env.docname: %s" %(app.builder.env.docname))
    #print("app.builder.imagedir: %s" %(app.builder.imagedir))

    cmd = cmd2img['cmd']
    text = cmd2img['text']
    options = cmd2img['options']
    format = app.builder.format
    cmd_args = shlex.split(cmd)
    rel_imgpath = relative_uri(app.builder.env.docname, app.builder.imagedir)
    hashkey = cmd + str(options) + text
    hashkey = sha(hashkey.encode('utf-8')).hexdigest()
    infname = '%s-%s.%s' % (cmd_args[0], hashkey, cmd2img['suffix'])
    infullfn = path.join(app.builder.outdir, app.builder.imagedir, infname)
    ensuredir(path.join(app.builder.outdir, app.builder.imagedir))
    currpath = os.getcwd() # Record the current dir and return here afterwards

    if options.get("suffix", None): # User definition is the 1st choice.
        suffix = options["suffix"]
    elif ((cmd_args[0] == "gnuplot") or
            ((cmd_args[0] == "ditaa") and
                ('--svg' in cmd_args) and
                not options.get("convert", None))):
        # Now: gnuplot and ditaa support vector image: .svg, .pdf
        format_map = OUTPUT_DEFAULT_FORMATS.copy()
        format_map.update(app.builder.config.cmd2img_output_format)
        suffix = format_map.get(app.builder.format, "png")
    else:
        suffix = "png"

    outfname = '%s-%s.%s' %(cmd_args[0], hashkey, suffix)
    out = dict(outrelfn = posixpath.join(rel_imgpath, outfname),
        outfullfn = path.join(app.builder.outdir, app.builder.imagedir, outfname),
        #outreference = posixpath.join(rel_imgpath, infname),
        outreference = None)
    #print(out)

    if path.isfile(out["outfullfn"]):
        print("file has already existed: %s" %(outfname))
        return out

    if cmd_args[0] == "ditaa":
        cmd_args.extend([infname, outfname])
        # Ditaa must work on the target directory.
        os.chdir(path.join(app.builder.outdir, app.builder.imagedir))
    elif cmd_args[0] == "dot":
        # dot -Tpng in_file -o out_file
        cmd_args.extend([infullfn, '-o', out["outfullfn"]])
    elif cmd_args[0] == "python" or cmd_args[0] == "python3" or cmd_args[0] == "python2":
        # change the embeded output file.
        text = re.sub(r'savefig\((.+)\)',
                r'savefig("%s")' %(out["outfullfn"]),
                text)
        cmd_args.append(infullfn)
    elif cmd_args[0] == "gnuplot":
        size = None
        if ('size' in options):
            if (suffix in ["pdf", "eps"]):
                if "," in options["size"]:
                    # pdf unit is inch while png is pixel, convert them.
                    tmp = map(lambda x: int(x.strip())/100, options["size"].split(","))
                    size = ",".join("%d"%(i) for i in tmp)
                else:
                    print("size %s is not valid." %(options["size"]))
            else:
                size = options["size"]
        #pdf/pdfcairo/epscairo
        t = suffix
        term = size and ("%s size %s" %(t, size)) or t
        #print("term: %s" %(term))

        # change the embeded output file, suffix is terminal name.
        #print("^\s*[^#].*output.*$" in text)
        if ("^\s*[^#].*output.*$" in text):
            text = re.sub(r'set\s+output (.+)',
                    r'set output "%s"' %(out["outfullfn"]), text)
        else:
            text = 'set output "%s"\n' %(out["outfullfn"]) + text

        #print("^\s*[^#].*terminal.*$" in text)
        if ("^\s*[^#].*terminal.*$" in text):
            text = re.sub(r'set\s+term(.*)', r'set term %s' %(term), text)
        else:
            text = 'set terminal %s\n' %(term) + text

        cmd_args.append(infullfn)
    elif cmd_args[0] == "convert":
        # Attach the body and change the embeded output file.
        if text:
            for i in StringIO(text).readlines():
                cmd_args.extend(shlex.split(i.rstrip("\r\n\\")))
        cmd_args[-1] = out["outfullfn"]
    else:
        cmd_args.append(infullfn)

    # write the text as infile.
    with open(infullfn, 'wb') as f:
        f.write(text.encode('utf-8'))

    # 2) generate the output file
    try:
        print(' '.join(cmd_args))
        p = Popen(cmd_args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        stdout, stderr = (p.stdout.read().decode("utf-8"),
                p.stderr.read().decode("utf-8"))
        print("[31m%s[1;30m%s[0m" %(stderr, stdout))
    except OSError as err:
        os.chdir(currpath)
        raise Cmd2imgError('[1;31m%s[0m' %(err))

    # We'd like to change something after image is generated:
    if options.get("convert", None):
        c = "convert %s" %(out["outfullfn"])
        for i in StringIO(options["convert"]).readlines():
            if (i.lstrip()[0] != "#"):
                c += " %s" %(i.strip().rstrip("\\"))
        c += " %s" %(out["outfullfn"])
        print(c)
        os.system(c)
    if (cmd_args[0] == "ditaa") and (suffix in ['pdf']):
        # In fact ditaa don't support pdf, we convert the .svg to .pdf.
        print("mv %s %s-%s.svg" %(outfname, cmd_args[0], hashkey))
        os.system("mv %s %s-%s.svg" %(outfname, cmd_args[0], hashkey))
        print("inkscape -f %s-%s.svg -A %s" %(cmd_args[0], hashkey, out["outfullfn"]))
        os.system("inkscape -f %s-%s.svg -A %s" %(cmd_args[0], hashkey, out["outfullfn"]))


    # 3) Check if it's need to generate the outreference file
    if options.get("show_source", False):
        # Input file could be rendered as a link
        out["outreference"] = posixpath.join(rel_imgpath, infname)

    os.chdir(currpath)
    return out

def setup(app):
    app.add_directive('cmd2fig', Cmd2figDirective)
    app.add_directive('cmd2img', Cmd2figDirective)
    app.connect('doctree-read', render_cmd2img_images)
    app.add_config_value('cmd2img', 'cmd2img', 'html')
    app.add_config_value('cmd2img_args', [], 'html')
    app.add_config_value('cmd2img_log_enable', True, 'html')
    app.add_config_value('cmd2img_output_format', OUTPUT_DEFAULT_FORMATS, 'html')

#https://blog.csdn.net/wangchaoqi1985/article/details/80461850
