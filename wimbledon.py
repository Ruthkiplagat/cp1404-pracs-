import csv

def read_csv(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

def get_champions(data):
    champions = {}
    for row in data:
        player = row[0]
        if player in champions:
            champions[player] += 1
        else:
            champions[player] = 1
    return champions

def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)

def display_champions(champions):
    print("Wimbledon Champions:")
    for player, wins in champions.items():
        print(f"{player} {wins}")

def display_countries(countries):
    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)

def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)
    champions = get_champions(data)
    countries = get_countries(data)
    display_champions(champions)
    display_countries(countries)

if __name__ == "__main__":
    main()