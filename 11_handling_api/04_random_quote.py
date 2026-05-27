import requests

def random_quote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    
    
    # fetch data from api
    

    response = requests.get(url)
    
    # convert api data into json fromat
    
    data  = response.json()
    
    if data["success"] and "data" in data:
        quote = data["data"]["content"]
        author_name = data["data"]["author"]
        quote_tag = data["data"]["tags"][0]
        return (quote ,author_name , quote_tag)
    else:
        raise Exception("Failed to fetch data from api")



def main():
    try:
        quote , author_name , quote_tag = random_quote()
        print(F" Quote : {quote} , author name : {author_name}  and  tags : {quote_tag}")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()