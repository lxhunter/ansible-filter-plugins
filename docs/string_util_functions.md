## List of underscore string functions

#### camelize
###### method: camelize(string, uppercase_first_letter=True)
> custom implementation / needs to be installed

Converts underscored or dasherized string to a camelized one. Begins with a lower case letter unless it starts with an underscore, dash or an upper case letter.

#### clean
###### method: clean(string)
> custom implementation / needs to be installed

Trim and replace multiple spaces with a single space.

#### classify
###### method: classify(string)
> custom implementation / needs to be installed

Converts string to camelized class name. First letter is always upper case.

#### count
###### method: count(haystack, needle)
> custom implementation / needs to be installed

Counts the number of times needle is in haystack

#### dasherize
###### method: dasherize(string)
> custom implementation / needs to be installed

Converts a underscored or camelized string into an dasherized one

#### decapitalize
###### method: decapitalize(string)
> custom implementation / needs to be installed

Converts first letter of the string to lowercase.

#### dedent
###### method: dedent(string)
> custom implementation / needs to be installed

_Using Python Standard Library textwrap_

Remove any common leading whitespace from every line in text.

This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form.

Note that tabs and spaces are both treated as whitespace, but they are not equal: the lines `  hello` and `\thello` are considered to have no common leading whitespace.


#### ends_with
###### method: ends_with(haystack, needle, beg=0, end=None)
> custom implementation / needs to be installed

Checks whether the string ends with needle at position (default: haystack.length).


#### escape_html
###### method: escape_html(string)
> custom implementation / needs to be installed

Converts HTML special characters to their entity equivalents. This function supports cent, yen, euro, pound, lt, gt, copy, reg, quote, amp, apos.

#### humanize
###### method: humanize(string)
> custom implementation / needs to be installed

Converts an underscored, camelized, or dasherized string into a humanized one. Also removes beginning and ending whitespace, and removes the postfix '_id'.

```python
{{ 'the_humanize_string_method' | humanize }}
# => 'The humanize string method'

{{ 'ThehumanizeStringMethod' | humanize }}
# => 'Thehumanize string method'

{{ 'the humanize_id string method_id' | humanize }}
# => 'Thehumanize string method'

{{ '   capitalize dash-CamelCase_underscore trim  ' | humanize }}
# => 'Capitalize dash camel case underscore trim'
```

#### includes
###### method: includes(haystack, needle)
> custom implementation / needs to be installed

Tests if string contains a substring.

```python
{{ 'foobar' | includes('ob') }}
# => True

{{ 'foobar' | includes('qux') }}
# => False

{{ 'foobar' | includes('bar') }}
# => True

{{ 'foobar' | includes('buzz') }}
# => False

{{ 12345 | includes(34) }}
# => True
```

#### insert
###### method: insert(string, index, substring)
> custom implementation / needs to be installed

Insert word in string at the defined position.

```python
{{ 'foo ' | insert(4, 'bar') }}
# => 'foo bar'

{{ 'Hello ' | insert(6, 'Jessy') }}
# => 'Hello Jessy'

{{ 'Hello ' | insert(100, 'Jessy') }}
# => 'Hello Jessy'
```

#### lpad
###### method: lpad(width[, fillchar])
> custom implementation / needs to be installed

_Using Python Standard Library string rjust_

Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than or equal to len(s).

```python
{{ '1' | lpad(8) }}
# => '       1'

{{ 1 | lpad(8) }}
# => '       1'

{{ '1' | lpad(8, '0') }}
# => '00000001'

```

#### ltrim
###### method: lpad(width[, fillchar])
> custom implementation / needs to be installed

_Using Python Standard Library string lstrip_

Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace.

```python
{{ ' foo' | ltrim }}
# => 'foo'

{{ '    foo' | ltrim }}
# => 'foo'

{{ 'foo ' | ltrim }}
# => 'foo '

{{ ' foo ' | ltrim }}
# => 'foo '
```

#### repeat
###### method: repeat(string, count, separator=None)
> custom implementation / needs to be installed

Repeats a string count times, can be seperated by separator.

```python
{{ 'foo' | repeat(3) }}
# => 'foofoofoo'

{{ 'foo' | repeat('3') }}
# => 'foofoofoo'

{{ 123 | repeat(2) }}
# => '123123'

{{ '1234' | repeat(2, '*') }}
# => '1234*1234'

{{ '1234' | repeat(2, '**') }}
# => '1234**1234'
```

#### rpad
###### method: rpad(string, width, fillchar=' ')
> custom implementation / needs to be installed

Return the string right justified in a string of length width.

```python
{{ '1' | rpad(8) }}
# => '1       '

{{ 1 | rpad(8) }}
# => '1       '

{{ 1 | rpad(8, '0') }}
# => '10000000'

{{ 'foo' | rpad(8, '0') }}
# => 'foo00000'

{{ 'foo' | rpad(7, '0') }}
# => 'foo0000'
```

#### rtrim
###### method: rtrim(string, characters)
> custom implementation / needs to be installed

_Using Python Standard Library string rstrip_

Return a copy of the string with trailing characters removed. If chars is omitted or `None`, whitespace characters are removed. If given and not `None`, chars must be a string; the characters in the string will be stripped from the end of the string this method is called on.

```python
{{ 'http://foo/' | rtrim('/') }}
# => 'http://foo'

{{ ' foo' | rtrim }}
# => ' foo'

{{ 'foo     ' | rtrim }}
# => 'foo'

{{ 'ffoo' | rtrim('f') }}
# => 'ffoo'

{{ 'ooff' | rtrim('f') }}
# => 'oo'
```

#### splice
###### method: splice(string, index, howmany, substring)
> custom implementation / needs to be installed

Adds/removes substring to/from string.

```python
{{ 'http://github.com/lxhunter/string' | splice(18, 8, 'awesome') }}
# => 'http://github.com/awesome/string'

{{ 12345 | splice(1, 2, 321) }}
# => '132145'
```

#### slugify
###### method: slugify(string)
> custom implementation / needs to be installed

_caution: needs python-slugify `pip install python-slugify`_

Transform text into an ascii slug which can be used in safely in URLs. Replaces whitespaces, accentuated, and special characters with a dash. Limited set of non-ascii characters are transformed to similar versions in the ascii character set such as `ä` to `a`.

```python

{{ 'This is a test ---' | slugify }}
# => "this-is-a-test"

{{ 'jaja---lol-méméméoo--a' | slugify(max_length=9) }}
# => "jaja-lol"

{{ 'jaja---lol-méméméoo--a' | slugify(max_length=15, word_boundary=True) }}
# => "jaja-lol-a"

{{ 'jaja---lol-méméméoo--a' | slugify(max_length=15, word_boundary=True, separator=".") }}
# => "jaja.lol.a"

{{ 'one two three four five' | slugify(max_length=13, word_boundary=True, save_order=True) }}
# => "one-two-three"

```

#### starts_with
###### method: starts_with(haystack, needle, beg=0, end=None)
> custom implementation / needs to be installed

_Using Python Standard Library string startswith_

Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.

```python
{{ 'image.gif' | starts_with('image') }}
# => True

{{ 'foobar' | starts_with(, 'foo') }}
# => True

{{ 'oobar' | starts_with('foo') }}
# => False

{{ 'oobar' | starts_with(, 'o') }}
# => True
```
