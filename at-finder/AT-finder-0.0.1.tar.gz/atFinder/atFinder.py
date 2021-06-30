import os
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import click

def gc_content(sequence):

    GC = sequence.count("C") + sequence.count("G") + sequence.count("c") + sequence.count("g")
    GC_content = (GC / len(sequence)) * 100

    return GC_content

def find_at_rich(sequence, cutoff = 0):

    regions = {} # Holds sequence of A/T rich regions with location as key

    # Walk through sequence finding substrings that match parameters of search
    start = 0
    end = 1
    while end <= len(sequence):

        # Store sequence once gc content threshold is reached
        if gc_content(sequence[start:end]) > cutoff:
            if len(sequence[start:(end-1)]) > 1:
                regions[(start+1, end)] = sequence[start:(end-1)]
                #regions.append(sequence[start:(end-1)])
            start = end # Update search parameter
            end += 1

        # Catch end sequences which match search parameters
        elif end == len(sequence):
            if gc_content(sequence[start:end]) <= cutoff:
                if len(sequence[start:end]) > 1:
                    #regions.append(sequence[start:end])
                    regions[(start+1, end+1)] = sequence[start:end]
                end += 1

        # Walk on if no catch
        else:
            end += 1

    return regions

@click.command()
@click.argument('file')
@click.option('-gc', '--gc_cutoff', type=float, default = 0, help='Cutoff for GC content of run, default = 0%')
@click.option('-l', '--min_length', type=int, default=2, help='Minimum length for A/T rich region, default = 2 bases.')
def cli(file, gc_cutoff=0, min_length=2):

    """Arguments:\n
    FILE The input file in genbank format (.gb).
    """

    record = SeqIO.read(file, 'genbank')
    sequence = str(record.seq)

    regions = find_at_rich(sequence, gc_cutoff)

    click.echo('A/T Rich Regions:')


    # Iterate through found A/T rich regions and add to genbank file depending on length cutoff
    count = 0
    for section in regions:
        if len(regions[section]) >= min_length:
            click.echo('Position: ' + str(section)) # Output A/T region to terminal
            click.echo(regions[section])
            count += 1
            feature = SeqFeature(FeatureLocation(section[0], section[1]), type = 'AT_rich_region')
            record.features.append(feature)
    click.echo('Found ' + str(count)  +  ' A/T rich regions.')

    new_file_information = record.format('genbank')

    # Form output file
    file_name = 'gc=' + str(gc_cutoff) + '_minlength=' + str(min_length) + '_' +  os.path.basename(file)
    base = os.getcwd()
    path = os.path.join(base, file_name)
    f = open(file_name, 'w')
    f.write(new_file_information)
    f.close()

    click.echo('New File Written: ' + path)


if __name__ == '__main__':
    cli()
