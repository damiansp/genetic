import datetime
import genetic

def guess_password(target):
    gene_set = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.?!'
    start_time = datetime.datetime.now()

    def fn_get_fitness(genes):
        return get_fitness(genes, target)

    def fn_display(genes):
        display(genes, target, start_time)

    optimal_fitness = len(target)
    genetic.get_best(
        fn_get_fitness, len(target), optimal_fitness, gene_set, fn_display)

def test_Hello_World():
    target = 'Hello World!'
    guess_password(target)
