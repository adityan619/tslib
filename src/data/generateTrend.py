######################################################
#
# Generate Trend data
#
######################################################

import sys, os
sys.path.append("..")
sys.path.append(os.getcwd())

import numpy as np


def linearTrendFn(**kwargs):

    power = kwargs['power']
    displacement =kwargs['displacement']
    timeSteps = kwargs['timeSteps']
    steps = range(0, timeSteps)

    return np.power(steps, power) + displacement

def logTrendFn(**kwargs):
    dampening = kwargs['dampening']
    displacement = kwargs['displacement']
    timeSteps = kwargs['timeSteps']

    steps = range(1, timeSteps+1)
    return np.log(steps) + displacement

def negExpTrendFn(**kwargs):
    dampening = kwargs['dampening']
    displacement = kwargs['displacement']
    timeSteps = kwargs['timeSteps']
    steps = np.arange(0, -1*timeSteps, -1)
    steps = steps * dampening
    return np.exp(steps) + displacement


def generate(Fn, **kwargs):

    if (Fn is None):
        raise Exception('Fn needs to be a valid (vector) function.')

    return Fn(**kwargs)