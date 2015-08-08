
# Ansible Filters
#### WORK in PROGRESS

# Overview

### String Utilities
* [capitalize] (docs/jinja_functions.md#capitalize) - Capitalize a String.
* [center] (docs/jinja_functions.md#center) - Centers the value in a field of a given width.
* [escape] (docs/jinja_functions.md#escape) - Convert the chars to HTML-safe sequences.
* [filesizeformat] (docs/jinja_functions.md#filesizeformat) - Format file sizes into ‘human-readable’ 
* [forceescape] (docs/jinja_functions.md#forceescape) - Enforce HTML escaping.
* [format] (docs/jinja_functions.md#format) - Apply python string formatting on an object.
* [indent] (docs/jinja_functions.md#indent) - Indent a string.
* [list] (docs/jinja_functions.md#list) - Convert the value into a list.
* [lower] (docs/jinja_functions.md#lower) - Convert a value to lowercase.
* [quote] (docs/ansible_tests.md#quote) - Add quotes for shell usage
* [replace] (docs/jinja_functions.md#replace) - Search for needle in haystack and replace it with substitute.
* [string] (docs/jinja_functions.md#string) - Make a string unicode.
* [title] (docs/jinja_functions.md#title) - Return a titlecased version of the value.
* [trim] (docs/jinja_functions.md#trim) - Strip leading and trailing whitespace.
* [truncate] (docs/jinja_functions.md#truncate) - Return a truncated copy of the string.
* [upper] (docs/jinja_functions.md#upper) - Convert a value to uppercase.
* [urlencode] (docs/jinja_functions.md#urlencode) - Escape strings for use in URLs.
* [urlize] (docs/jinja_functions.md#urlize) - Converts URLs in plain text into clickable links.
* [wordcount] (docs/jinja_functions.md#wordcount) - Count the words in that string.
* [wordwrap] (docs/jinja_functions.md#wordwrap) - Return a copy of the string passed to the filter wrapped after n characters. 
* [xmlattr] (docs/jinja_functions.md#xmlattr) - Create an SGML/XML attribute string based on the items in a dict. 

### Number / Math Utilities 
* [abs] (docs/jinja_functions.md#abs) - Return the absolute value of the argument.
* [float] (docs/jinja_functions.md#float) - Convert the value into a floating point number.
* [int] (docs/jinja_functions.md#int) - Convert the value into an integer.
* [log] (docs/ansible_tests.md#log) - Get the logarithm
* [pow] (docs/ansible_tests.md#pow) - Get the power of
* [root] (docs/ansible_tests.md#root) - Square root or root
* [round] (docs/jinja_functions.md#round) - Round the number to a given precision.
* [sum] (docs/jinja_functions.md#sum) - Returns the sum of a sequence.

### Collection Utilities
* [batch] (docs/jinja_functions.md#batch) - A filter that batches items.
* [dictsort] (docs/jinja_functions.md#dictsort) - Sort a dict and yield (key, value) pairs.
* [first] (docs/jinja_functions.md#first) - Return the first item of a sequence.
* [groupby] (docs/jinja_functions.md#groupby) - Group a sequence of objects by a common attribute.
* [join] (docs/jinja_functions.md#join) - Return a string which is the concatenation of the strings in the sequence.
* [last] (docs/jinja_functions.md#last) - Return the last item of a sequence.
* [length] (docs/jinja_functions.md#length) - Return the number of items of a sequence or mapping.
* [map] (docs/jinja_functions.md#map) - Applies a filter on a sequence of objects or looks up an attribute.
* [random] (docs/jinja_functions.md#random) - Return a random item from the sequence.
* [reject] (docs/jinja_functions.md#reject) - Filters a sequence of objects by applying a test to the object and rejecting the ones with the test succeeding.
* [select] (docs/jinja_functions.md#select) - Filters a sequence of objects by applying a test to the object and only selecting the ones with the test succeeding.
* [shuffle] (#shuffle) - Randomize an existing list, giving a different order every invocation.
* [slice] (docs/jinja_functions.md#slice) - Filters a sequence of objects by applying a test to the object and only selecting the ones with the test succeeding.
* [sort] (docs/jinja_functions.md#sort) - Sort an iterable.

### Hashing Utilities
* [checksum] (docs/ansible_tests.md#checksum) - Get a checksum for a string
* [hash] (docs/ansible_tests.md#hash) - Get the hash (md5, sha1, sha224, sha256, sha384, sha512) of a string
* [password_hash] (docs/ansible_tests.md#password_hash) - Get a password hash (md5, sha256, sha512) for a string

### Object Utilities
* [attr] (docs/jinja_functions.md#attr) - Get an attribute of an object.
* [rejectattr] (docs/jinja_functions.md#rejectattr) - Filters a sequence of objects by applying a test to an attribute of an object or the attribute and rejecting the ones with the test succeeding.
* [selectattr] (docs/jinja_functions.md#selectattr) - Slice an iterator and return a list of lists containing those items.

### Helper Utilities
* [b64decode] (docs/ansible_tests.md#b64decode) - Decode a Base64 encoded string.
* [b64encode] (docs/ansible_tests.md#b64encode) - Encode a string use Base64.
* [default] (docs/jinja_functions.md#default) - Set a default value
* [from_json] (docs/ansible_tests.md#from_json) - Reading in some JSON formatted data
* [from_yaml] (docs/ansible_tests.md#from_yaml) - Reading in YAML formatted data
* [pprint] (docs/jinja_functions.md#pprint) - Pretty print a variable.
* [regex_escape] (docs/ansible_tests.md#regex_escape) - Escape special characters within a regex
* [regex_replace] (docs/ansible_tests.md#regex_replace) - Replace text in a string with a regex
* [reverse] (docs/jinja_functions.md#reverse) - Reverse the object or return an iterator that iterates over it the other way round.
* [safe] (docs/jinja_functions.md#safe) - Make all potentionally dangerous chars safe. - safety is a illusion, so beware!
* [striptags] (docs/jinja_functions.md#striptags) - Strip SGML/XML tags and replace adjacent whitespace by one space.
* [ternary] (docs/ansible_tests.md#ternary) - Use one value on true and another on false
* [to_json] (docs/ansible_tests.md#to_json) - Convert value into JSON
* [to_nice_json] (docs/ansible_tests.md#to_nice_json) - Convert string into human readable JSON
* [to_nice_yaml] (docs/ansible_tests.md#to_nice_yaml) - Convert value into human readable YAML
* [to_uuid] (docs/ansible_tests.md#to_uuid) - Create a UUID from a string
* [to_yaml] (docs/ansible_tests.md#to_yaml) - Convert value into YAML
* [version_compare] (docs/ansible_tests.md#version_compare) - To compare a version number

### Tests
* [bool] (docs/ansible_tests.md#bool) - Check if the value is a boolean
* [callable] (docs/jinja_tests.md#callable) - Return whether the object is callable
* [defined] (docs/jinja_tests.md#defined) - Return true if the variable is defined
* [divisibleby] (docs/jinja_tests.md#divisibleby) - Check if a variable is divisible by a number.
* [equalto] (docs/jinja_tests.md#equalto) - Check if an object has the same value as another object.
* [escaped] (docs/jinja_tests.md#escaped) - Check if the value is escaped.
* [even] (docs/jinja_tests.md#even) - Return true if the variable is even.
* [isnan] (docs/ansible_tests.md#isnan) - To see if something is actually a number
* [iterable] (docs/jinja_tests.md#iterable) - Check if it’s possible to iterate over an object.
* [lower] (docs/jinja_tests.md#lower) - Return true if the variable is lowercased.
* [mapping] (docs/jinja_tests.md#mapping) - Return true if the object is a mapping (dict etc.).
* [none] (docs/jinja_tests.md#none) - Return true if the variable is none.
* [number] (docs/jinja_tests.md#number) - Return true if the variable is a number.
* [odd] (docs/jinja_tests.md#odd) - Return true if the variable is odd.
* [sameas] (docs/jinja_tests.md#sameas) - Check if an object points to the same memory address than another object.
* [sequence] (docs/jinja_tests.md#sequence) - Return true if the variable is a sequence.
* [string] (docs/jinja_tests.md#string) - Return true if the object is a string.
* [undefined] (docs/jinja_tests.md#undefined) - Like defined() but the other way round.
* [upper] (docs/jinja_tests.md#upper) - Return true if the variable is uppercased.


# Testing

```shell
python -m unittest -v string_utils
nodemon -e 'py' --exec "python -m unittest -v string_utils"
```
