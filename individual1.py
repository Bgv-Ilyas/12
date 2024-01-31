#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    def generate_permutations(arr, start, end):
        if start == end:
            print(arr)
        else:
            for i in range(start, end + 1):
                arr[start], arr[i] = arr[i], arr[start] 
                generate_permutations(arr, start + 1, end)
                arr[start], arr[i] = arr[i], arr[start] 

    def print_permutations(n):
        arr = list(range(1, n + 1))
        generate_permutations(arr, 0, n - 1)

    print_permutations(5)
