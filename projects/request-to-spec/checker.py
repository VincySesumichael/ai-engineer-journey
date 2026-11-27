# projects/request-to-spec/checker.py

# Your three word lists at the top, with plural names.
# A function find_missing_details(text: str) -> list[str]
# with a docstring, which returns the list of missing categories. No printing inside it.
# Below it, assert tests for: a request with everything, a vague request, capital letters,
# and an empty string.
# A loop over your 5 sample requests that prints the result for each, using the function.

time_words = [
    "daily",
    "weekly",
    "monthly",
    "quarter",
    "quarterly",
    "year",
    "yearly",
    "annual",
    "ytd",
    "last month",
    "this year",
    "since",
    "between",
    "2026",
]

metric_words = [
    "count",
    "how many",
    "number of",
    "total",
    "sum",
    "average",
    "avg",
    "amount",
    "percentage",
    "rate",
    "ratio",
    "trend",
]
audience_words = [
    "manager",
    "management",
    "operations",
    "ops",
    "team",
    "client",
    "executive",
    "leadership",
    "finance",
    "underwriting",
]


def find_missing_details(text: str) -> list[str]:
    """returns the list of missing categories"""
    text_lower = text.lower()
    match_timeperiod = [w for w in time_words if w in text_lower]
    match_metric = [w for w in metric_words if w in text_lower]
    match_audience = [w for w in audience_words if w in text_lower]
    missing = []
    if not match_timeperiod:
        missing.append("time period")
    if not match_metric:
        missing.append("metric")
    if not match_audience:
        missing.append("audience")

    return missing


# request1 = "Show me the monthly count of new policies for managers"
# request2 = "Give all condo policies"
# request3 = "how many l09 policies details for yearly for client"
# request4 = "provide lko7  Policy Changes quarterly"
# request5 = "provide all inactive loans"
# request6 = " "
# request7 = "MONTHLY COUNT for MANAGERS"

# requests =[request1,request2,request3,request4, request5 ]

# for request in requests:
#     missing = find_missing_details(request)
#     if missing:
#         print(f"'{request}'  is missing: {',' .join(missing)}")
#     else:
#         print(f"'{request}' has everything ")

# assert find_missing_details(request1) == []
# assert find_missing_details(request2) == ["time period", "metric", "audience"]
# assert find_missing_details(request3) == []
# assert find_missing_details(request4) == ["metric", "audience"]
# assert find_missing_details(request5) == ["time period", "metric", "audience"]
# assert find_missing_details(request6) == ["time period", "metric", "audience"]
# assert find_missing_details(request7) == []


# if missing:
#     print(f"'{request}' is missing: {', '.join(missing)}")
# else:
#     print(f"'{request}' has everything")

# assert find_missing_details("Give all condo policies") == ["time period", "metric", "audience"]


# dataclases
from models import Request

request1 = Request(
    id=1,
    text="Show me the monthly count of new policies for managers",
    requested_by="Sara",
    priority="high",
)
request2 = Request(
    id=2, text="Give all condo policies", requested_by="Sara", priority="high"
)
request3 = Request(
    id=3,
    text="how many l09 policies details for yearly for client",
    requested_by="Sara",
    priority="high",
)
request4 = Request(
    id=4,
    text="provide lko7  Policy Changes quarterly",
    requested_by="Sara",
    priority="high",
)
request5 = Request(
    id=5, text="provide all inactive loans", requested_by="Sara", priority="high"
)
request6 = Request(id=6, text=" ", requested_by="Sara", priority="high")
request7 = Request(
    id=7, text="MONTHLY COUNT for MANAGERS", requested_by="Sara", priority="high"
)

requests = [request1, request2, request3, request4, request5, request6, request7]


for request in requests:
    missing = find_missing_details(request.text)
    if missing:
        print(f"  '{request.id}' , '{request.requested_by}' , '{request.text}'  is missing: {', '.join(missing)}")
    else:
        print(f" '{request.id}' ,'{request.requested_by}' , '{request.text}' has everything ")

assert find_missing_details(request1.text) == []
assert find_missing_details(request2.text) == ["time period", "metric", "audience"]
assert find_missing_details(request3.text) == []
assert find_missing_details(request4.text) == ["metric", "audience"]
assert find_missing_details(request5.text) == ["time period", "metric", "audience"]
assert find_missing_details(request6.text) == ["time period", "metric", "audience"]
assert find_missing_details(request7.text) == []
