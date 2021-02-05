import pandas as pd
import matplotlib.pyplot as plt


def find_decade(year):
    if year < 1800:
        return "before18"
    elif 1800 <= year < 1810:
        return "eighteenhundreds"
    elif 1810 <= year < 1820:
        return "eighteentens"
    elif 1820 <= year < 1830:
        return "eighteentwenties"
    elif 1830 <= year < 1840:
        return "eighteenthirties"
    elif 1840 <= year < 1850:
        return "eighteenforties"
    elif 1850 <= year < 1860:
        return "eighteenfifties"
    elif 1860 <= year < 1870:
        return "eighteensixties"
    elif 1870 <= year < 1880:
        return "eighteenseventies"
    elif 1880 <= year < 1890:
        return "eighteeneighties"
    elif 1890 <= year < 1900:
        return "eighteennineties"
    elif 1900 <= year < 1910:
        return "nineteenhundreds"
    elif 1910 <= year < 1920:
        return "nineteentens"
    elif 1920 <= year < 1930:
        return "nineteentwenties"
    elif 1930 <= year < 1940:
        return "nineteenthirties"
    elif 1940 <= year < 1950:
        return "nineteenforties"
    elif 1950 <= year < 1960:
        return "nineteenfifties"
    elif 1960 <= year < 1970:
        return "nineteensixties"
    elif 1970 <= year < 1980:
        return "nineteenseventies"
    elif 1980 <= year < 1990:
        return "nineteeneighties"
    elif 1990 <= year < 2000:
        return "nineteennineties"
    elif 2000 <= year < 2010:
        return "twothousands"
    elif 2010 <= year < 2020:
        return "twentytens"
    elif year >= 2020:
        return "twentytwewnties"
    else:
        return "unknown"


decades_dict = {
    "before18": 0,
    "eighteenhundreds": 0,
    "eighteentens": 0,
    "eighteentwenties": 0,
    "eighteenthirties": 0,
    "eighteenforties": 0,
    "eighteenfifties": 0,
    "eighteensixties": 0,
    "eighteenseventies": 0,
    "eighteeneighties": 0,
    "eighteennineties": 0,
    "nineteenhundreds": 0,
    "nineteentens": 0,
    "nineteentwenties": 0,
    "nineteenthirties": 0,
    "nineteenforties": 0,
    "nineteenfifties": 0,
    "nineteensixties": 0,
    "nineteenseventies": 0,
    "nineteeneighties": 0,
    "nineteennineties": 0,
    "twothousands": 0,
    "twentytens": 0,
    "twentytwewnties": 0
}
serial_killers = pd.read_csv("serial_killers.csv")
print(serial_killers.info())
print(serial_killers.describe())

years_from = serial_killers["Active From"]
years_to = serial_killers["Active To"]

plt.style.use('ggplot')
plt.title("Years From")
(n, bins, patches) = plt.hist(years_from, bins=223)
# print(f"N: {n}, bins: {bins}, patches: {patches}")
plt.show()
plt.title("Years To")
plt.hist(years_to, bins=223)
plt.show()

for x in range(0, 438):
    # find decade of each year in range of (from, to), increase all decades it is found in
    set_of_decades = set()
    range_of_years = range(years_from[x], years_to[x] + 1)
    for d in range_of_years:
        set_of_decades.add(find_decade(d))
    for t in set_of_decades:
        decades_dict[t] += 1

print(*decades_dict.items(), sep='\n')
