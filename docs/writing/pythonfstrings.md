---
contributors:
- Nirant Kasliwal
date: '2019-08-27 23:29:18+05:30'
description: Python f-string Primer
draft: false
excerpt: Python f-string Primer
featured_image: images/ink.png
images: []
lastmod: '2019-08-27 23:29:18+05:30'
show_reading_time: true
tags:
- python
- tech
title: Best of Python 3 f-strings
toc: true
weight: 50
---

This piece is primarily meant for those new to Python. These include mathematicians, economists, and so on who want to use Python within a Jupyter environment. Here is a quick guide on how to make [Best of Jupyter](https://github.com/NirantK/best-of-jupyter).

## Quick Primer

If you are familiar with earlier Python versions, here are my top picks on how to move from .format () to this new one:

{{< highlight python >}}

_fstring = f'Total: {one + two}'  # Go f-string!
_format = 'Total: {}'.format(one + two)
_percent = 'Total: %s' % (one + two)
_concatenation = 'Total: ' + str(one + two)
assert _fstring == _format == _percent == _concatenation
{{< /highlight >}}

## f-string Magic

f-strings are how you should use print statements in Python. It is fairly reminiscent of LaTeX in it’s inline notation:
{{< highlight python >}}
# inline variables, similar to LaTeX
name = "Fred"
print(f"He said his name is {name}.")
# 'He said his name is Fred.'
{{< /highlight >}}

Notice how the variable _name_ can now be used inline. This is a simple and easy to use syntax: just include the variable in surrounding _{}_ while marking the string type as f-string using the ‘_f_’ in the beginning.

_Note to the advanced programmer_: 

‘f’ may be combined with ‘r’ to produce raw f-string which can be used inside regex or similar functions. ‘f’ may not be combined with ‘u’, this is because all Python3.6+ strings are Unicode by default now. This means, you can write fstrings in Hindi, Chinese, French, Korean and atleast 10 other languages.

> You can write fstrings in Hindi, Chinese, French, Korean and any language covered by Unicode.

But why are these called formatted-strings in the first place? Because you can use with some cool formatting hacks.

## Simplified Alignment and Spacing

Have you ever tried creating a table such as that for logging or visualization? Arranging the elements becomes a nightmare with several `\t` tab characters flying around.

This is much easier with Python f-strings using the colon ‘:’ operator, followed by a an alignment operator and field width value.

There are atleast 3 alignment operator: < for left aligned, > for right aligned, and ^ for center aligned. Refer the code example:

{{< highlight python >}}
correct = 'correct'
phonetic_correct = 'phonetic_correct'
typo = 'typo'
phonetic_typo = 'phonetic_typo'
phonetic_distance = 'phonetic_distance'

{{< /highlight >}}
{{< highlight python >}}

print(f'No Spacing:')
print(f'{correct}|{phonetic_correct}|{typo}|{phonetic_typo}|{phonetic_distance}|\n')
# No Spacing:
# correct|phonetic_correct|typo|phonetic_typo|phonetic_distance|
{{< /highlight >}}
{{< highlight python >}}

print(f'Right Aligned:')
print(f'{correct:>10}|{phonetic_correct:>20}|{typo:>10}|{phonetic_typo:>20}|{phonetic_distance:>20}|\n')
# Right Aligned:
#    correct|    phonetic_correct|      typo|       phonetic_typo|   phonetic_distance|
{{< /highlight >}}
{{< highlight python >}}

print(f'Left Aligned:')
print(f'{correct:<10}|{phonetic_correct:<20}|{typo:<10}|{phonetic_typo:<20}|{phonetic_distance:<20}|\n') 
# Left Aligned:
# correct   |phonetic_correct    |typo      |phonetic_typo       |phonetic_distance   |
{{< /highlight >}}
{{< highlight python >}}

print(f'Centre Aligned:')
print(f'{correct:^10}|{phonetic_correct:^20}|{typo:^10}|{phonetic_typo:^20}|{phonetic_distance:^20}|') 
# Centre Aligned:
#  correct  |  phonetic_correct  |   typo   |   phonetic_typo    | phonetic_distance  |
{{< /highlight >}}

You also have support for decimal truncation and similar standard formatting utilities:
{{< highlight python >}}
# auto-resolve variable scope when nested
width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")  # nested fields
# 'result:      12.35'
{{< /highlight >}}

You might notice something interesting here: width and precision are automatically picked up from the scope. This means you can calculate width and precision using screen width or other inputs from system and use that.

## Full Python Expressions Support

The above is only possible because the expression inside {} is actually being evaluated, or in programming terms: being executed.

This implies, that you can make any function call from within those {}.

Though, you should avoid doing this in practice very often because it might make your debugging very difficult. Instead, store the returned value from function in a variable and then add the variable in a fstring print statement.

Those coming from functional programming might miss their lambda functions. Don’t worry, Python has you covered:

## Lambda Functions in f-strings

{{< highlight python >}}
# If you feel you must use lambdas, they may be used inside of parentheses:
print(f'{(lambda x: x*3)(3)}')
# '9'
# note that this returned a <str> and not <int>
{{< /highlight >}}

# Summary

- f strings mean you can include variables and function calls inside your print statements
- Inline variables: these are easier to read and debug for the developer
- **_Use f-strings when you can_**!