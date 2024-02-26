programm_work = True
while programm_work == True:
  #all films
    serials_db = [ { "title": "Chronicles of the Galaxy", "genre": "Adventure", "seasons": 5, "rating": 8 },
       { "title": "Mystery Island", "genre": "Fantasy", "seasons": 3, "rating": 9 },
       { "title": "Epic Quest", "genre": "Fantasy", "seasons": 4, "rating": 7 },
       { "title": "Crime Files", "genre": "Crime Drama", "seasons": 6, "rating": 5},
       { "title": "Medical Miracles", "genre": "Medical Drama", "seasons": 2, "rating": 8 },
       { "title": "Time Travelers", "genre": "Adventure", "seasons": 4, "rating": 8 },
       { "title": "Comedy Central", "genre": "Comedy", "seasons": 7, "rating": 9 } ]

    find = 0
    while find not in [1, 2, 3, 4]:
        find = int(input('1 - find by genre, 2 - find by rating, 3 - show all films, 4 - exit: '))
      #Find film by the genre
        if find == 1:
            genre = input('Enter the TV show genre, that you want to find: ')
            found = False
            for movie in serials_db:
                if movie['genre'] == genre:
                    found = True
                    print(movie["title"])
            if not found:
                print('No movie of that genre found')
        #Find film by the rating
        elif find == 2:
            try:
                rating = int(input('Enter the TV show rating, that you want to find: '))
                found = False
                for movie in serials_db:
                    if movie['rating'] == rating:
                        found = True
                        print(movie["title"])
                if not found:
                    print('No movie with that rating found')
            except ValueError:
                print('Enter number, not symbol')
        #Show all films
        elif find == 3:
            for movie in serials_db:
              print(f"Title: {movie['title']}, Genre: {movie['genre']}, Seasons: {movie['seasons']}, Rating: {movie['rating']}")
        #Exit from the programm
        elif find == 4:
          print('Have a nice view')
          programm_work = False
        #If enterer print other number
        else:
            print('Enter 1, 2, 3 or 4')
