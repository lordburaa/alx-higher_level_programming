#!/usr/bin/python3
"""Cheking the sorted list"""


class MyList(list):
    """creating list"""

    def __init__(self):
        """initialization"""
        super().__init__()

    def print_sorted(self):
        """printing th esorted list"""
        print(sorted(self))
