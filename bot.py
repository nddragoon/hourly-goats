import os, random, linecache, mastodon
from mastodon import Mastodon
from time import sleep
from shutil import move

mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/'
)

queue = "./queue"
used = "./used"

# If the queue is empty, move all images back into the queue
if len(os.listdir(queue)) == 0:
    for file in os.listdir(used):
        move(os.path.join(used, file), queue)

# Pick a random file from the queue, store as a path relative to the bot script
file_name = random.choice(os.listdir(queue))
file = os.path.join(queue, file_name)

# Get an array of the author, license, and source from the csv at the line corresponding to the file name
data = linecache.getline( "data.csv", int(file_name.split(".")[0]) ) .split(",")

# Goats! 🐐
# 
# [Author], [License].
# Source: [Source]
post_text = f"Goats! 🐐\n\n{data[0]}, {data[1]}.\nSource: {data[2]}"

# Upload the image, wait 10 seconds to make sure it uploaded
upload = mastodon.media_post(
    media_file = file,
    mime_type = "image",
)
sleep(10)

# Publish the post
mastodon.status_post(
    status = post_text,
    media_ids = upload
)

# Move the image to the used folder
move(file, used)