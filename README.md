
# Ansible Filters
#### WORK in PROGRESS

# Overview

### String Utilities
* [capitalize] (#capitalizestring) - Capitalize a String.
* [center] (#centervalue-width80) - Centers the value in a field of a given width.
* [filesizeformat] (#filesizeformatnumber-binaryfalse) - Format file sizes into ‘human-readable’ 
* [escape] (#escapestring) - Convert the chars to HTML-safe sequences.
* [forceescape] (#forceescapestring--string) - Enforce HTML escaping.
* [format] (#formatstring-args-kwargs--string) - Apply python string formatting on an object.
* [indent] (#indentstring-width4-indentfirstfalse) - Indent a string.
* [list] (#listvalue) - Convert the value into a list.
* [lower] (#lowerstring) - Convert a value to lowercase.
* [replace] (#replacehaystack-neddle-substitute-countnone) - Search for needle in haystack and replace it with substitute.
* [string] (#stringobject) - Make a string unicode.
* [title] (#titlestring) - Return a titlecased version of the value.
* [trim] (#trimvalue) - Strip leading and trailing whitespace.
* [truncate] (#truncatestring-length255-killwordsfalse-end) - Return a truncated copy of the string.
* [upper] (#upperstring) - Convert a value to uppercase.
* [urlencode] (#urlencodevalue) - Escape strings for use in URLs.
* [urlize] (#urlizevalue-trim_url_limitnone-nofollowfalse-targetnone) - Converts URLs in plain text into clickable links.
* [wordcount] (#wordcountstring) - Count the words in that string.
* [wordwrap] (#wordwrapstring-width79-break_long_wordstrue-wrapstringnone) - Return a copy of the string passed to the filter wrapped after n characters. 
* [xmlattr] (#xmlattrdict-autospacetrue) - Create an SGML/XML attribute string based on the items in a dict. 

### Number Utilities 
* [abs] (#absnumber) - Return the absolute value of the argument.
* [float] (#floatstring-default00--string) - Convert the value into a floating point number.
* [int] (#intvalue-default0-base10) - Convert the value into an integer.
* [round] (#roundvalue-precision0-methodcommon) - Round the number to a given precision.
* [sum] (#sumiterable-attributenone-start0) - Returns the sum of a sequence.

### Collection Utilities
* [batch] (#batchsequence-linecount-fill_withnone) - A filter that batches items.
* [dictsort] (#dictsortdict-case_sensitivefalse-bykey) - Sort a dict and yield (key, value) pairs.
* [first] (#firstsequence) - Return the first item of a sequence.
* [groupby] (#groupbyvalue-attribute) - Group a sequence of objects by a common attribute.
* [join] (#joinvalue-delimiter-attributenone) - Return a string which is the concatenation of the strings in the sequence.
* [last] (#lastsequence) - Return the last item of a sequence.
* [length] (#lengthobject) - Return the number of items of a sequence or mapping.
* [map] (#map--list) - Applies a filter on a sequence of objects or looks up an attribute.
* [random] (#randomsequence) - Return a random item from the sequence.
* [reject] (#reject) - Filters a sequence of objects by applying a test to the object and rejecting the ones with the test succeeding.
* [rejectattr] (#rejectattr) - Filters a sequence of objects by applying a test to an attribute of an object or the attribute and rejecting the ones with the test succeeding.
* [select] (#select) - Filters a sequence of objects by applying a test to the object and only selecting the ones with the test succeeding.
* [slice] (#slicevalue-slices-fill_withnone) - Filters a sequence of objects by applying a test to the object and only selecting the ones with the test succeeding.
* [sort] (#sortvalue-reversefalse-case_sensitivefalse-attributenone) - Sort an iterable.

### Object Utilities
* [attr] (#attrobj-name) - Get an attribute of an object.
* [selectattr] (#selectattr) - Slice an iterator and return a list of lists containing those items.

### Helper Utilities
* [default] (#defaultvalue-default_valueu-booleanfalse) - Set a default value
* [pprint] (#pprintvalue-verbosefalse) - Pretty print a variable.
* [reverse] (#reversevalue) - Reverse the object or return an iterator that iterates over it the other way round.
* [safe] (#safevalue) - Make all potentionally dangerous chars safe. - safety is a illusion, so beware!
* [striptags] (#striptagsvalue) - Strip SGML/XML tags and replace adjacent whitespace by one space.

### Tests
* [callable] (#callableobject) - Return whether the object is callable
* [defined] (#definedvalue) - Return true if the variable is defined
* [divisibleby] (#divisiblebyvalue-num) - Check if a variable is divisible by a number.
* [equalto] (#equaltovalue-other) - Check if an object has the same value as another object.
* [escaped] (#escapedvalue) - Check if the value is escaped.
* [even] (#evenvalue) - Return true if the variable is even.
* [iterable] (#iterablevalue) - Check if it’s possible to iterate over an object.
* [lower] (#lowervalue) - Return true if the variable is lowercased.
* [mapping] (#mappingvalue) - Return true if the object is a mapping (dict etc.).
* [none] (#nonevalue) - Return true if the variable is none.
* [number] (#numbervalue) - Return true if the variable is a number.
* [odd] (#oddvalue) - Return true if the variable is odd.
* [sameas] (#sameasvalue-other) - Check if an object points to the same memory address than another object.
* [sequence] (#sequencevalue) - Return true if the variable is a sequence.
* [string] (#stringvalue) - Return true if the object is a string.
* [undefined] (#undefinedvalue) - Like defined() but the other way round.
* [upper] (#uppervalue) - Return true if the variable is uppercased.

## Jinja List of Builtin Functions 

#### abs(number)
> jinja built-in

Return the absolute value of the argument. 

```python
{{ -1|abs }}|{{ 1|abs }} 
# => 1
```

#### attr(obj, name) 
> jinja built-in


Get an attribute of an object. foo|attr("bar") works like foo.bar just that always an attribute is returned and items are not looked up.

```python
{{ foo|attr('bar') }} 
# => 'quux'
```

#### batch(sequence, linecount, fill_with=None) 
> jinja built-in


A filter that batches items. It works pretty much like slice just the other way round. It returns a list of lists with the given number of items. If you provide a second parameter this is used to fill up missing items. 

```python
{{ foo|batch(3)|list }} 
# => [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

{{ foo|batch(3, 'X')|list }} 
# => [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 'X', 'X']]
```

#### capitalize(string)
> jinja built-in


Capitalize a string. The first character will be uppercase, all others lowercase.

```python
{{ "foo bar"|capitalize }} 
# => 'Foo bar'
```

#### center(value, width=80)
> jinja built-in


Centers the value in a field of a given width.

```python
{{ "foo"|center(9) }} 
# => '   foo   '
```

#### default(value, default_value=u'', boolean=False)
> jinja built-in

_aliases_: d

If the value is undefined it will return the passed default value, otherwise the value of the variable

```python
{{ missing|default('no') }}
# => 'no'

{{ false|default('no') }} 
# => 'false'

{{ false|default('no', true) }} 
# => 'no'

{{ given|default('no') }} 
# => 'yes'
```

#### dictsort(dict, case_sensitive=False, by='key')
> jinja built-in


Sort a dict and yield (key, value) pairs. Because python dicts are unsorted you may want to use this function to order them by either key or value

```python
{{ {"aa": 0, "b": 1, "c": 2, "AB": 3}|dictsort }} 
# => [('aa', 0), ('AB', 3), ('b', 1), ('c', 2)]

{{ {"aa": 0, "b": 1, "c": 2, "AB": 3}|dictsort(true) }} 
# => [('AB', 3), ('aa', 0), ('b', 1), ('c', 2)]

{{ {"aa": 0, "b": 1, "c": 2, "AB": 3}|dictsort(false, "value") }} 
# => [('aa', 0), ('b', 1), ('c', 2), ('AB', 3)]
```

#### escape(string)
> jinja built-in

_aliases_: e

Convert the characters &, <, >, ‘, and ” in string s to HTML-safe sequences. Use this if you need to display text that might contain such characters in HTML. Marks return value as markup string.

```python
{{ '<">&'|escape }}
# => '&lt;&#34;&gt;&amp;'
```

#### filesizeformat(number, binary=False)
> jinja built-in


Format the value like a ‘human-readable’ file size (i.e. 13 kB, 4.1 MB, 102 Bytes, etc). Per default decimal prefixes are used (Mega, Giga, etc.), if the second parameter is set to True the binary prefixes are used (Mebi, Gibi).

```python
{{ 100|filesizeformat }}
# => 100 Bytes

{{ 1000|filesizeformat }}
# => 1.0 kB

{{ 1000000|filesizeformat }}
# => 1.0 MB

{{ 1000000000|filesizeformat }}
# => 1.0 GB

{{ 1000000000000|filesizeformat }}
# => 1.0 TB

{{ 100|filesizeformat(true) }}
# => 100 Bytes

{{ 1000|filesizeformat(true) }}
# => 1000 Bytes

{{ 1000000|filesizeformat(true) }}
# => 976.6 KiB

{{ 1000000000|filesizeformat(true) }}
# => 953.7 MiB

{{ 1000000000000|filesizeformat(true) }}
# => 931.3 GiB
```

#### first(sequence)
> jinja built-in


Return the first item of a sequence.

```python
{{ list(range(10))|first }}
# => 0
```

#### float(string, default=0.0) => string
> jinja built-in


Convert the value into a floating point number. If the conversion doesn’t work it will return 0.0. You can override this default using the first parameter.

```python
{{ "42"|float }}
# => 42.0

{{ "ajsghasjgd"|float }}
# => 0.0

{{ "32.32"|float }}
# => 32.32
```

#### forceescape(string) => string
> jinja built-in


Enforce HTML escaping. This will probably double escape variables.

```python
{{ '<div />'|forceescape }}
# => '&lt;div /&gt;'
```

#### format(string, *args, **kwargs) => string
> jinja built-in


Apply python string formatting on an object:

```python
{{ "%s - %s"|format("Hello?", "Foo!") }}
# => Hello? - Foo!
```

#### groupby(value, attribute)
> jinja built-in


Group a sequence of objects by a common attribute. 

```python
[{'foo': 1, 'bar': 2},{'foo': 2, 'bar': 3},{'foo': 1, 'bar': 1},{'foo': 3, 'bar': 4}]|groupby('foo')
# => "1: 1, 2: 1, 1|2: 2, 3|3: 3, 4|"

[('a', 1), ('a', 2), ('b', 1)]|groupby(0)
# => 'a:1:2|b:1|'
```

#### indent(string, width=4, indentfirst=False)
> jinja built-in


Return a copy of the passed string, each line indented by 4 spaces. The first line is not indented. If you want to change the number of spaces or indent the first line too you can pass additional parameters to the filter

```python
{{ 'indent by two spaces and indent the first line too.'|indent(2, true) }}
# => '  indent by two spaces and indent the first line too.'
```

#### int(value, default=0, base=10)
> jinja built-in


Convert the value into an integer. If the conversion doesn’t work it will return 0. You can override this default using the first parameter. You can also override the default base (10) in the second parameter, which handles input with prefixes such as 0b, 0o and 0x for bases 2, 8 and 16 respectively.

```python
{{ "42"|int }}
# => 42

{{ "ajsghasjgd"|int }}
# => 0

{{ "32.32"|int }}
# => 32

{{ "0x4d32"|int(0, 16) }}
# => 19762

{{ "011"|int(0, 8)}}
# => 9

{{ "0x33FU"|int(0, 16) }}
# => 0
```

#### join(value, delimiter='', attribute=None)
> jinja built-in


Return a string which is the concatenation of the strings in the sequence. The separator between elements is an empty string per default, you can define it with the optional parameter. It is also possible to join certain attributes of an object

```python
{{ [1, 2, 3]|join('|') }}
# => 1|2|3

{{ [1, 2, 3]|join }}
# => 123

{{ map(User, ['foo', 'bar']))|join(', ', attribute='username') }}
# => 'foo, bar'
```

#### last(sequence)
> jinja built-in


Return the last item of a sequence.

```python
{{ list(range(10))|last }}
# => 9
```

#### length(object)
> jinja built-in

_aliases_: count

Return the number of items of a sequence or mapping.

```python
{{ "hello world"|length }}
# => 11
```

#### list(value)
> jinja built-in


Convert the value into a list. If it was a string the returned list will be a list of characters.

```python
{{ "hello"|list }}
# => ['H', 'e', 'l', 'l', 'o']
```

#### lower(string)
> jinja built-in


Convert a value to lowercase.

```python
{{ "FOO"|lower }}
# => 'foo'
```

#### map() => list
> jinja built-in

Applies a filter on a sequence of objects or looks up an attribute. This is useful when dealing with lists of objects but you are really only interested in a certain value of it.

The basic usage is mapping on an attribute. Imagine you have a list of users but you are only interested in a list of usernames:

```python
{{ [User('john'), User('jane'), User('mike')]|map(attribute="name")|join(",") }}
# => 'john,jane,mike'
```

Alternatively you can let it invoke a filter by passing the name of the filter and the arguments afterwards. A good example would be applying a text conversion filter on a sequence:

```python
{{ ['John', 'Jane', 'Mike']| map('lower') | join(', ') }}
# => 'john, jane, mike'
```

_New in jinja version 2.7._


#### pprint(value, verbose=False)
> jinja built-in

Pretty print a variable. Useful for debugging.

With Jinja 1.2 onwards you can pass it a parameter. If this parameter is truthy the output will be more verbose (this requires pretty)

```python
{{[(0, {'a': 'A', 'c': 'C', 'b': 'B', 'e': 'E', 'd': 'D', 'g': 'G', 'f': 'F', 'h': 'H'}), (1, {'a': 'A', 'c': 'C', 'b': 'B', 'e': 'E', 'd': 'D', 'g': 'G', 'f': 'F', 'h': 'H'}), (2, {'a': 'A', 'c': 'C', 'b': 'B', 'e': 'E', 'd': 'D', 'g': 'G', 'f': 'F', 'h': 'H'})] | pprint }}
# => [(0,
#  {'a': 'A',
#   'b': 'B',
#   'c': 'C',
#   'd': 'D',
#   'e': 'E',
#   'f': 'F',
#   'g': 'G',
#   'h': 'H'}),
# (1,
#  {'a': 'A',
#   'b': 'B',
#   'c': 'C',
#   'd': 'D',
#   'e': 'E',
#   'f': 'F',
#   'g': 'G',
#   'h': 'H'}),
# (2,
#  {'a': 'A',
#   'b': 'B',
#   'c': 'C',
#   'd': 'D',
#   'e': 'E',
#   'f': 'F',
#   'g': 'G',
#   'h': 'H'})]
```

#### random(sequence)
> jinja built-in


Return a random item from the sequence.

```python
{{ ['John', 'Jane', 'Mike'] | random }}
# => 'Jane'

{{ ['John', 'Jane', 'Mike'] | random }}
# => 'Mike'
```

#### reject()
> jinja built-in


Filters a sequence of objects by applying a test to the object and rejecting the ones with the test succeeding.

```python
{{ [1, 2, 3, 4, 5]|reject("odd")|join("|") }}
# => '2|4'
```

_New in jinja version 2.7._

#### rejectattr()
> jinja built-in


Filters a sequence of objects by applying a test to an attribute of an object or the attribute and rejecting the ones with the test succeeding.

```python
{{ [User('john', True), User('jane', True), User('mike', False)]|rejectattr("is_active")|map(attribute="name") }}
# => 'mike'
```

_New in jinja version 2.7._

#### replace(haystack, neddle, substitute, count=None)
> jinja built-in


Return a copy of the value with all occurrences of a substring replaced with a new one. The first argument is the substring that should be replaced, the second is the replacement string. If the optional third argument count is given, only the first count occurrences are replaced:

```python
{{ "Hello World"|replace("Hello", "Goodbye") }}
# => Goodbye World

{{ "aaaaargh"|replace("a", "d'oh, ", 2) }}
# => d'oh, d'oh, aaargh

```

#### reverse(value)
> jinja built-in


Reverse the object or return an iterator that iterates over it the other way round.

```python
{{ "foobar"|reverse|join }} | {{ [1, 2, 3]|reverse|list }}
# => 'raboof|[3, 2, 1]'
```

#### round(value, precision=0, method='common')
> jinja built-in


Round the number to a given precision. The first parameter specifies the precision (default is 0), the second the rounding method:

* 'common' rounds either up or down
* 'ceil' always rounds up
* 'floor' always rounds down

If you don’t specify a method 'common' is used.

```python
{{ 42.55|round }}
# => 43.0

{{ 42.55|round(1, 'floor') }}
# => 42.5
```

Note that even if rounded to 0 precision, a float is returned. If you need a real integer, pipe it through int:

```python
{{ 42.55|round|int }}
# => 43
```

#### safe(value)
> jinja built-in


Mark the value as safe which means that in an environment with automatic escaping enabled this variable will not be escaped.

```python
{{ "<div>foo</div>"|safe }}
# => '<div>foo</div>'

{{ "<div>foo</div>" }}
# => '&lt;div&gt;foo&lt;/div&gt;'

```

#### select()
> jinja built-in


Filters a sequence of objects by applying a test to the object and only selecting the ones with the test succeeding.

```python
{{ [1, 2, 3, 4, 5]|select("odd")|join("|") }}
# => '1|3|5'
```

_New in jinja version 2.7._

#### selectattr()
> jinja built-in


Filters a sequence of objects by applying a test to an attribute of an object and only selecting the ones with the test succeeding.

```python
{{ [User('john', True), User('jane', True), User('mike', False)]|selectattr("is_active")|map(attribute="name") }}
# => 'john|jane'
```
_New in jinja version 2.7._

#### slice(value, slices, fill_with=None)
> jinja built-in


Slice an iterator and return a list of lists containing those items. 

```python
{{ list(range(10))|slice(3)|list }}
# => [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]

{{ list(range(10))|slice(3, "X")|list }}
# => [[0, 1, 2, 3], [4, 5, 6, 'X'], [7, 8, 9, 'X']]
```

If you pass it a second argument it’s used to fill missing values on the last iteration.

#### sort(value, reverse=False, case_sensitive=False, attribute=None)
> jinja built-in


Sort an iterable. Per default it sorts ascending, if you pass it true as first argument it will reverse the sorting.

If the iterable is made of strings the third parameter can be used to control the case sensitiveness of the comparison which is disabled by default.

```python
{{ [2, 3, 1]|sort }}
# => [1, 2, 3]

{{ [2, 3, 1]|sort(true) }}
# => [3, 2, 1]

{{ "".join(["c", "A", "b", "D"]|sort) }}
# => 'AbcD'

{{ ['foo', 'Bar', 'blah']|sort }}
# => "['Bar', 'blah', 'foo']"
```
_Changed in jinja version 2.6: The attribute parameter was added._

#### string(object)
> jinja built-in


Make a string unicode if it isn’t already. That way a markup string is not converted back to unicode.

```python
{{ [1, 2, 3, 4, 5]|string }}
# => '12345'
```

#### striptags(value)
> jinja built-in


Strip SGML/XML tags and replace adjacent whitespace by one space.

```python
{{ '<p>just a small   \n <a href="#">example</a> link</p>\n<p>to a webpage</p><!-- <p>and some commented stuff</p> -->|striptags }}
# => 'just a small example link to a webpage'
```

#### sum(iterable, attribute=None, start=0)
> jinja built-in


Returns the sum of a sequence of numbers plus the value of parameter ‘start’ (which defaults to 0). When the sequence is empty it returns start.

It is also possible to sum up only certain attributes:

```python
{{ [1, 2, 3, 4, 5, 6]|sum }}
# => '21'
```

_Changed in version 2.6: The attribute parameter was added to allow suming up over attributes. Also the start parameter was moved on to the right._

#### title(string)
> jinja built-in


Return a titlecased version of the value. I.e. words will start with uppercase letters, all remaining characters are lowercase.

```python
{{ "foo bar"|title }}
# => "Foo Bar"

{{ "foo's bar"|title }}
# => Foo's Bar"

{{ "foo   bar"|title }}
# => "Foo   Bar"

{{ "f bar f"|title }}
# => "F Bar F"

{{ "foo-bar"|title }}
# => "Foo-Bar"

{{ "foo\tbar"|title }}
# => "Foo\tBar"

{{ "FOO\tBAR"|title }}
# => "Foo\tBar"
```

#### trim(value)
> jinja built-in


Strip leading and trailing whitespace.

```python
{{ "  foo bar"|trim }}
# => "foo bar"

{{ "  foo bar  "|trim }}
# => "foo bar"

{{ "foo bar  "|trim }}
# => "foo bar"
```

#### truncate(string, length=255, killwords=False, end='...')
> jinja built-in


Return a truncated copy of the string. The length is specified with the first parameter which defaults to 255. If the second parameter is true the filter will cut the text at length. Otherwise it will discard the last word. If the text was in fact truncated it will append an ellipsis sign ("..."). If you want a different ellipsis sign than "..." you can specify it using the third parameter.

```python
{{ "foo bar baz"|truncate(9) }}
# => "foo ..."

{{ "foo bar baz"|truncate(9, True) }}
# => "foo ba..."
```

#### upper(string)
> jinja built-in


Convert a value to uppercase.

```python
{{ "foo"|upper }}
# => "FOO"
```

#### urlencode(value)
> jinja built-in


Escape strings for use in URLs (uses UTF-8 encoding). It accepts both dictionaries and regular strings as well as pairwise iterables.

```python
{{ "Hello, world!"|urlencode }}
# => 'Hello%2C%20world%21'

{{ "Hello, world\u203d"|urlencode }}
# => "Hello%2C%20world%E2%80%BD"

{{ ("f", 1),)"|urlencode }}
# => "f=1"

{{ (('f', 1), ("z", 2)) |urlencode }}
# => "f=1&amp;z=2"
```

_New in version 2.7._

#### urlize(value, trim_url_limit=None, nofollow=False, target=None)
> jinja built-in


Converts URLs in plain text into clickable links.

If you pass the filter an additional integer it will shorten the urls to that number. Also a third argument exists that makes the urls “nofollow”:

```python
{{ "foo http://www.example.com/ bar"|urlize }}
# => 'foo <a href="http://www.example.com/">http://www.example.com/</a> bar'

 '{{ "foo http://www.example.com/ bar"|urlize(target="_blank") }}'
# => 'foo <a href="http://www.example.com/" target="_blank">http://www.example.com/</a> bar'
```

_Changed in version 2.8+: The target parameter was added._

#### wordcount(string)
> jinja built-in


Count the words in that string.

```python
{{ "foo bar baz"|wordcount }}
# => 3
```

#### wordwrap(string, width=79, break_long_words=True, wrapstring=None)
> jinja built-in


Return a copy of the string passed to the filter wrapped after 79 characters. You can override this default using the first parameter. If you set the second parameter to false Jinja will not split words apart if they are longer than width. By default, the newlines will be the default newlines for the environment, but this can be changed using the wrapstring keyword argument.

```python
# todo: supply example?
```

_New in version 2.7: Added support for the wrapstring parameter._

#### xmlattr(dict, autospace=True)
> jinja built-in


Create an SGML/XML attribute string based on the items in a dict. All values that are neither none nor undefined are automatically escaped:

```python
{{ {'class': 'my_list', 'missing': none, 'id': 'list-%d'|format('42')}|xmlattr }}
# => class="my_list" id="list-42"
```

## List of Jinja Builtin Tests 

#### callable(object)
> jinja built-in


Return whether the object is callable (i.e., some kind of function). Note that classes are callable, as are instances with a __call__() method.

```python
{{ range is callable }}
# => True 

{{ 42 is callable }}
# => False
```

#### defined(value)
> jinja built-in


Return true if the variable is defined:

```python
{{ missing is defined }}
# => False

{{ true is defined }}
# => True
```

_See the -default- filter for a simple way to set undefined variables._

#### divisibleby(value, num)
> jinja built-in


Check if a variable is divisible by a number.

```python
# todo: check if it is correct
{{ 20 | divisibleby(5) }}
# => True
```

#### equalto(value, other)
> jinja built-in


Check if an object has the same value as another object:

```python
{{ foo is equalto 12 }}
# => True

{{ foo is equalto 0 }}
# => False

{{ foo is equalto (3 * 4) }}
# => True

{{ bar is equalto "baz" }}
# => True

{{ bar is equalto "zab" }}
# => False

{{ bar is equalto ("ba" + "z") }}
# => True

{{ bar is equalto bar }}
# => True

{{ bar is equalto foo }}
# => False
```

This appears to be a useless test as it does exactly the same as the == operator, but it can be useful when used together with the selectattr function:

{{ users|selectattr("email", "equalto", "foo@bar.invalid") }}

_New in jinja version 2.8._

#### escaped(value)
> jinja built-in


Check if the value is escaped.

```python
{{ 'foo' is escaped }
# => False
{{ '&lt;&#34;&gt;&amp;' is escaped }}
# => True
```

#### even(value)
> jinja built-in


Return true if the variable is even.

```python
{{ 1 is even }}
# => False

{{ 2 is even }}
# => True
```

#### iterable(value)
> jinja built-in


Check if it’s possible to iterate over an object.

```python
{{ range(5) is iterable }}
# => True

{{ 5 is iterable }}
# => False
```

#### lower(value)
> jinja built-in


Return true if the variable is lowercased.

```python
{{ "foo" is lower }}
# => True

{{ "FOO" is lower }}
# => False
```

#### mapping(value)
> jinja built-in


Return true if the object is a mapping (dict etc.).

```python
{{ {} is mapping }}
# => True

{{ [] is mapping }}
# => False
```

_New in jinja version 2.6._

#### none(value)
> jinja built-in


Return true if the variable is none.

```python
{{ None is none }}
# => True

{{ 'foo' is none }}
# => False
```

#### number(value)
> jinja built-in


Return true if the variable is a number.

```python
{{ 42 is number }}
# => True

{{ (10 ** 100) is number }}
# => True

{{ 3.14159 is number }}
# => True

{{ complex(1,2) is number }}
# => True
```

#### odd(value)
> jinja built-in


Return true if the variable is odd.

```python
{{ 1 is odd }}
# => True

{{ 2 is odd }}
# => False
```

#### sameas(value, other)
> jinja built-in


Check if an object points to the same memory address than another object

```python
{{ False is sameas false }}
# => True

{{ 0 is sameas false }}
# => False
```

#### sequence(value) 
> jinja built-in


Return true if the variable is a sequence. Sequences are variables that are iterable.

```python
{{ "foo" is sequence }}
# => True

{{ [1] is sequence }}
# => True
```

#### string(value)
> jinja built-in


Return true if the object is a string.

```python
{{ 42 is string }}
# => False
{{ "foo" is string }}
# => True
```

#### undefined(value)
> jinja built-in


Like defined() but the other way round.

```python
{{ 42 is undefined }}
# => False

{{ missing is undefined }}
# => True
```

#### upper(value)
> jinja built-in


Return true if the variable is uppercased.

```python
{{ "FOO" is upper }}
# => True

{{ "foo" is upper }}
# => False
```

## List of Ansible Built-in Functions 

#### b64encode
> ansible built-in

Encode Strings with Base64

```python
{{ 'foo' | b64decode }}
# => 'Zm9v'
```

#### b64decode
> ansible built-in

Decode Base64 encoded Strings

```python
{{ 'Zm9v' | b64encode }}
# => 'foo'
```

#### to_uuid
> ansible built-in

create a UUID from a string

```python
{{ 'hostname' | to_uuid }}
# => '333bb031-dca6-57ec-895a-259d66ca7c36'
```

_new in Ansible version 1.9_

#### to_json
> ansible built-in

Convert value into JSON

```python
# vars:
#   users:
#     - bob
#     - joe

{{ users | to_json }}
# => ["bob","joe"]
```

#### to_nice_json
> ansible built-in

Convert string into human readable JSON

```python
# vars:
#   users:
#     - bob
#     - joe

{{ users | to_nice_json }}
# => [
#   "bob",
#   "joe"
# ]
```

#### from_json
> ansible built-in

Reading in some JSON formatted data

[Here is an example](https://gist.github.com/lxhunter/45fb119c0128600158d8) 

#### to_yaml
> ansible built-in

Convert value into YAML

```python
# vars:
#   users:
#     - bob
#     - joe

{{ users | to_yaml }}
# => ["bob","joe"]
```

#### to_nice_yaml
> ansible built-in

Convert value into human readable YAML

```python
# vars:
#   users:
#     - bob
#     - joe  

{{ users | to_nice_yaml }}
# => - bob
#    - joe
```

#### from_yaml
> ansible built-in

Reading in YAML formatted data

[Here is an example for JSON, just adapt it YAML](https://gist.github.com/lxhunter/45fb119c0128600158d8) 

#### bool
> ansible built-in

Check if the value is a boolean

```python
{{ True | bool }}
# => True

{{ 'True' | bool }}
# => True

{{ 1 | bool }}
# => True

{{ False | bool }}
# => False

{{ 'False' | bool }}
# => False

{{ 0 | bool }}
# => False
```

_version_

#### quote
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### md5
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### sha1
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### checksum
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### password_hash
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### hash
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### fileglob
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### regex_replace
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### regex_escape
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### ternary
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### version_compare
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### random
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

#### shuffle
> ansible built-in

_aliases:_

desc

```python

# =>
```

_version_

# Testing

```shell
python -m unittest -v string_utils
nodemon -e 'py' --exec "python -m unittest -v string_utils"
```
