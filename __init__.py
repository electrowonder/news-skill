from mycroft import MycroftSkill, intent_file_handler


class News(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('news.intent')
    def handle_news(self, message):
        self.speak_dialog('news')


def create_skill():
    return News()

