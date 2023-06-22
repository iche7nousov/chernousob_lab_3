#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

if __name__ == "__main__":
    x = random.random()
    y = random.random()
    z = random.random()

    for i in x, y, z:
        if i >= 0 and i <=1:
            print(i)
