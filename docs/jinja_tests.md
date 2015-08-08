## List of Jinja Builtin Tests 

#### callable
###### method: callable(object)
> jinja built-in


Return whether the object is callable (i.e., some kind of function). Note that classes are callable, as are instances with a __call__() method.

```python
{{ range is callable }}
# => True 

{{ 42 is callable }}
# => False
```

#### defined
###### method: defined(value)
> jinja built-in


Return true if the variable is defined:

```python
{{ missing is defined }}
# => False

{{ true is defined }}
# => True
```

_See the -default- filter for a simple way to set undefined variables._

#### divisibleby
###### method: divisibleby(value, num)
> jinja built-in


Check if a variable is divisible by a number.

```python
# todo: check if it is correct
{{ 20 | divisibleby(5) }}
# => True
```

#### equalto
###### method: equalto(value, other)
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

#### escaped
###### method: escaped(value)
> jinja built-in


Check if the value is escaped.

```python
{{ 'foo' is escaped }
# => False
{{ '&lt;&#34;&gt;&amp;' is escaped }}
# => True
```

#### even
###### method: even(value)
> jinja built-in


Return true if the variable is even.

```python
{{ 1 is even }}
# => False

{{ 2 is even }}
# => True
```

#### iterable
###### method: iterable(value)
> jinja built-in


Check if it’s possible to iterate over an object.

```python
{{ range(5) is iterable }}
# => True

{{ 5 is iterable }}
# => False
```

#### lower
###### method: lower(value)
> jinja built-in


Return true if the variable is lowercased.

```python
{{ "foo" is lower }}
# => True

{{ "FOO" is lower }}
# => False
```

#### mapping
###### method: mapping(value)
> jinja built-in


Return true if the object is a mapping (dict etc.).

```python
{{ {} is mapping }}
# => True

{{ [] is mapping }}
# => False
```

_New in jinja version 2.6._

#### none
###### method: none(value)
> jinja built-in


Return true if the variable is none.

```python
{{ None is none }}
# => True

{{ 'foo' is none }}
# => False
```

#### number
###### method: number(value)
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

#### odd
###### method: odd(value)
> jinja built-in


Return true if the variable is odd.

```python
{{ 1 is odd }}
# => True

{{ 2 is odd }}
# => False
```

#### sameas
###### method: sameas(value, other)
> jinja built-in


Check if an object points to the same memory address than another object

```python
{{ False is sameas false }}
# => True

{{ 0 is sameas false }}
# => False
```

#### sequence
###### method: sequence(value) 
> jinja built-in


Return true if the variable is a sequence. Sequences are variables that are iterable.

```python
{{ "foo" is sequence }}
# => True

{{ [1] is sequence }}
# => True
```

#### string
###### method: string(value)
> jinja built-in


Return true if the object is a string.

```python
{{ 42 is string }}
# => False
{{ "foo" is string }}
# => True
```

#### undefined
###### method: undefined(value)
> jinja built-in


Like defined() but the other way round.

```python
{{ 42 is undefined }}
# => False

{{ missing is undefined }}
# => True
```

#### upper
###### method: upper(value)
> jinja built-in


Return true if the variable is uppercased.

```python
{{ "FOO" is upper }}
# => True

{{ "foo" is upper }}
# => False
```
