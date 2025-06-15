def cat_hat(str):
    # Count occurrences of "cat" and "hat" in the string
    return str.count("cat") == str.count("hat")

print(cat_hat("catandhat"))      # True (both "cat" and "hat" appear 1 time)
print(cat_hat("catcatandhat"))   # False (cat appears 2 times, hat appears 1 time)
print(cat_hat("hatandcat"))      # True (both "cat" and "hat" appear 1 time)
print(cat_hat("dogandbat"))      # False (neither "cat" nor "hat" appear)
