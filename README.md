# CFGCal
Calculate given Context Free Grammar variable along with rule set


# Rule set File
The rule set file contains lines starting with a variable shown in a capital English letter.
the yielding is shown by the notation : ->
for example:
A -> c
means A yields c.
each line can have variables yielding one or more items. e.g:
B -> C | #
means B yields C or #.
example rules.txt file:

``` txt
A -> 0A1
A -> #
```
this grammar eventually makes {0^n#1^n | n>=0 }

we can show \epsilon or null terminal putting nothing:
``` txt
S -> (S) | SS | 
```

the said grammar will generate all the paranthesis matching possible.

# TODO
- [x] Create a function for evaluation of a single variable.
