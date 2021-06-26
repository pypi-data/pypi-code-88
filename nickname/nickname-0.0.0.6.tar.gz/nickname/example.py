from Name import Name

original = Name("Neil","George","Tyson")

aliases = [
    ("Neil Tyson",1923),
    ("Neil Tyson",1974),
    ("Neil G. Jones",2007),
    ("Neil George Jones",2007),
    ("Neil G Tyson",1997),
    ("Neil G. Tyson",1992),
    ("Neil Granola Tyson",1988),
    ("Neil George Jones",1990)
]

score_map = {}
for alias,year in aliases:
    score = original.compare(alias)
    
    if score not in score_map:
        score_map[score]=[]
    score_map[score].append(year)
    
    print(f"Comparing {original} to {alias} gives a score {score}.")

score, years = sorted(list(score_map.items()))[0]
minimum_dob = min(years)
maximum_dob = max(years)
print(f"Best score is {score}")
print(f"The minimum date of birth is {minimum_dob} and a maxiumum dob is {maximum_dob}.")
