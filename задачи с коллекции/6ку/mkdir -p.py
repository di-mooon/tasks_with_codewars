import os


def mkdirp(*directories):
    if not os.path.isdir(os.path.join(*directories)):
        os.makedirs(os.path.join(*directories))
