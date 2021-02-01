import os
import compiler
import checker
import runner


class pipeline:
    def __init__(self, compiler, runner, checker):
        self.compiler = compiler
        self.runner = runner
        self.checker = checker

    def set_timelimit(self, timelimit):
        self.timelimit = timelimit

    def set_directory(self, directory):
        self.directory = directory

    def set_stop_policy(self,stop):
        self.stop = stop

    def set_input_folder(self,input_folder):
        self.input_folder = input_folder
    
    def set_output_folder(self,output_folder):
        self.output_folder = output_folder

    def set_answer_folder(self,answer_folder):
        self.answer_folder = answer_folder

    def set_checker_runable(self,checker_runnable):
        self.checker_runnable = checker_runnable

def create_checker(file):
    ext = os.path.splitext(file)[1]
    if(ext == '.c'):
        return pipeline(compiler.c_compiler, runner.binary_runner, checker.checker)
    if(ext == '.cpp' or ext == '.cc' or ext == '.C'):
        return pipeline(compiler.cpp_compiler, runner.binary_runner, checker.checker)
    if(ext == '.java'):
        return pipeline(compiler.java_compiler, runner.java_runner, checker.checker)
    if(ext == '.py2'):
        return pipeline(compiler.python_compiler, runner.python2_runner, checker.checker)
    if(ext == '.py3' or ext == '.py'):
        return pipeline(compiler.python_compiler, runner.python_runner, checker.checker)
    return pipeline(compiler.foo_compiler, runner.binary_runner, checker.checker)
