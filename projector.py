#! /usr/bin/env python

# Projector: Very Simple Project Management

import os
import sys

WORKSPACE="~/Important/"

INITIAL_GIT_FLAGS="-S -m 'Initial idea'"

EXECUTABLE_LOCATION="~/bin/"

def createProject(name):
    "Make a project with the specified name"
    os.system("mkdir " + WORKSPACE + name + ";" +
                     "cd " + WORKSPACE + name + ";" +
                     "editor idea.txt" + ";" +
                     "git init" + ";" +
                     "git add idea.txt" + ";" +
                     "git commit " + INITIAL_GIT_FLAGS + ";")

def linkProject(project, exe):
    "Link an executable into the executables dir."
    os.system("ln " + WORKSPACE + project + "/" + exe + " " + EXECUTABLE_LOCATION + exe)


if __name__ == "__main__":
    args = sys.argv[1:]
#    print args
#    sys.exit(0)
    while args != []:
        if args[0] == "-w":
            WORKSPACE=args[1]
            args = args[2:]
        elif args[0] == "-e":
            EXECUTABLE_LOCATION=args[1]
            args = args[2:]
        elif args[0] == "link":
            projectName = args[1]
            exeName = args[2]
            linkProject(projectName, exeName)
            args = args[3:]
        elif args[0] == "help" or args[0] == "--help" or args[0] == "-h":
            print "Projector: Simple Project Management"
            print "-h : help"
            print "-w : Set workspace"
            print "-e : Set executable location"
            print ""
            print "create (default) : Create a new project"
            print "link             : Link an executable from a project"
            print ""
            print "Projector - Accept no Substitutes"
            args = args[1:]
        elif args[0] == "create":
            createProject(args[1])
            args = args[2:]
        else:
            createProject(args[0])
            args = args[1:]
