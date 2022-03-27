shopping_dict = {
    "piekarnia": ["chleb", "bułka", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

shopping_dict = {k.capitalize():[i.capitalize() for i in v] for k,v in shopping_dict.items()}