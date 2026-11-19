# Weekly log

## Week 1 (Nov 16 – Nov 22)

### Learned
- **LLM basics:** watched Karpathy's *Intro to Large Language Models* (next-token prediction, pre-training vs fine-tuning, context windows, security risks)
- **Strings:** `.upper()`, `.lower()`, `.strip()` (only trims the ends), `.split()` vs `.split(" ")`, where `.split(" ")` creates empty strings `''` for double and trailing spaces
- **Case-insensitive checks:** lower-case the text before searching
- **Lists:** creating, `.append()` one item, `.extend()` with one list of items, slicing `[0:3]`, `len()`
- **Dictionaries:** keys and values, adding fields, `.get()` with a default vs `[]` which raises `KeyError`, looping with `.items()`
- **Lists of dictionaries:** the structure for storing requests
- **Loops and indentation:** nested loops; Python needs consistent 4-space indentation (`IndentationError`)
- **List comprehensions:** `[w for w in words if w in text]` collects the matching words into a new list
- **if statements:** an empty list counts as `False`, so `if not matches:` means "nothing found"
- **Joining:** `", ".join(list)` turns a list into one readable string
- **assert:** compare a result with an independently known value. `assert x == x` can never fail, so it tests nothing

### Built
- Practice file covering strings, lists and dictionaries
- **Missing-details checker:** flags requests with no time period, metric or audience, using keyword lists. This is the rule-based baseline for the Request-to-Spec Assistant
- Test requests covering all, none and some details, with expected results written before running

### Stuck on / fixed
- Counted characters instead of words; fixed with `.split()`
- Wrapped dictionary values in lists by mistake; switched to plain strings
- Mixed indentation caused errors; fixed with Format Document
- Tried to use a list like a dictionary (`requests["id"]`); lists use positions, and dictionaries live inside the list

### Habits started
- Naming: plural for lists, snake_case, names that describe what they hold
- Write expected results before running code
- Keep internal company names out of practice files

### Next
- Turn the checker into a reusable function with type hints (Tuesday's work)
- Classes and dataclasses: `Spec` and `TestCase`
- Git branches and pull requests
- Write the 15-request evaluation set

### Hours so far
-