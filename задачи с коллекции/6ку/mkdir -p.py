import os


def mkdirp(*directories):
    if not os.path.isdir('/'.join(directories).replace('//', '/')):
        os.makedirs('/'.join(directories).replace('//', '/'))
