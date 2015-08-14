# -*- coding: utf-8 -*-

import unittest
import re
import unicodedata
import textwrap
from slugify import slugify

def string_sanity_check(string):
    if string is None:
        return ''
    if not isinstance(string, basestring):
        return str(string)
    return string


''' Converts underscored or dasherized string to a camelized one. Begins with a lower case letter unless it starts with an underscore, dash or an upper case letter. '''
def camelize(string, uppercase_first_letter=True):
    sanitzed_string = string_sanity_check(string)
    replaced = re.sub(r"^[-_\s]+", "", sanitzed_string)
    if uppercase_first_letter:
        return re.sub(r"(?:^|[-_\s]+)(.)", lambda m: m.group(1).upper(), replaced)
    else:
        return replaced[0].lower() + camelize(replaced)[1:]

''' '''
def classify(string):
    sanitzed_string = string_sanity_check(string)
    replaced = re.sub(r"(?:^|[\.]+)(.)", lambda m: m.group(1).upper(), sanitzed_string)
    return camelize(replaced) 

''' Trim and replace multiple spaces with a single space. '''
def clean(string):
    sanitzed_string = string_sanity_check(string)
    return " ".join(sanitzed_string.split())

''' Counts the number of times needle is in haystack '''
def count(haystack, needle):
    haystack = string_sanity_check(haystack)
    needle = string_sanity_check(needle)
    if needle is '' or needle is None:
        return 0
    return haystack.count(needle)

''' Converts a underscored or camelized string into an dasherized one '''
def dasherize(string):
    sanitzed_string = string_sanity_check(string)
    striped = sanitzed_string.strip()
    replaced = re.sub(r'([A-Z])', r'-\1', striped)
    replaced = re.sub(r'[-_\s]+', r'-', replaced)
    replaced = re.sub(r'^-', r'', replaced)
    return replaced.lower()

''' Converts first letter of the string to lowercase. '''
def decapitalize(string):
    sanitzed_string = string_sanity_check(string)
    if sanitzed_string is '' or sanitzed_string is None:
        return ''
    return sanitzed_string[0].lower() + sanitzed_string[1:]


''' Dedent unnecessary indentation. '''
def dedent(string):
    sanitzed_string = string_sanity_check(string)
    if sanitzed_string is '' or sanitzed_string is None:
        return ''
    return textwrap.dedent(sanitzed_string)

''' Checks whether the string ends with needle at position (default: haystack.length). '''
def ends_with(haystack, needle, beg=0, end=None):
    haystack = string_sanity_check(haystack)
    needle = string_sanity_check(needle)
    if end is None:
        end = len(haystack)
    return haystack.endswith(needle, beg, end)

''' Converts HTML special characters to their entity equivalents. This function supports cent, yen, euro, pound, lt, gt, copy, reg, quote, amp, apos. '''
def escape_html(haystack):
    haystack = string_sanity_check(haystack)
    return haystack.replace('&' , '&amp;') \
    .replace('¢' , '&cent;') \
    .replace('£' , '&pound;') \
    .replace('¥' , '&yen;') \
    .replace('€' , '&euro;') \
    .replace('©' , '&copy;') \
    .replace('®' , '&reg;') \
    .replace('<' , '&lt;') \
    .replace('>' , '&gt;') \
    .replace('"' , '&quot;') \
    .replace("'" , '&#39;')

''' Converts an underscored, camelized, or dasherized string into a humanized one. Also removes beginning and ending whitespace, and removes the postfix '_id'. '''
def humanize(string):
    if string is '' or string is None:
        return ''
    sanitzed_string = string_sanity_check(string)
    underscored = underscore(sanitzed_string)
    replaced = re.sub('_id$', '', underscored)
    replaced = replaced.replace("_", ' ')
    replaced = replaced.replace("-", ' ')
    striped = replaced.strip()
    firstUp = striped[0].upper() + striped[1:]
    return re.sub(' +',' ', firstUp)

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
    sanitzed_string = string_sanity_check(string)
    sanitzed_substring = string_sanity_check(substring)
    return sanitzed_string[:index] + sanitzed_substring + sanitzed_string[index:]

''' Returns split lines as an array '''
def lines(string):
    sanitzed_string = string_sanity_check(string)
    return re.split('\r\n?|\n', sanitzed_string)

''' Return the string left justified in a string of length width. '''
def lpad(string, width, fillchar=' '):
    sanitzed_string = string_sanity_check(string)
    return sanitzed_string.rjust(width, fillchar)

''' Return a copy of the string with leading characters removed. '''
def ltrim(string,chars=None):
    sanitzed_string = string_sanity_check(string)
    if isinstance( chars, int):
        chars = str(chars)
    return sanitzed_string.lstrip(chars)

''' Repeats a string count times. '''
def repeat(string, count, separator=None):
    sanitzed_string = string_sanity_check(string)
    sanitzed_count = int(count)
    if separator is None:
        return sanitzed_count * sanitzed_string
    sanitzed_separator = str(separator)
    return (sanitzed_count * (sanitzed_string + str(sanitzed_separator)))[:-len(sanitzed_separator)]

''' Return the string right justified in a string of length width. '''
def rpad(string, width, fillchar=' '):
    sanitzed_string = string_sanity_check(string)
    return sanitzed_string.ljust(width, fillchar)

''' Return a copy of the string with trailing characters removed. '''
def rtrim(string,chars=None):
    sanitzed_string = string_sanity_check(string)
    if isinstance( chars, int):
        chars = str(chars)
    return sanitzed_string.rstrip(chars)

def _slugify(string, entities=True, decimal=True, hexadecimal=True, max_length=0, word_boundary=False,
            separator='-', save_order=False, stopwords=()):
    if string is None:
        return ''
    sanitzed_string = string_sanity_check(string)
    return slugify(sanitzed_string, entities, decimal, hexadecimal, max_length, word_boundary,
            separator, save_order, stopwords)

''' Replace string in string '''
def splice(string, index, how_many, substring):
    sanitzed_string = string_sanity_check(string)
    sanitzed_substring = string_sanity_check(substring)
    return sanitzed_string[:index] + sanitzed_substring + sanitzed_string[index + how_many:]

''' Checks whether the string begins with the needle at position (default: 0). '''
def starts_with(haystack, needle, beg=0, end=None):
    if end is None:
        end = len(haystack)
    return haystack.startswith(needle, beg, end)

''' Returns the successor to string '''
def successor(string):
    sanitzed_string = string_sanity_check(string)
    strip_zs = sanitzed_string.rstrip('z')
    if strip_zs:
        return strip_zs[:-1] + chr(ord(strip_zs[-1]) + 1) + 'a' * (len(sanitzed_string) - len(strip_zs))
    else:
        return 'a' * (len(sanitzed_string) + 1)

''' Returns a copy of the string in which all the case-based characters have had their case swapped.'''
def swap_case(string):
    sanitzed_string = string_sanity_check(string)
    return string.swapcase()

def transliterate(string):
    sanitzed_string = string_sanity_check(string)
    normalized = unicodedata.normalize('NFKD', sanitzed_string)
    return normalized.encode('ascii', 'ignore').decode('ascii')

''' Converts a underscored or camelized string into an dasherized one '''
def underscore(string):
    sanitzed_string = string_sanity_check(string)
    replaced = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', sanitzed_string)
    replaced = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', replaced)
    return replaced.replace("-", "_").lower()

''' Converts entity characters to HTML equivalents. This function supports cent, yen, euro, pound, lt, gt, copy, reg, quote, amp, apos, nbsp. '''
def unescape_html(haystack):
    haystack = string_sanity_check(haystack)
    return haystack.replace('&#39;',"'") \
    .replace('&cent;', '¢') \
    .replace('&pound;','£') \
    .replace('&yen;','¥') \
    .replace('&euro;','€') \
    .replace('&copy;','©') \
    .replace('&reg;','®') \
    .replace('&lt;','<') \
    .replace('&gt;','>') \
    .replace('&quot;','"') \
    .replace('&apos;', "'") \
    .replace('&#0039;', "'") \
    .replace('&nbsp;', ' ') \
    .replace('&amp;','&')

# ---

class FilterModule(object):
    def filters(self):
        return {
            'camelize': camelize,
            'clean': clean,
            'classify': classify,
            'count': count,
            'dasherize': dasherize,
            'decapitalize': decapitalize,
            'dedent': dedent,
            'ends_with': ends_with,
            'escape_html': escape_html,
            'humanize': humanize,
            'includes': includes,
            'insert': insert,
            'lines': lines,
            'lpad': lpad,
            'ltrim': ltrim,
            'rpad': rpad,
            'rtrim': rtrim,
            'repeat': repeat,
            'slugify': _slugify,
            'splice': splice,
            'starts_with': starts_with,
            'successor': successor,
            'swap_case': swap_case,
            'transliterate': transliterate,
            'underscore': underscore,
            'unescape_html': unescape_html
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

    def test_classify(self):
        self.assertEqual(classify(1), '1');
        self.assertEqual(classify('some_class_name'), 'SomeClassName');
        self.assertEqual(classify('my wonderfull class_name'), 'MyWonderfullClassName');
        self.assertEqual(classify('my wonderfull.class.name'), 'MyWonderfullClassName');
        self.assertEqual(classify('myLittleCamel'), 'MyLittleCamel');
        self.assertEqual(classify('myLittleCamel.class.name'), 'MyLittleCamelClassName');
        self.assertEqual(classify(123), '123');
        self.assertEqual(classify(''), '');
        self.assertEqual(classify(None), '');

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

    def test_decapitalize(self):
        self.assertEqual(decapitalize('Fabio'), 'fabio', 'First letter is lower case');
        self.assertEqual(decapitalize('Fabio'), 'fabio', 'First letter is lower case');
        self.assertEqual(decapitalize('FOO'), 'fOO', 'Other letters unchanged');
        self.assertEqual(decapitalize(123), '123', 'Non string');
        self.assertEqual(decapitalize(''), '', 'Decapitalizing empty string returns empty string');
        self.assertEqual(decapitalize(None), '', 'Decapitalizing null returns empty string');

    def test_dedent(self):
        self.assertEqual(dedent('Hello\nWorld'), 'Hello\nWorld');
        self.assertEqual(dedent('Hello\t\nWorld'), 'Hello\t\nWorld');
        self.assertEqual(dedent('Hello \nWorld'), 'Hello \nWorld');
        self.assertEqual(dedent('Hello\n  World'), 'Hello\n  World');
        self.assertEqual(dedent('    Hello\n  World'), '  Hello\nWorld');
        self.assertEqual(dedent('  Hello\nWorld'), '  Hello\nWorld');
        self.assertEqual(dedent('  Hello World'), 'Hello World');
        self.assertEqual(dedent('  Hello\n  World'), 'Hello\nWorld');
        self.assertEqual(dedent('  Hello\n    World'), 'Hello\n  World');
        self.assertEqual(dedent('\t\tHello\tWorld'), 'Hello\tWorld');
        self.assertEqual(dedent('\t\tHello\n\t\tWorld'), 'Hello\nWorld');
        self.assertEqual(dedent('Hello\n\t\tWorld'), 'Hello\n\t\tWorld');
        self.assertEqual(dedent('\t\tHello\n\t\t\t\tWorld'), 'Hello\n\t\tWorld');
        self.assertEqual(dedent('\t\tHello\r\n\t\t\t\tWorld'), 'Hello\r\n\t\tWorld');
        self.assertEqual(dedent('\t\tHello\n\n\n\n\t\t\t\tWorld'), 'Hello\n\n\n\n\t\tWorld');

    def test_escape_html(self):
        self.assertEqual(escape_html('<div>Blah & "blah" & \'blah\'</div>'), '&lt;div&gt;Blah &amp; &quot;blah&quot; &amp; &#39;blah&#39;&lt;/div&gt;')
        self.assertEqual(escape_html('&lt;'), '&amp;lt;')
        self.assertEqual(escape_html(' '), ' ')
        self.assertEqual(escape_html('¢'), '&cent;')
        self.assertEqual(escape_html('¢ £ ¥ € © ®'), '&cent; &pound; &yen; &euro; &copy; &reg;')
        self.assertEqual(escape_html(5), '5');
        self.assertEqual(escape_html(''), '');
        self.assertEqual(escape_html(None), '');

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
    
    def test_lpad(self):
        self.assertEqual(lpad('1', 8), '       1');
        self.assertEqual(lpad(1, 8), '       1');
        self.assertEqual(lpad('1', 8, '0'), '00000001');
        self.assertEqual(lpad('', 2), '  ');
        self.assertEqual(lpad(None, 2), '  ');

    def test_ltrim(self):
        self.assertEqual(ltrim(' foo'), 'foo');
        self.assertEqual(ltrim('    foo'), 'foo');
        self.assertEqual(ltrim('foo '), 'foo ');
        self.assertEqual(ltrim(' foo '), 'foo ');
        self.assertEqual(ltrim(''), '', 'ltrim empty string should return empty string');
        self.assertEqual(ltrim(None), '', 'ltrim null should return empty string');
        self.assertEqual(ltrim('ffoo', 'f'), 'oo');
        self.assertEqual(ltrim('ooff', 'f'), 'ooff');
        self.assertEqual(ltrim('ffooff', 'f'), 'ooff');
        self.assertEqual(ltrim('_-foobar-_', '_-'), 'foobar-_');
        self.assertEqual(ltrim(123, 1), '23');

    def test_repeat(self):
        self.assertEqual(repeat('foo', 3), 'foofoofoo');
        self.assertEqual(repeat('foo', '3'), 'foofoofoo');
        self.assertEqual(repeat(123, 2), '123123');
        self.assertEqual(repeat(1234, 2, '*'), '1234*1234');
        self.assertEqual(repeat(1234, 2, '**'), '1234**1234');
        self.assertEqual(repeat(1234, 2, 5), '123451234');

    def test_rpad(self):
        self.assertEqual(rpad('1', 8), '1       ');
        self.assertEqual(rpad(1, 8), '1       ');
        self.assertEqual(rpad('1', 8, '0'), '10000000');
        self.assertEqual(rpad('foo', 8, '0'), 'foo00000');
        self.assertEqual(rpad('foo', 7, '0'), 'foo0000');
        self.assertEqual(rpad('', 2), '  ');
        self.assertEqual(rpad(None, 2), '  ');

    def test_rtrim(self):
        self.assertEqual(rtrim('http://foo/', '/'), 'http://foo');
        self.assertEqual(rtrim(' foo'), ' foo');
        self.assertEqual(rtrim('foo '), 'foo');
        self.assertEqual(rtrim('foo     '), 'foo');
        self.assertEqual(rtrim('foo  bar     '), 'foo  bar');
        self.assertEqual(rtrim(' foo '), ' foo');
        self.assertEqual(rtrim('ffoo', 'f'), 'ffoo');
        self.assertEqual(rtrim('ooff', 'f'), 'oo');
        self.assertEqual(rtrim('ffooff', 'f'), 'ffoo');
        self.assertEqual(rtrim('_-foobar-_', '_-'), '_-foobar');
        self.assertEqual(rtrim(123, 3), '12');
        self.assertEqual(rtrim(''), '');
        self.assertEqual(rtrim(None), '');

    def test_slugify(self):
        self.assertEqual(_slugify('Jack & Jill like numbers 1,2,3 and 4 and silly characters ?%.$!/'), 'jack-jill-like-numbers-1-2-3-and-4-and-silly-characters');
        self.assertEqual(_slugify('I know latin characters: á í ó ú ç ã õ ñ ü ă ș ț'), 'i-know-latin-characters-a-i-o-u-c-a-o-n-u-a-s-t');
        self.assertEqual(_slugify('I am a word too, even though I am but a single letter: i!'), 'i-am-a-word-too-even-though-i-am-but-a-single-letter-i');
        self.assertEqual(_slugify(''), '');
        self.assertEqual(_slugify(None), '');
        self.assertEqual(_slugify("This is a test ---"), "this-is-a-test")
        self.assertEqual(_slugify("___This is a test ---"), "this-is-a-test")
        self.assertEqual(_slugify("___This is a test___"), "this-is-a-test")
        self.assertEqual(_slugify("This -- is a ## test ---"), "this-is-a-test")
        self.assertEqual(_slugify('影師嗎'), "ying-shi-ma")
        self.assertEqual(_slugify('C\'est déjà l\'été.'), "cest-deja-lete")
        self.assertEqual(_slugify('Nín hǎo. Wǒ shì zhōng guó rén'), "nin-hao-wo-shi-zhong-guo-ren")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a'), "jaja-lol-mememeoo-a")
        self.assertEqual(_slugify('Компьютер'), "kompiuter")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=9), "jaja-lol")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=15), "jaja-lol-mememe")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=50), "jaja-lol-mememeoo-a")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=15, word_boundary=True), "jaja-lol-a")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=17, word_boundary=True), "jaja-lol-mememeoo")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=18, word_boundary=True), "jaja-lol-mememeoo")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=19, word_boundary=True), "jaja-lol-mememeoo-a")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=20, word_boundary=True, separator="."), "jaja.lol.mememeoo.a")
        self.assertEqual(_slugify('jaja---lol-méméméoo--a', max_length=20, word_boundary=True, separator="ZZZZZZ"), "jajaZZZZZZlolZZZZZZmememeooZZZZZZa")
        self.assertEqual(_slugify('one two three four five', max_length=13, word_boundary=True, save_order=True), "one-two-three")
        self.assertEqual(_slugify('one two three four five', max_length=13, word_boundary=True, save_order=False), "one-two-three")
        self.assertEqual(_slugify('one two three four five', max_length=12, word_boundary=True, save_order=False), "one-two-four")
        self.assertEqual(_slugify('one two three four five', max_length=12, word_boundary=True, save_order=True), "one-two")
        self.assertEqual(_slugify('this has a stopword', stopwords=['stopword']), 'this-has-a')
        self.assertEqual(_slugify('the quick brown fox jumps over the lazy dog', stopwords=['the']), 'quick-brown-fox-jumps-over-lazy-dog')
        self.assertEqual(_slugify('Foo A FOO B foo C', stopwords=['foo']), 'a-b-c')
        self.assertEqual(_slugify('Foo A FOO B foo C', stopwords=['FOO']), 'a-b-c')
        self.assertEqual(_slugify('the quick brown fox jumps over the lazy dog in a hurry', stopwords=['the', 'in', 'a', 'hurry']), 'quick-brown-fox-jumps-over-lazy-dog')
        self.assertEqual(_slugify('foo &amp; bar'), 'foo-bar')

    def test_splice(self):
        self.assertEqual(splice('http://github.com/lxhunter/string', 18, 8, 'awesome'),
                         'http://github.com/awesome/string')
        self.assertEqual(splice(12345, 1, 2, 321), '132145');

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

    def test_unescape_html(self):
        self.assertEqual(unescape_html('&lt;div&gt;Blah &amp; &quot;blah&quot; &amp; &#39;blah&#39;&lt;/div&gt;'),'<div>Blah & "blah" & \'blah\'</div>')
        self.assertEqual(unescape_html('&amp;lt;'), '&lt;')
        self.assertEqual(unescape_html('&apos;'), '\'')
        self.assertEqual(unescape_html('&#39;'), '\'')
        self.assertEqual(unescape_html('&#0039;'), '\'')
        self.assertEqual(unescape_html('&#X4A;'), '&#X4A;')
        self.assertEqual(unescape_html('&_#39;'), '&_#39;')
        self.assertEqual(unescape_html('&#39_;'), '&#39_;')
        self.assertEqual(unescape_html('&amp;#38;'), '&#38;')
        self.assertEqual(unescape_html('&#39;'), "'")
        self.assertEqual(unescape_html(''), '')
        self.assertEqual(unescape_html('&nbsp;'), ' ')
        self.assertEqual(unescape_html('what is the &yen; to &pound; to &euro; conversion process?'), 'what is the ¥ to £ to € conversion process?')
        self.assertEqual(unescape_html('&reg; trademark'), '® trademark')
        self.assertEqual(unescape_html('&copy; 1992. License available for 50 &cent;'), '© 1992. License available for 50 ¢')
        self.assertEqual(unescape_html('&nbsp;'), ' ')
        self.assertEqual(unescape_html('&nbsp;'), ' ')
        self.assertEqual(unescape_html(None), '')

if __name__ == '__main__':
    unittest.main()          