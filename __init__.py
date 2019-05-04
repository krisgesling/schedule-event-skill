from mycroft import MycroftSkill, intent_file_handler


class ScheduleEvent(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('event.schedule.intent')
    def handle_event_schedule(self, message):
        self.speak_dialog('event.schedule')


def create_skill():
    return ScheduleEvent()

