
""" Global definitions """

""" C definitions """
C_COMPILER = ['gcc']
C_FLAGS = ['-O2','-DNDEBUG']
C_LFLAGS = ['-lm']

""" CPP definitions """
CPP_COMPILER = ['g++']
CPP_FLAGS = ['-O2','-DNDEBUG','-std=c++11']
CPP_LFLAGS = ['-lm']

""" Java definitions """
JAVA_COMPILER = ['javac']
JAVA_INTERPRETER = ['java']

""" Python2 definitions """
PYTHON2_INTERPRETER = ['python2']

""" Python3 definitions """
PYTHON3_INTERPRETER = ['python3']

'''
    Sort by string size, then lexicographical order.
'''
def custom_key(str):
    return +len(str), str.lower()