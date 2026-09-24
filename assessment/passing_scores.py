def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return "Hello"#passed

 passed = passing_scores([49, 50, 80, 65])
assert isinstance(passed, list), "Passed datatype must be a list"


