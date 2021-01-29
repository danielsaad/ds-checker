import subprocess
import sys
import shutil
import os
from definitions import C_COMPILER,C_FLAGS,C_LFLAGS,CPP_COMPILER,CPP_FLAGS,CPP_LFLAGS,JAVA_COMPILER


class compiler():
    def __init__(self, src, runnable_directory):
        self.src = src
        self.runnable_directory = runnable_directory
        assert(os.path.isfile(src))
        os.makedirs(os.path.dirname(runnable_directory), exist_ok=True)
        self.runnable_file = compile()

    def compile(self):
        return ''


class c_compiler(compiler):
    def __init__(self, src, runnable_file):
        super.__init__(src, runnable_file)

    def compile(self):
        command = C_COMPILER + C_FLAGS + [self.src] + ['-o', os.path.join(self.runnable_directory, os.path.splitext(self.src)[0])] + C_LFLAGS
        print('Compiling: ', ' '.join(command))
        p= subprocess.run(command)
        if(p.returncode):
            print('CE: C Compilation of', self.src, 'Failed')
            sys.exit(1)
        else:
            print(os.path.splitext(os.path.basename(self.src))[0], 'generated')

class cpp_compiler(compiler):
    def __init__(self, src, runnable_file):
        super.__init__(src, runnable_file)

    def compile(self):
        command = CPP_COMPILER + CPP_FLAGS + [self.src] + ['-o', os.path.join(self.runnable_directory, os.path.splitext(self.src)[0])] + CPP_LFLAGS
        print('Compiling: ', ' '.join(command))
        p= subprocess.run(command)
        if(p.returncode):
            print('CE: C Compilation of', self.src, 'Failed')
            sys.exit(1)
        else:
            print(os.path.splitext(os.path.basename(self.src))[0], 'generated')

        return os.path.join(os.path.join(self.runnable_directory,os.path.splitext(os.path.basename(self.src))[0]))

class java_compiler(compiler):
    def __init__(self, src, runnable_file):
        super.__init__(src, runnable_file)

    def compile(self):
        command= JAVA_COMPILER + ['-d', self.runnable_directory] + [self.src]
        print('Compiling: ', ' '.join(command))
        p= subprocess.run(command)
        if(p.returncode):
            print('CE: Java Compilation of', self.src, 'Failed')
            sys.exit(1)
        else:
            print(self.src + '.class', 'generated')

        return os.path.join(os.path.join(self.runnable_directory,os.path.splitext(os.path.basename(self.src))[0]))

class python_compiler(compiler):
    def __init__(self, src, runnable_file=' '):
        super.__init__(src, runnable_file)

    def compile(self):
        shutil.copy(self.src,os.path.join(self.runnable_directory,os.path.basename(self.src)))
        return os.path.join(os.path.join(self.runnable_directory,os.path.basename(self.src)))

class foo_compiler(compiler):
    def __init__(self, src, runnable_file=' '):
        super.__init__(src, runnable_file)

    def compile(self):
        shutil.copy(self.src,os.path.join(self.runnable_directory,os.path.basename(self.src)))
        return os.path.join(os.path.join(self.runnable_directory,os.path.basename(self.src)))
