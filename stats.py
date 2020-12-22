from random import randint


class die:
    def __init__(self, sides):
        self._sides = sides
        self._number = 1  # is equivalent to the side the

    def roll(self):
        self._number = randint(1, self._sides)

    def side(self):
        return self._number


def prob_thread_locking_on_batch(batch_number, threads):
    print("calculating probability for batch number", batch_number, "and", threads, "threads")
    count = 0
    tests = 10000000  # changed from 60000000 to current because previous was too slow
    # increase if you need a bit more accuracy on lower thread amoounts.
    for i in range(tests):
        dice = []
        ones = 0
        for j in range(threads):
            dice.append(die(batch_number))
            dice[j].roll()
            if (dice[j].side() == 1):
                ones += 1
            if (ones == 2):
                count += 1
                break
    return count / float(tests)


if __name__ == "__main__":
    from sys import argv

    batch_number = int(argv[1])
    threads = int(argv[2])
    answer = prob_thread_locking_on_batch(batch_number, threads)
    print(answer)

# want to make a table, a graph and store the data in a file.
# from batch 50 to 150
# threads 2 to 16
# runtime at current tests is about 3 hours
# at previous tests was 20 hours
