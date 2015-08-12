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

Remove any common leading whitespace from every line in text.

This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form.

Note that tabs and spaces are both treated as whitespace, but they are not equal: the lines `  hello` and `\thello` are considered to have no common leading whitespace.

_Using Python Standard Library textwrap_

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











