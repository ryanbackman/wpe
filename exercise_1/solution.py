from collections import defaultdict, Counter

visits = defaultdict(Counter)

def collect_places():
    visits.clear()
    answer = " "
    while answer != "":
        answer = input("Tell me where you went: ").strip()
        if answer:
            if "," in answer:
                answers = answer.split(',')
                if len(answers) == 2:
                    city, country = answers
                    visits[country.strip()].update([city.strip()])
                else:
                    print("That's not a legal city, country combination")
            else:
                print("That's not a legal city, country combination")

def display_places():
    print("You Visited:")
    for country, cities in sorted(visits.items()):
        print(country)
        for city, count in sorted(visits[country].items()):
            if count > 1:
                print(f"\t{city} ({count})")
            else:
                print(f"\t{city}")

if __name__ == "__main__":
    collect_places()
    display_places()
