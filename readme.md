# TIpyAPL

an APL-like programming language designed to run on the TI-84 Plus CE Python

the source is pretty golfed and the lines are pretty short because I wrote most of it on the calculator itself! where you can only write 31 characters on a line before it wraps to the next one. the calculator runs Python 3.4 so it can't use new features. the device only gives python a very small amount of memory so it can't store lists larger than a few thousand numbers, and it can't load files longer than around a hundred and ten lines.

while tipyapl is designed for the calculator, you can also try the language on any platform with Python 3.4 or higher installed. just clone the repo and run `python3 A.py` to enter a REPL.

this project is still a work in progress. I'm writing it mostly to pass time in precalculus class.

the language runs from left to right. numeric literals can be entered with digits. you can make functions with curly braces `{body}`, where the left argument is X and the right argument is Y.

you can make arrays with the comma function `,`. passing two scalar values gives a list of two items. you can add a leading unit-axis to an array with the function `f`.

```
    1,2,3
1 2 3
    1,2,3f,(4,5,6)
1 2 3
4 5 6
    1,2,3f,(4,5,6)+1
2 3 4
5 6 7
```

(the name is a reference to [tinyapl](https://github.com/RubenVerg/tinyapl))
