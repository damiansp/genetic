import datetime
import random

gene_set = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.?!'
target = 'Hello World!'

def generate_parent(length):
    genes = []

    while len(genes) < length:
        sample_size = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, sample_size))

    return ''.join(genes)

def get_fitness(guess):
    return sum(
        1 for expected, actual in zip(target, guess) if expected == actual)

def mutate(parent):
    index = random.randrange(0, len(parent))
    child_genes = list(parent)
    new_gene, alternate = random.sample(gene_set, 2)
    child_genes[index] = (alternate if new_gene == child_genes[index]
                          else new_gene)
    return ''.join(child_genes)

def display(guess):
    time_diff = datetime.datetime.now() - start_time
    fitness = get_fitness(guess)
    print('{0}\t{1}\t{2}'.format(guess, fitness, str(time_diff)))

random.seed()
start_time = datetime.datetime.now()
best_parent = generate_parent(len(target))
best_fitness = get_fitness(best_parent)
display(best_parent)

while True:
    child = mutate(best_parent)
    child_fitness = get_fitness(child)

    if best_fitness >= child_fitness:
        continue

    display(child)

    if child_fitness >= len(best_parent):
        break

    best_fitness = child_fitness
    best_parent = child
