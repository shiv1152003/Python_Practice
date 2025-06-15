def in_trouble(j_angry, s_angry):
    # Return True if both are angry or neither are angry
    return j_angry == s_angry

print(in_trouble("true", "true"))
print(in_trouble("false","false"))
print(in_trouble("false","true"))
print(in_trouble("true","false"))