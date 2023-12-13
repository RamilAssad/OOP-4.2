#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or not isinstance(second, float):
            raise ValueError("Некорректные значения аргументов")
        self.first = first
        self.second = second

    def __mul__(self, number):
        if not isinstance(number, float):
            raise ValueError("Некорректное значение аргумента")
        return Pair(self.first * number, self.second * number)

    def __str__(self):
        return f"first: {self.first}\nsecond: {self.second}"


def make_Pair(first, second):
    return Pair(first, second)


if __name__ == "__main__":
    p = make_Pair(3, 0.5)
    print(p)

    p = p * 2.5
    print(p)