# -*- coding: UTF-8 -*-
# Copyright 2011-2021 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

import logging
logger = logging.getLogger(__name__)

import os
import sys
import tempfile
import subprocess
from optparse import make_option
from os.path import join, exists
from io import open
from pathlib import Path

from django.db import models
from django.conf import settings
from django.utils import translation
from django.utils.translation import gettext as _
from django.utils.encoding import force_str
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from django.apps import apps

import atelier
from atelier.projects import Project

import lino
#from lino.core.utils import app_labels
from lino.utils import curry
import rstgen
from atelier.utils import cd
from lino.utils.restify import doc2rst, abstract
from lino.core import kernel
from lino.core import actors
from lino.core import elems
from lino.core.boundaction import BoundAction
from lino.core.tables import AbstractTable
from lino.core.model import Model

from lino.api.dd import full_model_name
from lino.api import doctest

use_dirhtml = False

def runcmd(cmd, **kw):
    """Run the specified command in a subprocess.

    Stop when Ctrl-C. If the subprocess has non-zero return code, we simply
    stop. We don't use check=True because this would add another useless
    traceback.  The subprocess is responsible for reporting the reason of
    the error.

    """
    # kw.update(stdout=subprocess.PIPE)
    # kw.update(stderr=subprocess.STDOUT)
    kw.update(shell=True)
    kw.update(universal_newlines=True)
    cp = subprocess.run(cmd, **kw)
    if cp.returncode != 0:
        # subprocess.run("sudo journalctl -xe", **kw)
        raise Exception(
        "{} ended with return code {}".format(cmd, cp.returncode))



def fieldtype(f):
    if isinstance(f, models.ForeignKey):
        return f.__class__.__name__ + " to " + refto(f.remote_field.model)
    return f.__class__.__name__

def field_ref(f):
    if isinstance(f.model, Model):
        return ":ref:`{}.{}`".format(full_model_name(f.model), f.name)
    # parameter field
    return ":ref:`{}.{}`".format(str(f.model), f.name)

def report_ref(rpt):
    return ":doc:`{}`".format(str(rpt))
    # return settings.SITE.server_url + '.' + str(rpt)
    #~ return ":ref:`%s.%s`" % (settings.SITE.source_name,str(rpt))

def model_ref(model):
    return settings.SITE.source_name + '.' + model._meta.app_label + '.' + model.__name__



def refto(x):
    if x is None:
        return '`None`'
    if isinstance(x, type):
        if issubclass(x, models.Model):
            return ':doc:`' + x.__name__ + ' <' + full_model_name(x) + '>`'
    if isinstance(x, BoundAction):
        return ':doc:`{} <{}>`'.format(x.action_name, x.actor)
    return "``{}``".format(repr(x))
    #~ if isinstance(x,Field):
    # return ':ref:`' + x.verbose_name + ' <' + full_model_name(x.model) + '.' + x.name + '>`'

def verbose_name(f):
    return str(f.verbose_name or "(None)")

def help_text(f):
    # if isinstance(f, elems.FieldElement):
    #     f = f.field
    if f.help_text:
        return f.help_text
    return "See {}.".format(refto(f))

def field2par(f):
    return shortpar(f.name, verbose_name(f), help_text(f))

def shortpar(name='', label='', text=''):
    label = str(label).strip()
    text = str(text).strip()
    name = str(name).strip()
    return f"**{label}** ({name}) : {text}"

def elem2par(e):
    if isinstance(e, elems.FieldElement):
        e = e.field
        return shortpar(e.name, e.verbose_name, help_text(e))
    return refto(e)

def action2par(a):
    if isinstance(a, BoundAction):
        a = a.action
    return shortpar(a.action_name, a.label, help_text(a))

def rubric(s):
    return "\n\n.. rubric:: {}\n\n".format(s)

def model_overview(model):
    s = ""
    masters = [r for r in kernel.master_tables if r.model is model]
    if masters:
        s += "**{}** : {}\n\n".format(_("Master tables"), rptlist(masters))
    slaves = getattr(model, '_lino_slaves', None)
    if slaves:
        s += "**{}** : {}\n\n".format(_("Slave tables"), rptlist(slaves.values()))
    s += rubric("Database fields:")
    s += rstgen.ul([field2par(f) for f in model._meta.fields])
    return s

def actor_overview(rpt):
    s = ""
    # if issubclass(rpt, AbstractTable):
    if not issubclass(rpt, AbstractTable):
        return refto(rpt)
    if not rpt.is_abstract():
        s += rubric(_("Columns"))
        s += rstgen.ul([elem2par(f) for f in rpt.wildcard_data_elems()])
    if rpt.detail_action:
        s += rubric(_("Detail fields"))
        s += rstgen.ul([elem2par(f) for f in rpt.get_detail_elems()])
    s += rubric(_("Actions"))
    s += rstgen.ul([action2par(a) for a in rpt._actions_list])
    if rpt.parameters:
        s += rubric(_("Filter parameters"))
        s += rstgen.ul([elem2par(f) for f in rpt.parameters.values()])
    return s


def rptlist(l):
    return ', '.join([report_ref(rpt) for rpt in sorted(l, key=str)])
        # ":doc:`%s (%s) <%s>`" % (str(rpt),
        #                          force_str(rpt.label), report_ref(rpt))
        # for rpt in l])


def model_referenced_from(model):
    #~ headers = ["name","description"]
    #~ rows = []
    def ddhfmt(ddh):
        return ', '.join(['{}.{}'.format(full_model_name(model), fk.name)
                          for model, fk in ddh.fklist])
    return ddhfmt(model._lino_ddh)
    #~ rows.append(['_lino_ddh',ddhfmt(model._lino_ddh)])
    #~ return rstgen.table(headers,rows)


class GeneratingCommand(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tmpdir', action='store',
                            dest='tmpdir', default=None,
                            help='Path for temporary files.')

    def handle(self, *args, **options):

        self.options = options
        parts = ('cache', 'help')
        self.output_dir = join(settings.MEDIA_ROOT, *parts)
        self.generated_count = 0

        tmpdir = options['tmpdir']
        if tmpdir:
            self.run_on_temp_dir(tmpdir)
        else:
            with tempfile.TemporaryDirectory() as tmpdirname:
                self.run_on_temp_dir(tmpdirname)

    def run_on_temp_dir(self, temp_dir):
        verbosity = self.options.get('verbosity', 0)
        self.temp_dir = temp_dir
        logger.info("Generate temporary rst files to %s", self.temp_dir)

        self.generate_files()
        logger.info("Generated %s files to %s", self.generated_count, self.temp_dir)
        logger.info("Building site help html to %s", self.output_dir)
        for lng in settings.SITE.languages:
            self.language = lng
            docs_dir = self.docspath()
            builder = 'html'
            if use_dirhtml:
                builder = 'dirhtml'
            args = ['sphinx-build', '-b', builder]
            args += ['-T'] # show full traceback on exception
            # ~ args += ['-a'] # all files, not only outdated
            # ~ args += ['-P'] # no postmortem
            if not verbosity:
                args += ['-Q'] # no output
            args += ['.']
            if lng.index == 0:
                args += [self.output_dir]
            else:
                args += [join(self.output_dir, lng.django_code)]
            cmd = ' '.join(args)
            print("Run `cd {} && {}`".format(docs_dir, cmd))
            with cd(docs_dir):
                runcmd(cmd)



    def docspath(self, output_file=None):
        parts = [self.temp_dir]
        if self.language.index == 0:
            parts.append('docs')
        else:
            parts.append(self.language.django_code + 'docs')
        if output_file:
            parts.append(output_file)
        return os.path.join(*parts)

    def generate(self, tplname, output_file, **context):
        output_file = self.docspath(output_file)
        logger.info("Generating %s", output_file)
        #~ logger.info("Generating %s from %s",fn,tpl_filename)
        env = settings.SITE.plugins.jinja.renderer.jinja_env
        template = env.get_template(tplname)
        context.update(self.context)
        content = template.render(**context)

        # def app_labels():
        #     return [p.app_label for p in settings.SITE.installed_plugins]
        # self.context.update(
        #     lino=lino,
        #     #~ models=models,
        #     settings=settings,
        #     app_labels=app_labels)
        #~ d = dict(site=site)
        #~ print 20110223, [m for m in models.get_models()]
        #~ print 20110315, context
        #~ print s
        open(output_file, 'wt').write(content)
        self.generated_count += 1
        return ''


class Command(GeneratingCommand):
    help = "Generate the html help pages for this Lino site."

    def generate_files(self):

        self.context = dict(
            header=rstgen.header,
            h1=curry(rstgen.header, 1),
            table=rstgen.table,
            doc2rst=doc2rst,
            models=models,
            abstract=abstract,
            refto=refto,
            settings=settings,
            actors=actors,
            doctest=doctest,
            translation=translation,
            use_dirhtml=use_dirhtml,
            #~ py2rst=rstgen.py2rst,
            languages=[lng.django_code for lng in settings.SITE.languages],
            get_models=apps.get_models,
            full_model_name=full_model_name,
            model_overview=model_overview,
            actor_overview=actor_overview,
            model_referenced_from=model_referenced_from,
            model_ref=model_ref,
            makedocs=self,
        )
        self.context['_'] = _
        for lng in settings.SITE.languages:
            self.language = lng
            os.makedirs(self.docspath(), exist_ok=True)
            self.generate('makedocs/index.tpl.rst', 'index.rst')
            self.generate('makedocs/conf.tpl.py', 'conf.py')
