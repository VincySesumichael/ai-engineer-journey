# Function greet

# def greet(name):
#     return f"Hello, {name}"

# msg = greet("Vincy")
# print(msg)

# #function tax
# def add_tax(price:float, rate:float =0.05 ) ->float:
#     return price + (2 *rate)

# tax = add_tax(2)
# print(tax)


# Exer count_words(text: str) -> int
def count_words(text: str) -> int:
    """Return the number of words in a text string."""
    return len(text.split())


word_count = count_words(" ")
assert count_words("provide all inactive loans") == 4
