#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(0, len(empty_list))

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual("peanut", noms[0])
        self.assertEqual("jelly", noms[3])
        self.assertEqual("jelly", noms[-1])
        self.assertEqual("butter", noms[-3])

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(["peanut"], noms[0:1])
        self.assertEqual(["peanut", "butter"], noms[0:2])
        self.assertEqual([], noms[2:2])
        self.assertEqual(["and", "jelly"], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        #start at 2 and end when list ends
        self.assertEqual(["and", "jelly"], noms[2:])
        # start at index 0 and end BEFORE index 2
        self.assertEqual(["peanut", "butter"], noms[:2])

    def test_lists_and_ranges(self):
       #a range type is range
        self.assertEqual(range, type(range(5)))
        #gives you a list from 1 (included) to 6 (excluded)
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        #gives you a list from 0 to the number specified (excluded)
        self.assertEqual([0,1,2,3,4], list(range(5)))
        self.assertEqual([5,6,7,8], list(range(5, 9)))

    def test_ranges_with_steps(self):
      #starts with larger number to small by subtracting 1 (3 not included)
        self.assertEqual([5,4], list(range(5, 3, -1)))
        #go from 0 to 8 by twos (8 not included)
        self.assertEqual([0,2,4,6], list(range(0, 8, 2)))
        #go from 1 to 8 by threes, (8 not included)
        self.assertEqual([1,4,7], list(range(1, 8, 3)))
        #go from 5 to -7 by subtracting 4 (-7 not included)
        self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
        #go from 5 to -8 by -4 (-8 not included)
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4)))

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        #inserts 'not' in knight list index 2
        knight.insert(2, 'not')
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10, 20, 30, 40, 'last'], stack)

        popped_value = stack.pop()
        #last gets popped off because its the last value in the list
        self.assertEqual('last', popped_value)
        #stack without the last value
        self.assertEqual([10, 20, 30, 40], stack)

        #pops off index 1
        popped_value = stack.pop(1)
        #pops off 20
        self.assertEqual(20, popped_value)
        #stack without 20
        self.assertEqual([10, 30, 40], stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')
        #append is same as push
        self.assertEqual([1,2, 'last'], queue)

        #pops off the first value
        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

