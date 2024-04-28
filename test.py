import importlib
import argparse
import tensorflow as tf
parser = argparse.ArgumentParser()
parser.add_argument('--model', default='pointnet2_cls_ssg', help='Model name [default: pointnet2_cls_ssg]')
FLAGS = parser.parse_args()
MODEL = importlib.import_module('..'+FLAGS.model,package="models.{}".format(FLAGS.model)) 
# mod1=importlib.import_module('..mod3',package="mod.mod3")
# mod1.mod1()