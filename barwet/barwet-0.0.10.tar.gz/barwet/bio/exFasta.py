def clean_seq(fasta_text: str) -> str:
    clear_seq = ''
    seqs = fasta_text.split('\n')
    for line in seqs:
        if line.strip():
            if line.startswith('>'):
                continue
            else:
                clear_seq += line.strip()
    return clear_seq