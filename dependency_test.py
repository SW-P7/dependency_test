from thefuzz import fuzz
if __name__ == "__main__":
    print(fuzz.partial_ratio("this is a string", "this is a string"))
    