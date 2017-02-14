import random

gene_set = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.?!'
target = 'Hello World!'

def generate_parent(length):
    genes = []

    while len(genes) < length:
        sample_size = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, sample_size))

    return ''.join(genes)
