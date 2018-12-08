# Simple-Echo-bot

This is a simple bot for [Zulip](https://www.zulipchat.com) that "echoes" the messages that is sent to it.
This can be used as a template to write more complex bots for Zulip using the official Python bindings for the bots from Zulip.

## Running the bot locally

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

## Deploying the bot to Heroku

Before proceeding, please make sure you have the Heroku CLI installed.
For installation instructions, refer: [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

1. Modify the  `sample.zuliprc` with values specific to your bot.

2. Login into Heroku CLI
```
$ heroku login
```

3. Create a new application. When a new application is created, Heroku automatically creates
a repo on its server and adds its locally under the remote name `heroku`.
```
$ heroku create
```

4. Check that a new git remote `heroku` has been added
```
$ git remote -v
```

5. Now, push the code into the `master` branch of `heroku` remote. Whenever the push is done to the remote server, the app is automatically updated and deployed by Heroku.
```
$ git push heroku heroku-test:master
```

6. Check if there are any workers running alloted.
```
$ heroku ps

Free dyno hours quota remaining this month: 550h 0m (100%)
Free dyno usage for this app: 0h 0m (0%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

No dynos on ⬢ <app name>
```
If you receive a similar output saying no dynos are running, then you need to allot a worker to make
the bot start. For now, we will be alloting one dyno(similar to a server) as a worker.
```
$ heroku ps:scale worker=1
```

7. Now, check the logs to make sure that the bot is running. It should have an output something similar to the 
one below.
```
$ heroku logs


2018-12-08T13:45:19.041392+00:00 heroku[worker.1]: Starting process with command `zulip-run-bot bot.py --config-file sample.zuliprc`
2018-12-08T13:45:19.606792+00:00 heroku[worker.1]: State changed from starting to up
2018-12-08T13:45:22.071731+00:00 app[worker.1]: Running Bot Bot:
2018-12-08T13:45:22.071758+00:00 app[worker.1]: 
2018-12-08T13:45:22.071761+00:00 app[worker.1]: I am a simple bot and I  echo the message that is sent to me.
2018-12-08T13:45:22.071763+00:00 app[worker.1]: Try sending me a message !
2018-12-08T13:45:22.071765+00:00 app[worker.1]: 
2018-12-08T13:45:22.073109+00:00 app[worker.1]: INFO:root:starting message handling...
2018-12-08T13:45:50.951031+00:00 app[worker.1]: INFO:root:waiting for next message
2018-12-08T13:45:51.194360+00:00 app[worker.1]: INFO:root:waiting for next message
2018-12-08T13:46:08.538392+00:00 app[worker.1]: INFO:root:waiting for next message
2018-12-08T13:46:08.962915+00:00 app[worker.1]: INFO:root:waiting for next message
```


That's it ! Now the bot is deployed to Heroku !