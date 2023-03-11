# hourly-goats
A mastodon bot to post goats every hour. hopefully flexible enough for other people to use

## How to use
See the [Mastodon API documentation](https://docs.joinmastodon.org/client/intro/) to learn how to set up an app, and the [Mastodon.py docs](https://mastodonpy.readthedocs.io/en/stable/) on how to initialize an app.
The bot needs to exist in a directory with the following:
- A `queue` directory
- A `used` directory
- A `data.csv` file. The bot is written to use a photographer name, license type, and source, but with some minor tweaking can take any data in the CSV file you want.

The `queue` directory should contain all images you want the bot to post, with a number as their file name corresponding to a line in the CSV file. As each image gets posted it's moved to the `used` folder until the queue is empty.
