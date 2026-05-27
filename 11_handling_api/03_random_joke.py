import requests

def get_random_joke():
    # url to get api
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    
    # fetch data from api
    response = requests.get(url)
    
    # convert api data into json format (for easy understanding)
    data = response.json()
    
    if data["success"] and "data" in data:
        joke = data["data"]["content"]
        return joke
    else:
        raise Exception("failed to fetch data")


def main():
    try:
        joke = get_random_joke()
        print(F"joke : {joke}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()