def add_tag(profile, tag):
    updated = profile.copy()
    #updated["tags"] = profile["tags"].copy()
    updated["tags"].append(tag)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")

assert original["tags"] == ["python"], "Original list should remain unchanged."
assert changed["tags"] == ["python", "testing"], "Copied list should be changed."

changed["tags"].append("debugging")

assert original["tags"] == ["python"], "Original list should remain unchanged."

print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])

#============================================================================================
# Original Function

# def add_tag(profile, tag):
#     updated = profile.copy()
#     updated["tags"].append(tag)
#     return updated
# original = {"name": "Ada", "tags": ["python"]}
# changed = add_tag(original, "testing")
# print(original["tags"])
# print(changed is original)
# print(changed["tags"] is original["tags"])

# Output of original Function:
# ['python', 'testing']
# False
# True
# profile.copy() makes a shallow copy of the dictionary. The dictionary itself gets copied. The 
# value of "tags" is a list , and the list itself is not copied, both dictionaries point to 
# the same list.
#=============================================================================================