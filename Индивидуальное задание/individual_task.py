#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    x3 = int(input("x3 = "))
    y3 = int(input("y3 = "))

    A = (((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))**0.5
    B = (((x1-x3)*(x1-x3))+((y1-y3)*(y1-y3)))**0.5
    C = (((x2-x3)*(x2-x3))+((y2-y3)*(y2-y3)))**0.5

    P = A + B + C
    p1 = P/2
    S = (p1 * (p1 - A) * (p1 - B) * (p1 - C)) ** 0.5

    print("\nПериметр P = ", '%.2f' % P, "см2\nПлощадь S = ", '%.2f' % S, "см2")
