# -*- coding: utf-8 -*-

import unittest


def where(entries, properties):
    ret = []

    if type(properties) is str:
        for entry in entries:
            if properties in entry:
                ret.append(entry[properties])

    if type(properties) is list:
        for entry in entries:
            obj = {}
            for p in properties:
                if p in entry:
                    obj[p] = entry[p]
            ret.append(obj)
    return ret


def initial(array):
    return array[0:len(array) - 1]


def rest(array):
    return array[1:len(array)]


class FilterModule(object):

    """ utility filters for operating on hashes """

    def filters(self):
        return {
            'where': where,
            'initial': initial,
            'rest': rest
        }


class TestCollectionUtils(unittest.TestCase):

    def test_where(self):
        l = [
            {'foo': 'bar', 'bar': 'quuux', 'baz': 'qux'},
            {'foo': 'baz', 'bar': 'quuuux', 'baz': 'quux'}
        ]
        self.assertEqual(where(l, 'foo'), ['bar', 'baz'])
        self.assertEqual(where(l, ['foo', 'baz']), [
            {'foo': 'bar', 'baz': 'qux'},
            {'foo': 'baz', 'baz': 'quux'}
        ])

    def test_initial(self):
        self.assertEqual(initial([1, 2, 3]), [1, 2])

    def test_rest(self):
        self.assertEqual(rest([1, 2, 3]), [2, 3])


if __name__ == '__main__':
    unittest.main()
