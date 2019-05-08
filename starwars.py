from requests import get as requests_get

def main():
    def search_planet(x):
        global a
        thy = requests_get(x)
        thy_1 = thy.json()
        a = thy_1["name"]

    def massiv(x):
        global m
        m = []
        for i in x:
            m.append(i)

    def search_films(x):
        global j
        j = str
        for i in x:
            ght = requests_get(i)
            ght_1 = ght.json()
            k = str(ght_1["title"] + '(' + str(ght_1["episode_id"]) + ')')
            j = str(j) + k + '; '

    name = requests_get('https://www.swapi.co/api/people')
    planet = requests_get('https://www.swapi.co/api/planets')

    data = name.json()
    data_1 = planet.json()

    z = 0
    ch = []
    for i in data['results']:
        pl = data['results'][z]['homeworld']
        films = data['results'][z]['films']
        massiv(films)
        search_films(m)
        search_planet(pl)
        b = 'Name: ' + (data['results'][z]['name']) + '; Planet: ' + a + '; Film: ' + str(j)
        ch.append(b)
        z +=1

    for i in ch:
        print(i, '\n')


if __name__ == '__main__':
    main()
