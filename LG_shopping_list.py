shopping_dict = {
    "piekarnia": ["chleb", "bułka", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

shopping_dict = {k.capitalize():[i.capitalize() for i in v] for k,v in shopping_dict.items()}

for k in shopping_dict:
    print(f"Idę do {k} i kupuję tam {shopping_dict[k]}.")
print(f"W sumie kupuję {sum(len(shopping_dict[v]) for v in shopping_dict )} produktów")