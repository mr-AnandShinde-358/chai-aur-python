import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
)
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES(?,?)",(name,time))
    # cursor.commit()
    conn.commit()

def update_video(video_id,new_name,new_time):
    print(video_id,new_name,new_time)
    cursor.execute("UPDATE videos SET name = ?, time=? WHERE id=?",(new_name,new_time,video_id))
    # cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    # cursor.commit()
    conn.commit()

def delete_video(video_id):
    cursor.execute('DELETE FROM videos where id=?',(video_id,))
    # cursor.commit()
    conn.commit()

def main():    
    while True:
        print("\n Youtube manager app with DB")
        print("1. List video")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit App")

        choice = input("Enter your choice: ")

        if choice =='1':
            list_videos()
        elif choice == '2':
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id=input("Enter video ID to update: ")
            name=input("Enter the video new name: ")
            time=input("Enter the video new time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id=input("Enter video ID to update: ")
            
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()

