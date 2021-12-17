import subprocess
import sys
import shutil
import os
from definitions import (
    C_COMPILER,
    C_FLAGS,
    C_LFLAGS,
    CPP_COMPILER,
    CPP_FLAGS,
    CPP_LFLAGS,
    JAVA_COMPILER,
)


class compiler:
    def __init__(self, src, runnable_directory):
        self.src = src
        self.runnable_directory = runnable_directory
        assert os.path.isfile(src)
        os.makedirs(runnable_directory, exist_ok=True)

    def compile(self):
        pass


class c_compiler(compiler):
    def __init__(self, src, runnable_directory):
        super().__init__(src, runnable_directory)

    def compile(self):
        command = (
            C_COMPILER
            + C_FLAGS
            + [self.src]
            + [
                "-o",
                os.path.join(
                    self.runnable_directory,
                    os.path.splitext(os.path.basename(self.src))[0],
                ),
            ]
            + C_LFLAGS
        )
        print("Compiling: ", " ".join(command))
        p = subprocess.run(command)
        if p.returncode:
            print("CE: C Compilation of", self.src, "Failed")
            sys.exit(1)
        else:
            print(os.path.splitext(os.path.basename(self.src))[0], "generated")
        self.runnable_file = os.path.join(
            self.runnable_directory, os.path.splitext(
                os.path.basename(self.src))[0]
        )


class cpp_compiler(compiler):
    def __init__(self, src, runnable_directory):
        super().__init__(src, runnable_directory)

    def compile(self):
        command = (
            CPP_COMPILER
            + CPP_FLAGS
            + [self.src]
            + [
                "-o",
                os.path.join(
                    self.runnable_directory,
                    os.path.splitext(os.path.basename(self.src))[0],
                ),
            ]
            + CPP_LFLAGS
        )
        print("Compiling: ", " ".join(command))
        p = subprocess.run(command)
        if p.returncode:
            print("CE: C Compilation of", self.src, "Failed")
            sys.exit(1)
        else:
            print(os.path.splitext(os.path.basename(self.src))[0], "generated")

        self.runnable_file = os.path.join(
            self.runnable_directory, os.path.splitext(
                os.path.basename(self.src))[0]
        )


class java_compiler(compiler):
    def __init__(self, src, runnable_directory):
        super().__init__(src, runnable_directory)

    def compile(self):
        command = JAVA_COMPILER + ["-d", self.runnable_directory] + [self.src]
        print("Compiling: ", " ".join(command))
        p = subprocess.run(command)
        if p.returncode:
            print("CE: Java Compilation of", self.src, "Failed")
            sys.exit(1)
        else:
            print(self.src + ".class", "generated")

        self.runnable_file = os.path.join(
            os.path.join(
                self.runnable_directory, os.path.splitext(
                    os.path.basename(self.src))[0]
            )
        )


class python_compiler(compiler):
    def __init__(self, src, runnable_directory=" "):
        super().__init__(src, runnable_directory)

    def compile(self):
        shutil.copy(
            self.src, os.path.join(
                self.runnable_directory, os.path.basename(self.src))
        )
        self.runnable_file = os.path.join(
            os.path.join(self.runnable_directory, os.path.basename(self.src))
        )


class foo_compiler(compiler):
    def __init__(self, src, runnable_directory):
        super().__init__(src, runnable_directory)

    def compile(self):
        src_newpath = os.path.join(
            self.runnable_directory, os.path.basename(self.src))

        if os.path.abspath(self.src) != os.path.abspath(src_newpath):
            shutil.copy(
                self.src,
                src_newpath
            )

        self.runnable_file = src_newpath
