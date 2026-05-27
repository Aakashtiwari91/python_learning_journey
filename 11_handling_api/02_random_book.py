import requests


def access_random_book_info():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    
    # get or fetch api
    response = requests.get(url)
    
    # convert data into json fromat
    data = response.json()
    
    if data["success"] and "data" in data:
        book_title = data["data"]["volumeInfo"]["title"]
        book_auther = data["data"]["volumeInfo"]["authors"][0]
        return book_title, book_auther
    else:
        raise Exception("Failed to fetch data")


def main():
    try:
        book_title , book_author  = access_random_book_info()
        print(F"book title name: {book_title} and book auther name: {book_author}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()