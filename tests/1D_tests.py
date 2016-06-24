#!/usr/bin/env python
from effective_quadratures.PolyParams import PolynomialParam
from effective_quadratures.PolyParentFile import PolyParent
from effective_quadratures.IndexSets import IndexSet
import effective_quadratures.MatrixRoutines as matrix
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
import numpy.ma as maogle
import os
"""

    Testing Script for Effective Quadrature Suite of Tools

    Pranay Seshadri
    ps583@cam.ac.uk

    Copyright (c) 2016 by Pranay Seshadri
"""
# Simple analytical function
def fun(x):
    return x[:]

def main():

    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                    INPUT SECTION
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    order = 6
    derivative_flag = 0 # derivative flag
    error_flag = 0

    # Min and max values. Not used for a "Gaussian" or "Normal" distribution
    min_value = -3.0
    max_value = 2.0

    # For a "Beta" uncertainty, these become alpha and beta shape parameters
    # in which case both have to be greater than 1.0
    # For a "Normal" or "Gaussian" uncertainty these become the mean and variance
    parameter_A = 0
    parameter_B = 1

    # Method for computing coefficients. Right now functionality is limited to
    # tensor grids. to do: THIS NEEDS TO BE CODED
    method = "tensor grid"
    level = 2
    growth_rule = "exponential"
    # Write out the properties for each "uq_parameter". You can have as many
    # as you like!
    uq_parameters = []
    uq_parameter = PolynomialParam("Beta", min_value, max_value, parameter_A, parameter_B, derivative_flag, order)
    uq_parameters.append(uq_parameter)

    print '****************************************************************'
    print '                     EFFECTIVE-QUADRATURES                      '
    print '\n'
    for i in range(0,len(uq_parameters)):
        print str('Uncertainty Parameter %i : '%(i+1)) + str(uq_parameters[i].param_type)
        if(uq_parameters[i].param_type == "Gaussian" or uq_parameters[i].param_type == "Normal"):
            print str('With mean & variance:')+'\t'+('[')+str(uq_parameters[i].shape_parameter_A)+str(',')+str(uq_parameters[i].shape_parameter_B)+str(']')
        elif(uq_parameters[i].param_type == "Beta" ):
            print str('With shape parameters:')+'\t'+('[')+str(uq_parameters[i].shape_parameter_A)+str(',')+str(uq_parameters[i].shape_parameter_A)+str(']')
        elif(uq_parameters[i].param_type == "Beta" or uq_parameters[i].param_type == "Uniform"):
            print str('With support:')+'\t'+('[')+str(uq_parameters[i].lower_bound)+str(',')+str(uq_parameters[i].upper_bound)+str(']')
            print str('Order:')+'\t'+str(uq_parameters[i].order)+'\n'
    print '****************************************************************'

    # Create a PolyParent object!
    uq_structure = PolyParent(uq_parameters, method)
    #uq_structure = PolyParent(uq_parameters, "tensor grid")


    pts, wts = PolyParent.getPointsAndWeights(uq_structure,)

    print '--Quadrature Points--'
    print pts
    print '\n'
    print '--Weights--'
    print wts
    print '\n'

    # For coefficients!
    X , F = PolyParent.getCoefficients(uq_structure, fun)
    print '---Pseudospectral coefficients---'
    print X
    print '\n'
    print 'Mean: '+str(X[0,0])
    print 'Variance: '+str(np.sum(X[0,1:]**2))
    print T

    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                    PLOTTING SECTION
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    # Plot all the univariate polynomials:
    #M = PolyParent.getMultivariatePoly(uq_structure, pts_for_plotting)
    #color=iter(cm.rainbow(np.linspace(0,1,order)))

    #for i in range(0, order):
    #    c = next(color)
    #    plt.plot(pts_for_plotting, M[i,:], '-', c=c)
    #plt.xlabel('x')
    #plt.ylabel('p(x)')
    #plt.title('Orthogonal polynomials')
    #plt.show()

main()