import unittest
import random
import os
from shutil import rmtree
import pkgutil
from subprocess import Popen, DEVNULL

# random.seed(1) # To make results reproducible
modules = [i.name for i in pkgutil.iter_modules() if not i.name.startswith('_')]
totest  = random.sample(modules, 10)

class TestSimilarity(unittest.TestCase):
    def test_all(self):
        for module in totest:
            print(f'Now testing: {module}')
            self.basic(module)
            self.full(module)

    def basic(self, module):
        p = Popen(['doc2md', module], stdout=DEVNULL)
        p.communicate()

    def full(self, module):
        p = Popen(['doc2md', module, '-d', '3', '-o', 'TEMP', '--level', '2', '--mode', 'allfull'], stdout=DEVNULL)
        p.communicate()
        if os.path.exists('TEMP'):
            rmtree('TEMP')

    @classmethod
    def tearDownClass(self):
        if os.path.exists('TEMP'):
            rmtree('TEMP')
