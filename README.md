# Simple-Echo-bot

This is a simple bot for [Zulip](https://www.zulipchat.com) that "echoes" the messages that is sent to it.
This can be used as a template to write more complex bots for Zulip using the official Python bindings for the bots from Zulip.

## Running the bot

1. Clone this repo

2. Create a `virtualenv`
```
virtualenv bot-venv
```

3. Activate the `venv`

```
On Windows: 
bot-venv\Scripts\activate

On Linux:
source bot-venv/bin/activate
```

4. Install `zulip_bots` package.
```
pip install zulip_bots
```

5. Download the `.zuliprc` file for your bot.

6. Run the bot using the command:
```
zulip-run-bot bot.py --config-file .zuliprc
```
