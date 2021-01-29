import os
import subprocess
from definitions import JAVA_INTERPRETER,PYTHON2_INTERPRETER,PYTHON3_INTERPRETER,custom_key
import time


class runner:
    def __init__(self, runnable_file='', inf_folder='', ouf_folder='', timelimit=0):
        self.runnable_file = runnable_file
        self.inf_folder = inf_folder
        self.ouf_folder = ouf_folder
        self.timelimit = timelimit

    def run_helper(self,fname_in,fname_out):
        return 0

    def run(self):
        # def inf files
        input_files = [os.path.join(self.inf_folder, f) for f in os.listdir(
            self.inf_folder) if os.path.isfile(os.path.join(self.inf_folder, f))]
        # create ouf folder
        os.makedirs(self.ouf_folder, exist_ok=True)
        input_files.sort(key=custom_key)
        
        succ = 0
        total = 0
        
        for fname_in in input_files:
            fname_out = os.path.join(
                self.ouf_folder, os.path.basename(fname_in))
            print('Running test', os.path.basename(fname_in))
            local_time_start = time.perf_counter()
            rv = self.run_helper(fname_in,fname_out)
            local_time_end = time.perf_counter()
            if(rv == 0):
                print('Time elapsed: {0:.2f}'.format(
                    local_time_end-local_time_start), 'seconds')
                succ = succ + 1
            if(rv == 1):
                print('RE: Runtime error')
            if (rv == 2):
                print('TLE: Time Limit Exceeded')
            total = total + 1
        
        print('Successfuly ran',succ,'of',total,'tests')

class binary_runner(runner):
    def __init__(self, runnable_file='', inf_folder='', ouf_folder='', timelimit=0):
        super().__init__(runnable_file,inf_folder,ouf_folder,timelimit)

    def run_helper(self,fname_in,fname_out):
        with open(fname_in,'r') as inf, open(fname_out,'w') as ouf:
            t = None if self.timelimit == 0 else self.timelimit
            try:
                p = subprocess.run(self.runnable_file,stdin=inf,stdout=ouf,timeout=t)
            except subprocess.TimeoutExpired:
                return 2
            if(p.returncode):
                return 1
            return 0

class java_runner(runner):
    def __init__(self, runnable_file='', inf_folder='', ouf_folder='', timelimit=0):
        super().__init__(runnable_file,inf_folder,ouf_folder,timelimit)

    def run_helper(self,fname_in,fname_out):
        with open(fname_in,'r') as inf, open(fname_out,'w') as ouf:
            t = None if self.timelimit == 0 else self.timelimit
            try:
                command = JAVA_INTERPRETER + ['-classpath',
                    os.path.dirname(self.runnable_file)] + [os.path.basename(self.runnable_file)]
                p = subprocess.run(command, stdin=inf, stdout=ouf,timeout=t)
            except subprocess.TimeoutExpired:
                return 2
            if(p.returncode):
                return 1
            return 0


class python_runner(runner):
    def __init__(self, runnable_file='', inf_folder='', ouf_folder='', timelimit=0):
        super().__init__(runnable_file,inf_folder,ouf_folder,timelimit)

    def run_helper(self,fname_in,fname_out):
        with open(fname_in,'r') as inf, open(fname_out,'w') as ouf:
            t = None if self.timelimit == 0 else self.timelimit
            try:
                command = PYTHON3_INTERPRETER + [self.runnable_file]
                p = subprocess.run(command, stdin=inf, stdout=ouf,timeout=t)
            except subprocess.TimeoutExpired:
                return 2
            if(p.returncode):
                return 1
            return 0

class python2_runner(runner):
    def __init__(self, runnable_file='', inf_folder='', ouf_folder='', timelimit=0):
        super().__init__(runnable_file,inf_folder,ouf_folder,timelimit)

    def run_helper(self,fname_in,fname_out):
        with open(fname_in,'r') as inf, open(fname_out,'w') as ouf:
            t = None if self.timelimit == 0 else self.timelimit
            try:
                command = PYTHON2_INTERPRETER + [self.runnable_file]
                p = subprocess.run(command, stdin=inf, stdout=ouf,timeout=t)
            except subprocess.TimeoutExpired:
                return 2
            if(p.returncode):
                return 1
            return 0
