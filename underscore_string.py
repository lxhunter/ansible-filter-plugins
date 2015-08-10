# -*- coding: utf-8 -*-

import unittest
import re
import unicodedata

def string_sanity_check(string):
    if string is None:
        return ''
    if not isinstance(string, basestring):
        return str(string)
    return string


''' Converts underscored or dasherized string to a camelized one. Begins with a lower case letter unless it starts with an underscore, dash or an upper case letter. '''
def camelize(string, uppercase_first_letter=True):
    string = string_sanity_check(string)
    string = re.sub(r"^[-_\s]+", "", string)
    if uppercase_first_letter:
        return re.sub(r"(?:^|[-_\s]+)(.)", lambda m: m.group(1).upper(), string)
    else:
        return string[0].lower() + camelize(string)[1:]

''' Seperates each in char in a list '''
def chars(string):
    list = []
    list[:0] = string
    return list

''' Trim and replace multiple spaces with a single space. '''
def clean(string):
    string = string_sanity_check(string)
    return " ".join(string.split())

''' Counts the number of times needle is in haystack '''
def count(haystack, needle):
    haystack = string_sanity_check(haystack)
    needle = string_sanity_check(needle)
    if needle is '' or needle is None:
        return 0
    return haystack.count(needle)

''' Converts a underscored or camelized string into an dasherized one '''
def dasherize(string):
    string = string_sanity_check(string)
    string = string.strip()
    string = re.sub(r'([A-Z])', r'-\1', string)
    string = re.sub(r'[-_\s]+', r'-', string)
    string = re.sub(r'^-', r'', string)
    string = string.lower()
    return string

''' Checks whether the string ends with needle at position (default: haystack.length). '''
def ends_with(haystack, needle, beg=0, end=None):
    haystack = string_sanity_check(haystack)
    needle = string_sanity_check(needle)

    if end is None:
        end = len(haystack)
    return haystack.endswith(needle, beg, end)

''' Converts an underscored, camelized, or dasherized string into a humanized one. Also removes beginning and ending whitespace, and removes the postfix '_id'. '''
def humanize(string):
    if string is '' or string is None:
        return ''
    string = string_sanity_check(string)
    string = underscore(string)
    string = re.sub('_id$', '', string)
    string = string.replace("_", ' ')
    string = string.replace("-", ' ')
    string = string.strip()
    string = string[0].upper() + string[1:]
    string = re.sub(' +',' ', string)
    return string

''' Tests if string contains a substring. '''
def includes(haystack, needle):
    haystack = string_sanity_check(haystack)
    needle = string_sanity_check(needle)
    if needle in haystack:
        return True
    else:
        return False

''' Insert word in string at the defined position ''' 
def insert(string, index, substring):
    string = string_sanity_check(string)
    substring = string_sanity_check(substring)
    return string[:index] + substring + string[index:]

''' Returns split lines as an array '''
def lines(string):
    string = string_sanity_check(string)
    return re.split('\r\n?|\n', string)

''' Replace string in string '''
def splice(string, index, how_many, substring):
    return string[:index] + substring + string[index + how_many:]

''' Checks whether the string begins with the needle at position (default: 0). '''
def starts_with(haystack, needle, beg=0, end=None):
    if end is None:
        end = len(haystack)
    return haystack.startswith(needle, beg, end)

''' Returns the successor to string '''
def successor(string):
    strip_zs = string.rstrip('z')
    if strip_zs:
        return strip_zs[:-1] + chr(ord(strip_zs[-1]) + 1) + 'a' * (len(string) - len(strip_zs))
    else:
        return 'a' * (len(string) + 1)

''' Returns a copy of the string in which all the case-based characters have had their case swapped.'''
def swap_case(string):
    return string.swapcase()

def transliterate(string):
    normalized = unicodedata.normalize('NFKD', string)
    return normalized.encode('ascii', 'ignore').decode('ascii')

''' Converts a underscored or camelized string into an dasherized one '''
def underscore(string):
    string = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', string)
    string = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', string)
    string = string.replace("-", "_")
    return string.lower()

# ---

class FilterModule(object):
    def filters(self):
        return {
            'camelize': camelize,
            'chars': chars,
            'clean': clean,
            'count': count,
            'dasherize': dasherize,
            'ends_with': ends_with,
            'humanize': humanize,
            'includes': includes,
            'insert': insert,
            'lines': lines,
            'splice': splice,
            'starts_with': starts_with,
            'successor': successor,
            'swap_case': swap_case,
            'transliterate': transliterate,
            'underscore': underscore
        }

# ---

class TestStringUtlisFunctions(unittest.TestCase):

    def test_camelize(self):
        self.assertEqual(camelize('the_camelize_string_method',False), 'theCamelizeStringMethod');
        self.assertEqual(camelize('webkit-transform',False), 'webkitTransform');
        self.assertEqual(camelize('webkit-transform',True), 'WebkitTransform');
        self.assertEqual(camelize('-the-camelize-string-method',True), 'TheCamelizeStringMethod');
        self.assertEqual(camelize('_the_camelize_string_method'), 'TheCamelizeStringMethod');
        self.assertEqual(camelize('The-camelize-string-method'), 'TheCamelizeStringMethod');
        self.assertEqual(camelize('the camelize string method',False), 'theCamelizeStringMethod');
        self.assertEqual(camelize(' the camelize  string method',False), 'theCamelizeStringMethod');
        self.assertEqual(camelize('the camelize   string method',False), 'theCamelizeStringMethod');
        self.assertEqual(camelize(' with   spaces',False), 'withSpaces');
        self.assertEqual(camelize("_som eWeird---name"), 'SomEWeirdName');
        self.assertEqual(camelize(''), '', 'Camelize empty string returns empty string');
        self.assertEqual(camelize(None), '', 'Camelize null returns empty string');
        self.assertEqual(camelize(123), '123');

    def test_chars(self):
        self.assertEqual(chars("Hello"),['H', 'e', 'l', 'l', 'o'])
        self.assertNotEqual(chars("Hello"),['h', 'e', 'l', 'l', 'o'])        
        self.assertEqual(camelize(''), '', 'Chars empty string returns empty string');
        self.assertEqual(camelize(None), '', 'Chars null returns empty string');
        self.assertEqual(camelize(123), '123');

    def test_clean(self):
        self.assertEqual(clean(' foo    bar   '), 'foo bar');
        self.assertEqual(clean(123), '123');
        self.assertEqual(clean(''), '', 'cleaning empty string returns empty string');
        self.assertEqual(clean(None), '', 'cleaning null returns empty string');
        self.assertEqual(clean(' foo    bar   '), 'foo bar')
        self.assertEqual(clean('foo bar '), 'foo bar')
        self.assertEqual(clean('   foo\t bar '), 'foo bar')

    def test_count(self):
        self.assertEqual(count('Hello world', 'l'), 3);
        self.assertEqual(count('Hello world', 'Hello'), 1);
        self.assertEqual(count('Hello world', 'foo'), 0);
        self.assertEqual(count('x.xx....x.x', 'x'), 5);
        self.assertEqual(count('', 'x'), 0);
        self.assertEqual(count(None, 'x'), 0);
        self.assertEqual(count(12345, 1), 1);
        self.assertEqual(count(11345, 1), 2);
        self.assertEqual(count('Hello World', ''), 0);
        self.assertEqual(count('Hello World', None), 0);
        self.assertEqual(count('', ''), 0);

    def test_dasherize(self):
        self.assertEqual(dasherize('foo_bar'), 'foo-bar') 
        self.assertEqual(dasherize('the_dasherize_string_method'), 'the-dasherize-string-method');
        self.assertEqual(dasherize('thisIsATest'), 'this-is-a-test');
        self.assertEqual(dasherize('this Is A Test'), 'this-is-a-test');
        self.assertEqual(dasherize('thisIsATest123'), 'this-is-a-test123');
        self.assertEqual(dasherize('123thisIsATest'), '123this-is-a-test');
        self.assertEqual(dasherize('the dasherize string method'), 'the-dasherize-string-method');
        self.assertEqual(dasherize('the  dasherize string method  '), 'the-dasherize-string-method');
        self.assertEqual(dasherize('téléphone'), 'téléphone');
        self.assertEqual(dasherize('foo$bar'), 'foo$bar');
        self.assertEqual(dasherize(''), '');
        self.assertEqual(dasherize(None), '');
        self.assertEqual(dasherize(123), '123');

    def test_ends_with(self):
        self.assertEqual(ends_with('image.gif', 'gif'), True)        
        self.assertEqual(ends_with('foobar', 'bar'), True);
        self.assertEqual(ends_with('foobarfoobar', 'bar'), True);
        self.assertEqual(ends_with('foo', 'o'), True);
        self.assertEqual(ends_with('foobar', 'bar'), True);
        self.assertEqual(ends_with('00018-0000062.Plone.sdh264.1a7264e6912a91aa4a81b64dc5517df7b8875994.mp4', 'mp4'), True);
        self.assertEqual(ends_with('fooba', 'bar'),False);
        self.assertEqual(ends_with(12345, 45), True);
        self.assertEqual(ends_with(12345, 6), False);
        self.assertEqual(ends_with('', ''), True);
        self.assertEqual(ends_with(None, ''), True);
        self.assertEqual(ends_with(None, 'foo'), False);
        self.assertEqual(ends_with('foobä', 'ä'), True);        

    def test_humanize(self):
        self.assertEqual(humanize('the_humanize_string_method'), 'The humanize string method');
        self.assertEqual(humanize('ThehumanizeStringMethod'), 'Thehumanize string method');
        self.assertEqual(humanize('-ThehumanizeStringMethod'), 'Thehumanize string method');
        self.assertEqual(humanize('the humanize string method'), 'The humanize string method');
        self.assertEqual(humanize('the humanize_id string method_id'), 'The humanize id string method');
        self.assertEqual(humanize('the  humanize string method  '), 'The humanize string method');
        self.assertEqual(humanize('   capitalize dash-CamelCase_underscore trim  '), 'Capitalize dash camel case underscore trim');
        self.assertEqual(humanize(123), '123');
        self.assertEqual(humanize(''), '');
        self.assertEqual(humanize(None), '');

    def test_includes(self):
        self.assertEqual(includes('foobar', 'ob'), True)
        self.assertEqual(includes('foobar', 'qux'), False)  
        self.assertEqual(includes('foobar', 'bar'), True);
        self.assertEqual(includes('foobar', 'buzz'), False);
        self.assertEqual(includes(12345, 34), True);
        self.assertEqual(includes(12345, 6), False);
        self.assertEqual(includes('', 34), False);
        self.assertEqual(includes(None, 34), False);
        self.assertEqual(includes(None, ''), True);      

    def test_insert(self):
        self.assertEqual(insert('foo ', 4, 'bar'), 'foo bar')
        self.assertEqual(insert('Hello ', 6, 'Jessy'), 'Hello Jessy');
        self.assertEqual(insert('Hello ', 100, 'Jessy'), 'Hello Jessy');
        self.assertEqual(insert('', 100, 'Jessy'), 'Jessy');
        self.assertEqual(insert(None, 100, 'Jessy'), 'Jessy');
        self.assertEqual(insert(12345, 6, 'Jessy'), '12345Jessy');        

    def test_lines(self):
        self.assertEqual(lines('foo\nbar'), ['foo', 'bar'])
        self.assertEqual(len(lines('Hello\nWorld')), 2);
        self.assertEqual(len(lines('Hello\rWorld')), 2);
        self.assertEqual(len(lines('Hello World')), 1);
        self.assertEqual(len(lines('\r\n\n\r')), 4);
        self.assertEqual(len(lines('Hello\r\r\nWorld')), 3);
        self.assertEqual(len(lines('Hello\r\rWorld')), 3);
        self.assertEqual(len(lines(123)), 1);
    
    def test_splice(self):
        self.assertEqual(splice('http://github.com/lxhunter/string', 18, 8, 'awesome'),
                         'http://github.com/awesome/string')

    def test_starts_with(self):
        self.assertEqual(starts_with('image.gif', 'image'), True)        

    def test_successor(self):
        self.assertEqual(successor('a'), 'b')
        self.assertEqual(successor('b'), 'c')
        self.assertEqual(successor('z'), 'aa')

    def test_swap_case(self):
        self.assertEqual(swap_case('fOO'), 'Foo')

    def test_transliterate(self):
        self.assertEqual(transliterate(u'älämölö'), u'alamolo')
        self.assertEqual(transliterate(u'Ærøskøbing'),  u'rskbing')        

    def test_underscore(self):
        self.assertEqual(underscore('FooBar'), 'foo_bar')

if __name__ == '__main__':
    unittest.main()          