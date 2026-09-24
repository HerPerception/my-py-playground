def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed #"Hello"

passed = passing_scores([49, 50, 80, 65])
try:
    if not isinstance(passed, list):
        raise TypeError("Datatype for passed must be a list")

    for num in passed:
        if num < 50:
            raise ValueError("Scores must be greater than or equal to 50")
except (TypeError, ValueError) as error:
    print(f"Error: {error}")

# assert isinstance(passed, list), "Passed datatype must be a list"


