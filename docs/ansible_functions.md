## List of Ansible Built-in Functions 

#### b64encode
###### method: b64encode
> ansible built-in

Encode Strings with Base64

```python
{{ 'foo' | b64decode }}
# => 'Zm9v'
```

#### b64decode
###### method: b64decode
> ansible built-in

Decode Base64 encoded Strings

```python
{{ 'Zm9v' | b64encode }}
# => 'foo'
```

#### to_uuid
###### method: to_uuid
> ansible built-in

create a UUID from a string

```python
{{ 'hostname' | to_uuid }}
# => '333bb031-dca6-57ec-895a-259d66ca7c36'
```

_new in Ansible version 1.9_

#### to_json
###### method: to_json
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
###### method: to_nice_json
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
###### method: from_json
> ansible built-in

Reading in some JSON formatted data

[Here is an example](https://gist.github.com/lxhunter/45fb119c0128600158d8) 

#### to_yaml
###### method: to_yaml
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
###### method: to_nice_yaml
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
###### method: from_yaml
> ansible built-in

Reading in YAML formatted data

[Here is an example for JSON, just adapt it YAML](https://gist.github.com/lxhunter/45fb119c0128600158d8) 

#### bool
###### method: bool
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

#### quote
###### method: quote
> ansible built-in

Add quotes for shell usage

```python
#  using single quotes ' and escaping with two single quotes ''
'{{ ''{"a": 1, "b": 2}'' | quote }}'

# => '{\"a\": 1, \"b\": 2}'
```

#### hash
###### method: hash(data, hashtype='sha1')
> ansible built-in

Get the hash of a string

Options:
- 'md5'
- 'sha1'
- 'sha224'
- 'sha256'
- 'sha384'
- 'sha512'

Platform dependend:
- 'blowfish'

```python
{{ 'foo'|hash('md5') }}
# => acbd18db4cc2f85cedef654fccc4a4d8

{{ 'foo'|hash('sha1') }}
# => 0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33

{{ 'foo'|hash('sha224') }}
# => 0808f64e60d58979fcb676c96ec938270dea42445aeefcd3a4e6f8db

{{ 'foo'|hash('sha256') }}
# => 2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae

{{ 'foo'|hash('sha384') }}
# => 98c11ffdfdd540676b1a137cb1a22b2a70350c9a44171d6b1180c6be5cbb2ee3f79d532c8a1dd9ef2e8e08e752a3babb

{{ 'foo'|hash('sha512') }}
# => f7fbba6e0636f890e56fbbf3283e524c6fa3204ae298382d624741d0dc6638326e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7

{{ 'foo'|hash('blowfish') }}
# is platform dependend 
```

_New in ansible version 1.9._

#### checksum
###### method: checksum
> ansible built-in

Get a checksum for a string

```python
{{ 'foo'|checksum }}

# => 0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33
```

_New in ansible version 1.9._

#### password_hash
###### method: password_hash(password, hashtype='sha512', salt=None)
> ansible built-in

Get a password hash from a String

Options:
- 'md5'
- 'sha256'
- 'sha512'

Platform dependend:
- 'blowfish'

```python
{{ 'fooosecretbar'|password_hash('md5') }}
# => $1$QalF8sBf$uTmJo0xCVPBKrdEsAPjuV0

{{ 'fooosecretbar'|password_hash('sha256') }}
# => $5$SSkuLCmtvlQ2kT2I$2Y5F2gPPXXtNaSY5FrHhm8ggtBEcjuPODxHS1Lsvy31

{{ 'fooosecretbar'|password_hash('sha512') }}
# => $6$8XFFhlPGyfY3V9qm$.Rc4GnmfwO3y.RtfL9c.X6gtrh6rkE33KlfdI2u55RMa8aWYf/K6S/W2knO07EAndV.kADM1Fin75osI4oEtO1

{{ 'fooosecretbar'|password_hash('blowfish') }}
# => is platform dependend 
```

_New in ansible version 1.9._

#### regex_replace
###### method: regex_replace(value='', pattern='', replacement='', ignorecase=False)
> ansible built-in

Replace text in a string with a regex

_Caution: If “regex_replace” filter is used with variables inside YAML arguments (as opposed to simpler ‘key=value’ arguments), then you need to escape backreferences (e.g. \\1) with 4 backslashes (\\\\\\\\) instead of 2 (\\\\)._

```python
{{ 'ansible' | regex_replace('^a.*i(.*)$', 'a\\\\1') }}
# => able

{{ 'foobar' | regex_replace('^f.*o(.*)$', '\\\\1') }}
# => bar
```

_New in ansible version 1.6._

#### regex_escape
###### method: regex_escape
> ansible built-in

Escape special characters within a regex

```python
{{ '^f.*o(.*)$' | regex_escape() }}
# => \\^f\\.\\*o\\(\\.\\*\\)\\$
```

_New in ansible version 1.6._

#### ternary
###### method: ternary(value, true_val, false_val)

> ansible built-in

Use one value on true and another on false

```python
{{ True | ternary('true_case','false_case') }}
# => true_case

{{ False | ternary('true_case','false_case') }}
# => false_case
```

_New in ansible version 1.9._

#### version_compare
###### method: (value, version, operator='eq', strict=False)
> ansible built-in

To compare a version number

```python
{{ '12.04' | version_compare('12.04', '<') }}
# => False

{{ '12.03' | version_compare('12.04', '<') }}
# => True

{{ '12.05' | version_compare('12.04', '<') }}
# => False
```

_New in ansible version 1.6._

#### random
###### method: random(end, start=None, step=None))
> ansible built-in

This filter can be used similar to the default jinja2 random filter (returning a random item from a sequence of items), but can also generate a random number based on a range.

To get a random item from a list:

```python
{{ ['a','b','c']|random }}
# => c
```

To get a random number from 0 to supplied end:

```python
{{ 59 |random(step=10) }}
# => 35
```

Get a random number from 0 to 100 but in steps of 10:

```python
{{ 100 |random(step=10) }} 
# => 60
```

Get a random number from 1 to 100 in steps of 10:

```python
{{ 100 |random(1, 10) }}
# => 31

{{ 100 |random(start=1, step=10) }} 
# => 51
```

_New in ansible version 1.6._

#### shuffle
###### method: shuffle(list)
> ansible built-in

Randomize an existing list, giving a different order every invocation.

```python
{{ ['a','b','c']|shuffle }} 
# => ['c','a','b']

{{ ['a','b','c']|shuffle }} 
# => ['b','c','a']
```

_New in ansible version 1.8._

#### isnan
###### method: isnan(value)
> ansible built-in

To see if something is actually a number:

_caution: somehow the filter always returns false_

```python
{{ 1 | isnan }}
# => False

{{ 'foo' | isnan }}
# => False

{{ True | isnan }}
# => False

{{ False | isnan }}
# => False

{{ '1' | isnan }}
# => False

{{ None | isnan }}
# => False

```

_New in ansible version 1.9._

#### log
###### method: log(value, base=math.e)
> ansible built-in

Get the logarithm:

```python
{{ 50 | log }}
# => 3.91202300543
```

Get the base 10 logarithm:

```python
{{ 50 | log(10) }}
# => 1.69897000434
```

_New in ansible version 1.9._

#### pow
###### method: pow(value, y)
> ansible built-in

the power of n

```python
{{ 50 | pow(2) }}
# => 2500.0

{{ 50 | pow(5) }}
# => 312500000.0
```

_New in ansible version 1.9._

#### root
###### method: root(value, base=2)
> ansible built-in

Square root or root

```python
{{ myvar | root }}
# => 7.07106781187

{{ myvar | root(5) }}
# => 2.18672414789
```

_New in ansible version 1.9._

#### ipaddr
###### method:
> ansible built-in

_caution: needs python-netaddr_

To test if a string is a valid IP address

```python
{{ '192.168.0.1' | ipaddr }}
# => 192.168.0.1

{{ 50 | ipaddr }}
# => 0.0.0.50

{{ 'foo' | ipaddr }}
# => false

{{ '255.255.255.255' | ipaddr }}
# => 255.255.255.255

{{ '2001:0db8:85a3:08d3:1319:8a2e:0370:7344' | ipaddr }}
# => 2001:0db8:85a3:08d3:1319:8a2e:0370:7344
```

_New in ansible version 1.9._


#### ipv4
###### method: ipv4(value, query = '')
> ansible built-in

To test if a string is a valid IPv4 address

```python
{{ '192.168.0.1' | ipv4 }}
# => 192.168.0.1

{{ '2001:0db8:85a3:08d3:1319:8a2e:0370:7344' | ipv4 }}
# => False
```

_New in ansible version 1.9._

#### ipv6
###### method: ipv6(value, query = '')
> ansible built-in

To test if a string is a valid IPv6 address

```python
{{ '192.168.0.1' | ipv4 }}
# => False

{{ '2001:0db8:85a3:08d3:1319:8a2e:0370:7344' | ipv4 }}
# => 2001:0db8:85a3:08d3:1319:8a2e:0370:7344
```

_New in ansible version 1.9._
