def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed #"Hello"
original = [49, 50, 80, 65]
passed = passing_scores(original)
try:
    if not isinstance(passed, list):
        raise TypeError("Datatype for passed must be a list")

    for num in passed:
        if num < 50:
            raise ValueError("Scores must be greater than or equal to 50")
except (TypeError, ValueError) as error:
    print(f"Error: {error}")

assert passing_scores([50]) == [50], "Pass boundary should be 5"
assert passing_scores([65]) == [65], "Passing score 65 not returning correctly."
assert passing_scores([]) == [], "Empty list must return an empty list."
# assert isinstance(passed, list), "Passed datatype must be a list"
#assert all(for each_score in passed >= 50 and for each in original: each >= 50 in passed), "Pass scores missing in filtered list"
# assert all(score >= 50 for score in passed) and \
#        all(score in passed for score in original if score >= 50), \
#        "Pass scores missing in filtered list"


