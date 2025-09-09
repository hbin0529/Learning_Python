from application import Movie

list_of_movie_details = []

while True:
    movie_name = input("Enter movie name: ")
    actor_name = input("Enter actor name: ")
    actress_name = input("Enter actress name: ")

    movie_details = Movie(movie_name, actor_name, actress_name)

    list_of_movie_details.append(movie_details)

    print("Movie Details are Added Successfully!!")

    option = input("Do you want to add another movie? (y/n): ") # 사용자가 N, n 으로 작성할 수 있으니, 대소문자 비교 작성

    if option.lower() == "n": # 대소문자 비교 작성
        break

print("\nHere are all Movie Details ")
for movies in list_of_movie_details:
    movies.movie_details()
    print(" ")







