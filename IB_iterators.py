import random

# Task 1

def gen_fa(path):
    file = open(path)
    lines = file.readlines()
    print(lines)
    file.close()
    i = 0
    while i < len(lines)-1:
        yield lines[i].strip('\n') + ' ' + lines[i+1].strip('\n')
        i = i + 2


print(gen_fa('ex.fasta'))
for item in gen_fa('ex.fasta'):
    print(item)


# Task 2

class Evolution:


    def __init__(self, path):
        self.path = path
        file = open(self.path)
        self.lines = file.readlines()
        file.close()
        self.seqs = []
        while True:
            for item in self.iter_gen():
                self.seqs.append(item)
            print(*self.seqs)
    

    def deletion(self, it, ind):
        it = it.replace(it[ind], "")
        return it
    

    def insertion(self, it, ind):
        it_list = it.split()
        insert = random.choice(it_list)
        it = it[:ind] + insert + it[ind:]
        return it
    

    def replacement(self, it, ind):
        it_list = it.split()
        repl = random.choice(it_list)
        it = it.replace(it[ind], repl)
        return it


    def mutate(self, it):
        ind = random.randint(0, len(it)-1)
        fun_list = ['self.deletion(it, ind)', 'self.insertion(it, ind)', 'self.replacement(it, ind)']
        func = random.choice(fun_list)
        return eval(func)
    

    def iter_gen(self):
        i = 1
        while i <= len(self.lines)-1:
            #print(i)
            #print(self.lines[i])
            #print('mutated')
            #print(self.mutate(self.lines[i]))
            yield self.mutate(self.lines[i])
            i = i + 2
            #if i > len(self.lines)-1:
                #i = 1


obj = Evolution('ex.fasta')
print('print')
print(*obj.seqs)
