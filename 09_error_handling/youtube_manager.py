import json

def load_data():
    try:
        with open('youtube1.txt','r') as file: # (with context manager):  open and after work close file automatically     ** 'r' - Read entire file (like loop)
            return json.load(file)            # json.load() - convert JSON to python object  , read JSON data from a file and convert it into a Python object.
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data_helper(videos):
    with open('youtube1.txt', 'w') as file:    # 'w'  creates file if not exists , overwrites old content
        json.dump(videos , file)        # json.dump() is used to convert a Python object into JSON format and store it directly into a file.


def list_all_videos(videos):
    print("\n")
    print("*"*70)
    print("\n")
    for index ,video in enumerate(videos,start = 1):   # enumerate(): loop over an iterable while also getting the index (position) of each element. (1 'apple') (2.mango)
        print(F"{index}. {video['name']},Duration: {video['time']}")
    print("\n")
    print("*"*70)


def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video Time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index  = int(input("Enter the video number to update:"))
    if 1<=index <=len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1]= {'name':name , 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to be deleted:"))
    
    if 1<= index <=len(videos):
        del videos[index-1]                                    # del delete item from original list and not return any thing
        save_data_helper(videos)
    else:
        print("Invalid video index selected")




def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. update a youtube video details")
        print("4. delete a youtube video")
        print("5. Exit the app")
        
        choice = input("Enter your choice: ")
        
        # print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice")
                

if __name__ == "__main__":                                        # __name__ is a special Python variable that tells whether a file is running directly or imported.
    main()                                                        # first main() run kar dega 