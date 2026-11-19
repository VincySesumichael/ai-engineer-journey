# Variables and strings

# Exercise 1 (variables and strings), without the answer:

# Create a variable that holds a request sentence of your own. Then print three things about it:

# the request in all capital letters
# how many words it has
# whether it contains the word “region” (True or False)

# name = "Vincy"
# role = "AI Engineer"
# print(f"{name} is becoming an {role}")
# request = "  Can I get a report on late payments?  "
# print(request.strip().upper())
# print(len(request.strip()))
# print("report" in request.lower())

# Exer1 Variables and strings
# req = "How many payments does the loan hold  in the Region "
# words = req.split()
# upper_text = req.strip().upper()
# word_count = len(words)
# assert word_count == 10
# has_region = "region" in req.lower()


# print(words)
# print(upper_text)
# print(word_count)
# print(has_region)


# Exer2 list

# ext: exercise 2 (lists)

# Make a list of 3 request strings.
# Add 2 more to the list.
# Print how many requests the list now holds.
# Print only the first three.
# Add one assert that checks the list length.


# req1 = "How many payments does the loan hold  in the Region "
# req2 = "Provide me the voluntary policies  "
# req3 = "Give all l09 policies"
# requests = [req1, req2, req3]
# print(requests)
# #add to the list
# req4 = "Provide lko7  Policy Changes"
# req5 = "Provide all inactive loans"
# requests.append(req4)
# requests.append(req5)
# print(requests)

# requestcount = len(requests)
# assert requestcount == 5
# print(requestcount)
# print(requests[0:3])

# Exercise 3 (dictionaries):

# Create one request as a dictionary with 4 fields: id, text, requested_by and priority.
# Print just the text field.
# Add a 5th field, deadline, after the dictionary is created.
# Try to get a field that doesn’t exist, such as audience, in a way that doesn’t crash.
# Hint: dictionaries have a method that lets you give a default value.
# Loop through the dictionary and print each field name and its value on its own line.


requests = [
    {
        "id": "req_01",
        "text": "Show me the monthly count of new policies for managers",  # timeperiod, metric, aud
        "requested_by": "Sara",
        "priority": "high",
    },
    {
        "id": "req_02",
        "text": "Give all condo policies",  # No timeperiod, metric, aud
        "requested_by": "John",
        "priority": "medium",
    },
    {
        "id": "req_03",
        "text": "how many l09 policies details for yearly for client",  # timeperiod, metric, aud
        "requested_by": "Henry",
        "priority": "low",
    },
]

requests.extend(
    [
        {
            "id": "req_04",
            "text": "provide lko7  Policy Changes quarterly",  # no aud and metric
            "requested_by": "Sam",
            "priority": "low",
        },
        {
            "id": "req_05",
            "text": "provide all inactive loans",
            "requested_by": "John",
            "priority": "High",
        },
    ]
)

timeperiod = [
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

metric = [
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
audience = [
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

for request in requests:
    text_lower = request.get("text", "").lower()
    match_timeperiod = [w for w in timeperiod if w in text_lower]
    match_metric = [w for w in metric if w in text_lower]
    match_audience = [w for w in audience if w in text_lower]
    missing = []
    if not match_timeperiod:
        missing.append("time period")
    if not match_metric:
        missing.append("metric")
    if not match_audience:
        missing.append("audience")
    if missing:
        print(f"{request['id']} is missing: {', '.join(missing)}")
    else:
        print(f"{request['id']} has everything")

    # print(request["id"] , "->", "Timeperiod :", match_timperiod, "|" , "Metric :",match_metric, "|", "Audience :", match_audience)


# print(requests)

# print text
# for item in requests:
#     print(item["text"])

# # #add a field to all ids
# for item in requests:
#     item["deadline"] = "2020-01-02"


# # add a field only to id 3
# for item in requests:
#     if item["id"] == "req_03":
#         item["deadline"] = "2026-01-02"
# print(requests)

# # #get a field which is not available
# for item in requests:
#     # field_check= item["audience"]
#     field_check = item.get("audience", "Not available")
#     print(item["id"], "->", field_check)


# # #loop through dic and print list in one line
# for request in requests:
#     for key, value in request.items():
#         print(f"{key}: {value}")
#     print("---")
# print(item["id"][0],"|" , item["text"], "|", item["requested_by"], "|", item["priority"])


# Check each request for a time period, a metric and an audience,
# and print what’s missing, for example req_01 is missing: time period, audience


# # print(requests)

# for request in requests:
#     if request["id"]== "req_01":
#         timeperiod=request["timeperiod"]="daily"
#         metric=request["metric"]="01"
#         audience=request["audience"]="operation"
#     if request["id"]== "req_03":
#         timeperiod=request["timeperiod"]="monthly"
#     if request["id"]== "req_04":
#         timeperiod=request["timeperiod"]="yearly"
#         audience=request["audience"]="client"

# # print(requests)
# for request in requests:
#     a=timeperiod in requests
#     print(request["id"] , "->", a)
