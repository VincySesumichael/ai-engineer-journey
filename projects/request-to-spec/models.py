

# @dataclass
# class Book:
#     title: str
#     author: str
#     pages: int = 0          # default value

# book = Book(title="Python Basics", author="Sam", pages=200)
# print(book.title)           # dot instead of ["title"]
# print(book)                 # prints all fields neatly


# Build (~2 hours): create projects/request-to-spec/models.py with:

# A Request dataclass: id, text, requested_by, priority.


from dataclasses import dataclass
@dataclass
class Request:
    id: int
    text: str
    requested_by: str    
    priority: str 

# request= Request(id=1, text="Show me the monthly count of new policies for managers", requested_by="Sara", priority="high")
# print(request.text)           # dot instead of ["title"]
# print(request)                 # prints all fields neatly



# A Spec dataclass holding what a finished spec contains, such as goal, metrics, filters, audience and missing_details. Hint: some fields hold lists. Look up how dataclasses handle list defaults; using [] directly gives an error, and finding out why is part of the exercise.
# A TestCase dataclass: description and expected_result.
# In checker.py, rebuild your 7 requests as Request objects, loop over them, and print request.id with the missing details.

# from dataclasses import dataclass, field
# @dataclass
# class Spec:
#     goal: str
#     audience: str =""
#     metrics: list[str]=field(default_factory=list)
#     filters: list[str]   =field(default_factory=list)
#     missing_details: list[str]=field(default_factory=list)


# spec_a = Spec(goal="Monthly policy count")
# spec_b = Spec(goal="Inactive loans")
# spec_a.metrics.append("policy count")
# print(spec_a.metrics)
# print(spec_b.metrics)   # should still be empty: that proves each Spec has its own list



# from dataclasses import dataclass, field
# @dataclass
# class TestCase:
#     description: str
#     expected_result: str 
 
