from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    def main():
    post = fetch_data()

    print(
        "Fetched Post Title:",
        post.get("title", "No title found")
    )

    write_log(post)


if __name__ == "__main__":
    main()