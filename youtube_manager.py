import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            videos = json.load(file)
            return videos
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)


def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return
    for idx, vid in enumerate(videos, 1):
        print(f"{idx}. Name: {vid['name']}, Time: {vid['time']}")


def add_videos(videos):
    name = input("Enter Video name: ")
    time = input("Enter Video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully!")


def update_videos(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        idx = int(input("Enter the number of the video to update: ")) - 1
        if 0 <= idx < len(videos):
            name = input("Enter new Video name (leave blank to keep current): ")
            time = input("Enter new Video time (leave blank to keep current): ")
            if name:
                videos[idx]['name'] = name
            if time:
                videos[idx]['time'] = time
            save_data_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")


def delete_videos(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        idx = int(input("Enter the number of the video to delete: ")) - 1
        if 0 <= idx < len(videos):
            videos.pop(idx)
            save_data_helper(videos)
            print("Video deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all favorite videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

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
                print("INVALID CHOICE")


if __name__ == "__main__":
    main()
