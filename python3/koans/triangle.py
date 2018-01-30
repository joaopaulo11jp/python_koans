#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if (not isTriangle(a,b,c)):
        raise TriangleError('Invalid triangle!')

    return {1:'equilateral', 2:'isosceles', 3:'scalene'}[len(set([a,b,c]))]

    #Less efficient alternative...
    #distincSides = len(set([a,b,c]))

    #if distincSides == 1:
    #    return 'equilateral'
    #elif distincSides == 2:
    #    return 'isosceles'
    #elif distincSides == 3:
    #    return 'scalene'

def isTriangle(a,b,c):
    return (a + b > c) and (a + c > b) and (b + c > a)

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
