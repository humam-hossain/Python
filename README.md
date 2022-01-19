# Notes on python .py

## Python Variable Scope

***Shortcut: LEGB***

Local > Enclosing > Global > Builtin

```python
#!/bin/python3

x = "global x"

def outer():
    x = "outer x"

    def inner():
        x = "inner x"
        print(x)
    
    inner()
    print(x)

outer()
print(x)
```
