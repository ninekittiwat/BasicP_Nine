def ticket(movie_list,user,price_movie,subtitle):
    print("Here! Your Ticket")
    print(movie_list[user-1]["name"] , "price" , price_movie , "Sub is", subtitle)

def calculate(movie_list,user_select):
    movie_genre = movie_list[user_select-1]["genre"]
    if movie_genre == "romantic":
        price = 50
    else :
        price = 0
    all_price = price + movie_list[user_select-1]["cost"]
    return all_price

def show_movie(movie_list):
    print("-----------Movie List-----------")
    print("----Romantic price plus 50 baht----")
    for i in movie_list:
        print(i["name"],"price",i["cost"],"Genre",i["genre"])
    main(movie_list)

def buy_ticket(movie_list):
    select = int(input("Select movie 1-5 : "))
    user_age = int(input("Enter your age : "))
    movie_age = movie_list[select-1]["rate"]

    if movie_age == 18 and user_age < 18:
        print("You too yong for this movie")
        print("Get out!!!!")
        main(movie_list)

    else :
        sub = int(input("Select your subtitle [1 for Thai] : [2 for Subtitle] \n :"))
        if sub == 1:
            subtitle = "Thai"
        if sub == 2:
            subtitle = "Subtitle"
        price_movie = calculate(movie_list,select)
        ticket(movie_list,select,price_movie,subtitle)
        

def main(movie_list):
    n = int(input(" [1] for list of movie \n [2] for buy a ticket \n :"))
    if n == 1:
        show_movie(movie_list)
    else :
        buy_ticket(movie_list)


ls = [
    {"name":"movie A","rate":18 , "genre":"action" , "cost":200},
    {"name":"movie B","rate":"G" , "genre":"romantic" , "cost":250},
    {"name":"movie C","rate":18 , "genre":"romantic" , "cost":100},
    {"name":"movie D","rate":"G" , "genre":"horror" , "cost":205},
    {"name":"movie E","rate":"G" , "genre":"cartoon" , "cost":300}, 
]

main(ls)