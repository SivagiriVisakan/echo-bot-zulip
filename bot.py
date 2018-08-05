"""
    This is a simple bot that can be used as a template to write more complex
    bots for Zulip.
    https://www.zulip.com.
"""

class SimpleBotHandler(object):
    HELP = """
                I am a simple bot and I  echo the message that is sent to me.
                Try sending me a message !
            """
    def usage(self):
        return self.HELP

    def handle_message(self, message, bot_handler):
        content = message['content']
        if content.lower() == 'help':
            bot_handler.send_reply(message, self.HELP)
            return

        bot_handler.send_reply(message, content)

handler_class = SimpleBotHandler
