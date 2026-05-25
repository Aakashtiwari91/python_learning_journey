import json

import json

def load_data():
    try:
        with open("youtube1.txt", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []
    
    
def data_save_helper(videos):
    with open('youtube1.txt','w') as file:
        return json.dump(videos, file)
    
def list_all_videos(videos):
    print("\n")
    print('*'*70)
    for index , video in enumerate(videos , start=1):
        print(F"{index}.{video['name']}, duration : {video['time']}")

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name':name,'time':time})
    data_save_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter video index to be update: "))
    if 1<=index <=len(videos):
        name = input("Enter video name: ")
        time = input("Enter video duration :")
        videos[index-1] = {'name':name, 'time':time}
        data_save_helper(videos)
    else:
        print("Invalid choice")
    

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter video  index  to be deleted : "))
    if 1<=index <=len(videos):
        del videos[index-1]
        data_save_helper(videos)
    else:
        print("Invalid choice")

def main():
    videos = load_data()
    while True:
        print("\n  youtube manager | choose an option")
        print("1. list all youtube videos")
        print("2. add new video on youtube")
        print("3. update videos on youtube")
        print("4. delete videos on youtube")
        print("5 exit from youtube video")
        
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:               # default case 
                print("Invalid choice")
            
            
if __name__ == "__main__":
    main()