import datetime
import genetic
import random
import unittest

def display(candidate, start_time):
    time_diff = datetime.datetime.now() - start_time
    print('{0}\t{1}\t{2}'.format(
        ''.join(candidate.Genes), candidate.fitness, str(time_diff)))

class GuessPasswordTests(unittest.TestCase):
    gene_set = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.?!'
    
    def get_fitness(self, genes, target):
        return sum(1 for expected, actual in zip(target, genes)
                   if expected == actual)

    def guess_password(self, target):
        start_time = datetime.datetime.now()

        def fn_get_fitness(self, genes):
            return self.get_fitness(genes, target)

        def fn_display(self, genes):
            display(candidate, start_time)

            optimal_fitness = len(target)
            best = genetic.get_best(fn_get_fitness,
                                    len(target),
                                    optimal_fitness,
                                    self.gene_set,
                                    fn_display)
            self.assertEqual(''.join(best.Genes), target)

    def test_Hello_World(self):
        target = 'Hello World!'
        self.guess_password(target)

    def test_long(self):
        target = 'For I am fearfully and wonderfully made, bitches.'
        self.guess_password(target)

    def test_random(self):
        length = 150
        target = ''.join(random.choice(self.gene_set) for _ in range(length))
        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_random)

if __name__ == '__main__':
    unittest.main()

