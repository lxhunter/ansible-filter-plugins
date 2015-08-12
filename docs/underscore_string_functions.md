## List of underscore string functions 

#### camelize
###### method: camelize(string, uppercase_first_letter=True)
> custom implementation / needs to be installed

Converts underscored or dasherized string to a camelized one. Begins with a lower case letter unless it starts with an underscore, dash or an upper case letter.

```python
{{ 'the_camelize_string_method' | camelize }}
# => TheCamelizeStringMethod

{{ 'webkit-transform' | camelize(True) }}
# => WebkitTransform

{{ 'webkit-transform' | camelize(False) }}
# => webkitTransform
```

#### clean
###### method: clean(string)
> custom implementation / needs to be installed

Trim and replace multiple spaces with a single space.

```python
{{ ' foo    bar   ' | clean }}
# => 'foo bar'

{{ 123 | clean }}
# => 123

{{ '   foo\t bar ' | clean }}
# => 'foo bar'
```

#### classify
###### method: classify(string)
> custom implementation / needs to be installed

Converts string to camelized class name. First letter is always upper case.

```python
{{ 'some_class_name' | classify }}
# => 'SomeClassName'

{{ 'my wonderfull class_name' | classify }}
# => 'MyWonderfullClassName'

{{ 'my wonderfull.class.name' | classify }}
# => 'MyWonderfullClassName'

{{ 'myLittleCamel' | classify }}
# => 'MyLittleCamel'
```

#### count
###### method: count(haystack, needle)
> custom implementation / needs to be installed

Counts the number of times needle is in haystack

```python
{{ 'Hello world' | count('l') }}
# => 3

{{ 'Hello world' | count('Hello') }}
# => 1

{{ 'Hello world' | count('foo') }}
# => 0

{{ 'x.xx....x.x' | count('x') }}
# => 5
```

#### dasherize
###### method: dasherize(string)
> custom implementation / needs to be installed

Converts a underscored or camelized string into an dasherized one

```python
{{ 'foo_bar' | dasherize }}
# => 'foo-bar'

{{ 'the_dasherize_string_method' | dasherize }}
# => 'the-dasherize-string-method'

{{ 'thisIsATest' | dasherize }}
# => 'this-is-a-test'

{{ 'this Is A Test' | dasherize }}
# => 'this-is-a-test'
```

#### decapitalize
###### method: decapitalize(string)
> custom implementation / needs to be installed

Converts first letter of the string to lowercase.

```python
{{ 'Fabio' | decapitalize }}
# => 'fabio'

{{ 'FOO' | decapitalize }}
# =>  'fOO'
 
{{ 123 | decapitalize }}
# => '123'
```

#### dedent
###### method: dedent(string)
> custom implementation / needs to be installed

_Using Python Standard Library textwrap_

Remove any common leading whitespace from every line in text.

This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form.

Note that tabs and spaces are both treated as whitespace, but they are not equal: the lines `  hello` and `\thello` are considered to have no common leading whitespace.

```python
{{ 'Hello\nWorld' | dedent }}
# => 'Hello\nWorld'

{{ 'Hello\t\nWorld' | dedent }}
# =>  'Hello\t\nWorld'
 
{{ 'Hello \nWorld' | dedent }}
# => 'Hello \nWorld'

{{ '    Hello\n  World' | dedent }}
# => '  Hello\nWorld'
```

#### ends_with
###### method: ends_with(haystack, needle, beg=0, end=None)
> custom implementation / needs to be installed

Checks whether the string ends with needle at position (default: haystack.length).

```python

{{ 'image.gif' | ends_with('gif')) }}
# => true

{{ 'foobar' | ends_with('bar')) }}
# => true

{{ 'foobarfoobar' | ends_with('bar')) }}
# => true

{{ 'foo' | ends_with('o')) }}
# => true

{{ 'foobar' | ends_with('bar'))}}
# => true

{{ '00018-0000062.Plone.sdh264.1a7264e6912a91aa4a81b64dc5517df7b8875994.mp4| ends_with('mp4'))}}
# => true
```

#### escape_html
###### method: escape_html(haystack)
> custom implementation / needs to be installed

Converts HTML special characters to their entity equivalents. This function supports cent, yen, euro, pound, lt, gt, copy, reg, quote, amp, apos.

```python
{{ '&lt;div&gt;Blah &amp; &quot;blah&quot; &amp; &#39;blah&#39;&lt;/div&gt;' | unescape_html }}
# => '<div>Blah & \"blah\" & 'blah'</div>'
```

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
