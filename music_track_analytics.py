class MusicTrack:
    def __init__(self, title, artist, play_count=0, skip_count=0):
        self.title = title
        self.artist = artist
        self.__play_count = play_count
        self.__skip_count = skip_count

    def play(self):
        self.__play_count += 1
        print(f"Playing '{self.title}' by {self.artist}...")

    def skip(self):
        self.__skip_count += 1
        print(f"Skipped '{self.title}'.")

    def get_play_count(self):
        return self.__play_count

    def get_skip_count(self):
        return self.__skip_count

    def set_play_count(self, new_count):
        if new_count >= 0:
            self.__play_count = new_count
        else:
            print("Invalid play count. Must be non-negative.")

    def set_skip_count(self, new_count):
        if new_count >= 0:
            self.__skip_count = new_count
        else:
            print("Invalid skip count. Must be non-negative.")

    def display_details(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Plays: {self.__play_count}, Skips: {self.__skip_count}")

# Initial library
library = [
    MusicTrack("Imagine", "John Lennon", 5, 2),
    MusicTrack("Bohemian Rhapsody", "Queen", 8, 1),
    MusicTrack("Billie Jean", "Michael Jackson", 10, 0)
]

# Main menu loop
while True:
    print("\nMUSIC TRACK ANALYTICS SYSTEM")
    print("1. Add Multiple Music Tracks")
    print("2. View All Tracks")
    print("3. Update Track Stats")
    print("4. Delete Track")
    print("5. Total Plays and Skips")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        count = int(input("How many music tracks do you want to add? "))
        for i in range(count):
            print(f"\nAdding track {i+1} of {count}")
            title = input("Enter music title: ")
            artist = input("Enter artist name: ")
            play_count = int(input("Enter initial play count: "))
            skip_count = int(input("Enter initial skip count: "))

            if play_count < 0 or skip_count < 0:
                print("Error: Play and skip counts must be non-negative.")
            else:
                track = MusicTrack(title, artist, play_count, skip_count)
                library.append(track)
                print(f"'{title}' added to library.")

    elif choice == "2":
        print("\nTrack List:")
        if not library:
            print("No tracks in library.")
        else:
            for i, track in enumerate(library, start=1):
                print(f"{i}. ", end="")
                track.display_details()

            print("\nEncapsulation Test:")
            for track in library:
                plays = track.get_play_count()
                skips = track.get_skip_count()
                print(f"{track.title} stats - Plays: {plays}, Skips: {skips}")

    elif choice == "3":
        update_title = input("Enter track title to update: ")
        found = False
        for track in library:
            if track.title.lower() == update_title.lower():
                new_plays = int(input("Enter new play count: "))
                new_skips = int(input("Enter new skip count: "))

                if new_plays < 0 or new_skips < 0:
                    print("Error: Counts must be non-negative.")
                else:
                    track.set_play_count(new_plays)
                    track.set_skip_count(new_skips)
                    print(f"'{track.title}' updated.")
                found = True
                break
        if not found:
            print("Track not found.")

    elif choice == "4":
        delete_title = input("Enter track title to delete: ")
        for track in library:
            if track.title.lower() == delete_title.lower():
                library.remove(track)
                print(f"'{delete_title}' removed from library.")
                break
        else:
            print("Track not found.")

    elif choice == "5":
        print("\nTotal Plays and Skips of Selected Tracks")
        total_plays = 0
        total_skips = 0
        selected = []
        for track in library:
            select = input(f"Include '{track.title}' in total? (Y/N): ").strip().upper()
            if select == "Y":
                selected.append(track)
                total_plays += track.get_play_count()
                total_skips += track.get_skip_count()
        if selected:
            print("\nSelected Tracks:")
            for track in selected:
                track.display_details()
            print(f"\nTotal Plays: {total_plays}")
            print(f"Total Skips: {total_skips}")
        else:
            print("No tracks selected.")

    elif choice == "6":
        print("Exiting")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")