# Tools

A set of useful and sometimes one use tools for Common Knowledge.

## `links.py`

Produces a list of links like this, adding the parameter `s=X` to the URL where
`X` is a number from one to fifty.

```
python3 links.py https://example.com
https://example.com&s=1
https://example.com&s=2
```

First argument is the link to extend.
