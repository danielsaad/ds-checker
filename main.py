#!/usr/bin/python3

import compiler
import runner
import checker
import argparse
import os
import factory
import datetime


def parse(args):
    assert(os.path.isfile(args.file))
    assert(os.path.isdir(args.input_folder))
    assert(os.path.isdir(args.answer_folder))
    assert(os.path.isfile(args.checker))
    p = factory.create_checker(args.file)
    p.set_directory(args.directory)
    p.set_stop_policy(args.stop)
    p.set_timelimit(args.timelimit)
    p.set_input_folder(args.input_folder)
    folder_name = 'submission_' + datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    p.set_output_folder(os.path.join(p.directory, folder_name))
    p.set_answer_folder(args.answer_folder)
    p.set_checker_runable(args.checker)

    return p


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--timelimit', dest='timelimit', action='store', type=int,
                        default=0, help='apply action on all problems')
    parser.add_argument('-n', '--non-stop', dest='stop', action='store_true',
                        default=True, help='set checker to stop when WA occrus')
    parser.add_argument('-d', '--directory', action='store', dest='directory', type=str,
                        default='/tmp', help='Directory where the submission will be processed.')

    parser.add_argument('-v', '--verbose', dest='verbose',
                        action='store_true', default=False, help='Verbose mode.')

    parser.add_argument('file', type=str,
                        help='the file to be processed')
    parser.add_argument('input_folder', type=str,
                        help='Input folder containing the test cases')
    parser.add_argument('answer_folder', type=str,
                        help='Answer folder containing the answers to the input test cases.')
    parser.add_argument('checker', type=str, help='Runnable checker to ')
    args = parser.parse_args()
    p = parse(args)
    print('File =', args.file)
    print(args.directory)
    c = p.compiler(args.file, args.directory)
    c.compile()
    r = p.runner(c.runnable_file, p.input_folder, p.output_folder, p.timelimit)
    r.run()
    c = p.checker(p.checker_runnable, p.input_folder,
                  p.output_folder, p.answer_folder, p.stop)
    c.check(args.verbose)
