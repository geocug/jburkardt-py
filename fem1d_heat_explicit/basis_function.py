#! /usr/bin/env python

def basis_function ( index, element, node_x, point_x ):

#*****************************************************************************80
#
## BASIS_FUNCTION evaluates a basis function.
#
#  Discussion:
#
#    Piecewise linear basis functions are used.
#
#    Basis functions are associated with NODES, and are numbered 1 to NODE_NUM.
#
#    Elements are associated with intervals, having nodes as endpoints.
#    Element I begins at node I and ends at node I+1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer INDEX, the index of the basis function to be evaluated.
#
#    Input, integer ELEMENT, the index of the element in which the points lie.
#
#    Input, real NODE_X(NODE_NUM), the coordinates of nodes.
#
#    Input, integer POINT_NUM, the number of evaluation points.
#
#    Input, real POINT_X, the evaluation points.
#
#    Output, real B, DBDX, the basis function and its derivative, evaluated
#    at the evaluation points.
#
  import numpy as np

  b    = 0.0
  dbdx = 0.0

  if ( index == element ):
    b    = ( node_x[element+1] - point_x ) / ( node_x[element+1] - node_x[element] )
    dbdx =                     - 1.0       / ( node_x[element+1] - node_x[element] )
  elif ( index == element + 1 ):
    b    = ( point_x - node_x[element] )   / ( node_x[element+1] - node_x[element] )
    dbdx = + 1.0                           / ( node_x[element+1] - node_x[element] )

  return b, dbdx

