#!/usr/bin/python3


import os
import subprocess
import sys
import time
import shutil
from definitions import custom_key


class checker:
    def __init__(self, checker_runnable, in_folder, out_folder, ans_folder, stop=False):
        self.checker_runnable = checker_runnable
        self.input_folder = in_folder
        self.output_folder = out_folder
        self.ans_folder = ans_folder
        self.nonstop = stop

    def check(self,verbose=False):
        input_files = [os.path.join(self.input_folder, f) for f in os.listdir(
            self.input_folder) if os.path.isfile(os.path.join(self.input_folder, f))]
        input_files.sort(key=custom_key)
        total = 0
        succ = 0
        for inf in input_files:
            total = total + 1
            fname = os.path.basename(inf)
            ouf = os.path.join(self.output_folder, fname)
            ans = os.path.join(self.ans_folder, fname)
            if(not os.path.isfile(ouf)):
                print('Output', fname, 'not available')
                if(self.nonstop):
                    continue
                sys.exit(1)
            if(not os.path.isfile(ans)):
                print('Answer', fname, 'not available')
                sys.exit(1)
            print('Checking input', fname)
            command = [self.checker_runnable, inf, ouf, ans]
            p = subprocess.run(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            checker_output = p.stderr.decode('utf-8',errors="backslashreplace")
            if(verbose):
                print(p.stderr.decode('utf-8',errors="backslashreplace"))
            if(checker_output.startswith('ok')):
                print('Input', fname, ': AC')
                succ = succ+1
            elif(checker_output.startswith('wrong answer')):
                print('Input', fname, ': WA')
                if(not self.nonstop):
                    sys.exit(0)
            elif(checker_output.startswith('wrong output format')):
                print('Input', fname, ': PE')
                if(not self.nonstop):
                    sys.exit(0)
            elif(checker_output.startswith('FAIL')):
                print('Input', fname,
                      ': FAIL: maybe the jury solution or the checker are not correct')
                if(self.nonstop):
                    sys.exit(0)
            else:
                print('Input', fname, ': Output not recognized -> ', checker_output)
                sys.exit(0)
        if(succ == total):
            print('OK: All tests passed!')
        else:
            print(succ, 'of', total, 'tests passed')
