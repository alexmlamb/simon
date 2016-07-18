
import sys

import subprocess
import os

import datetime

import random

class simon(object):
    def __init__(self, folder, name = "nameless"):

        self.terminal = sys.stdout

        if folder[-1] != "/":
            folder = folder + "/"

        exp_path_name = folder + name + "_" + datetime.datetime.now().strftime("%Y%m%d_%Hh%Mm%Ss") + "/"

        if os.path.exists(exp_path_name):
            self.experiment_dir = folder + name + "_" + datetime.datetime.now().strftime("%Y%m%d_%Hh%Mm%Ss") + "_" + str(random.randint(0,1000)) + "/"
        else:
            self.experiment_dir = exp_path_name

        os.mkdir(self.experiment_dir)

        self.filename = self.experiment_dir + "log.txt"

        self.logobj = open(self.filename, "w")

        sys.stdout = self

        try:

            gitstr = subprocess.check_output(['git', 'rev-parse', 'HEAD'], stderr=open(os.devnull, 'w')).strip("\n")
    
            str_short = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], stderr=open(os.devnull, 'w')).strip("\n")

            url = subprocess.check_output(['git','config', '--get', 'remote.origin.url'], stderr=open(os.devnull,'w')).strip("\n")

            using_git = True

            url_commit =  url.rstrip("git").rstrip(".")

            full_url = url_commit + "/commit/" + str_short

        except:
            pass

        print "[logging info]"
        print "\tExperiment Directory", os.path.abspath(self.experiment_dir)
        print "\tLog Location", "less " + os.path.abspath(self.experiment_dir) + "/log.txt"

        if using_git:
            print "[git info]"
            print "\tcommit", gitstr
            print "\tshort commit", str_short
            print "\tpackage link", url
            print "\tcommit link", full_url

    def write(self, message):
        self.terminal.write(message)
        self.logobj.write(message)
        self.flush()

    def flush(self):
        self.terminal.flush()
        self.logobj.flush()

    def log(self, message):
        self.logobj.write(message)



