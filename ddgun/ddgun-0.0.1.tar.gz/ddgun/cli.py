# aaindexN vengono da https://www.genome.jp/ftp/db/community/aaindex/
from . import funcs_seq
#import funcs_3d
from .aa import Substitution
from . import ddgun
import click
import sys


@click.group()
def cli():
	pass


#def smart_open(path, mode):
#	import gzip
#	return (gzip.open if path.endswith('.gz') else open)(path, mode)

@cli.command()
@click.argument('sub')
@click.argument('profile', type=click.Path(exists=True, readable=True))
def predict(profile, sub):
	'''Predict DDG of SUB using PROFILE'''
	#click.echo(f"{aa_from}{aa_pos + 1}{aa_to}")
	if False: #debug
		import pandas
		m = ddgun.parse_aa_change(sub)
		p = pandas.read_csv(profile, sep='\s+', index_col=0)
		ddg = ddgun.ddgun_seq_old(p, m)
		click.echo(ddg)

	p = ddgun.Profile(profile)
	s = Substitution.parse(sub)
	ddg = ddgun.ddgun_seq(p, s)
	click.echo(ddg)


@cli.command()
@click.option('--output', type=click.Path(writable=True), help='output file, defaults to stdout')
@click.argument('msa', type=click.Path(exists=True, readable=True))
def mkprof(msa, output):
	'''Convert MSA into a profile table.

MSA multiple sequence alignments in psiblast format'''
	p = ddgun.Profile.from_msa(msa)
	if output is None:
		output = sys.stdout
	p.write(output)
