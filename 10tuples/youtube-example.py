search_term = input("Please enter a search term:")

with open('USVideos.csv', encoding="utf8") as movie_info:
    count = 0
    for l in movie_info:
        count+=1
        values = l.split(",")
        if len(values) > 2:
            print(f'{count} for {values[2]}')