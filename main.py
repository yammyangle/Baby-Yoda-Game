
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import requests
from kivy.clock import Clock
import datetime
from datetime import datetime
from kivymd.uix. floatlayout import MDFloatLayout
from kivymd.uix. behaviors import FakeRectangularElevationBehavior
from kivy.core.window import Window
from twilio.rest import Client
#Window.size = (300, 500)
from kivymd.uix.label import MDLabel

Window.size = (350, 600)

class Introduction(Screen):
    def on_touch_move(self, touch):
        if touch.x < touch.ox:
            self.parent.current = "introduction2"

class IntroductionTwo(Screen):
    def on_touch_move(self, touch):
        if touch.x < touch.ox:
            self.parent.current = "login"

base_id = "appo3z8pFbRIUjN0q"
table_name = "Login System"
url = "https://api.airtable.com/v0/" + base_id + "/" + table_name
api_key = "keyonOCTWYREdHmFl"
headers = {"Authorization": "Bearer " + api_key}
response = requests.get(url, headers=headers)

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


class LoginScreen(Screen):
    p = ""
    u = ""
    def logger(self):
        base_id = "appo3z8pFbRIUjN0q"
        table_name = "Login System"
        url = "https://api.airtable.com/v0/" + base_id + "/" + table_name
        api_key = "keyonOCTWYREdHmFl"
        headers = {"Authorization": "Bearer " + api_key}
        response = requests.get(url, headers=headers)
        rows = response.json()['records']
        correct = False

        for row in rows:
            if row['fields']['username'] == self.ids.user.text:
                if row['fields']['password'] == self.ids.password.text:
                    correct = True
        if correct == True:
            self.ids.welcome_label.text = f'correct!'
            self.parent.current = "main"
        else:
            self.ids.welcome_label.text = f'incorrect!'
            invalidLogin()

    def clear(self):
        url2 = "https://api.airtable.com/v0/appE0EnwZFabOiwUP/Tasks/"
        headers2 = {"Authorization": "Bearer keyonOCTWYREdHmFl"}
        username = self.ids.user.text
        password = self.ids.password.text
        if(username == "" or password == ""):
            invalidForm()
        else:
            body = {
                "records": [
                    {
                        "fields": {
                            "username": username,
                            "password": password
                        }
                    }
                ]
            }
            requests.post(url, headers=headers, json=body)
            self.ids.user.text = ""
            self.ids.password.text = ""
            self.ids.phonenumber.text = ""
            b = 0
            while (b < len(requests.get(url2, headers=headers2).json()['records'])):
                b += 1
            body = {
                "records": [
                    {
                        "fields": {
                            "index": str(b)
                        }
                    }
                ]
            }

            requests.post(url2, headers=headers2, json=body)

    def get_row(self):
        base_id = "appo3z8pFbRIUjN0q"
        table_name = "Login System"
        url = "https://api.airtable.com/v0/" + base_id + "/" + table_name
        api_key = "keyonOCTWYREdHmFl"
        headers = {"Authorization": "Bearer " + api_key}
        response = requests.get(url, headers=headers)
        rows = response.json()['records']
        c = 0
        rnum = 0
        for row in rows:
            if row['fields']['username'] == self.ids.user.text:
                if row['fields']['password'] == self.ids.password.text:
                    rnum = c
            c += 1
        return rnum





class CustomizationOne(Screen):
    def on_touch_move(self, touch):
        if touch.x < touch.ox:
            self.parent.current = "customization2"

class CustomizationTwo(Screen):
    def on_touch_move(self, touch):
        if touch.x < touch.ox:
            self.parent.current = "customization3"

class CustomizationThree(Screen):
    def on_touch_move(self, touch):
        if touch.x < touch.ox:
            self.parent.current = "customization4"

class CustomizationFour(Screen):
    def on_touch_move(self, touch):
        if touch.x < touch.ox:
            self.parent.current = "home"

class HomeScreen(Screen):
    url = "https://api.airtable.com/v0/appE0EnwZFabOiwUP/Tasks/"
    headers = {"Authorization": "Bearer keyonOCTWYREdHmFl"}
    tasks = requests.get(url, headers=headers).json()['records']

    def on_touch_move(self, touch):
        if touch.x < touch.ox:
            self.parent.current = "main"

    def feed(self):
        current = self.ids.money_bar.value
        health = self.ids.health_bar.value
        health += 10
        current -= 5
        self.ids.money_bar.value = current
        self.ids.health_bar.value = health
    def constant_health(self):
        Clock.schedule_interval(self.add_health, 120)
    def add_health(self, dt):
        health = self.ids.health_bar.value
        health -= 1
        self.ids.health_bar.value = health
    def show_bubbles(self, dt):
        self.ids.bubbles.opacity = 1
    def delete_bubbles(self, dt):
        self.ids.bubbles.opacity = 0
    def update_poop(self):
        if(self.ids.health_bar.value <= 20):
            self.ids.poop3.opacity = 1
        if(self.ids.health_bar.value <= 30):
            self.ids.poop2.opacity = 1
        if(self.ids.health_bar.value <= 40):
            self.ids.poop1.opacity = 1

    def take_bath(self):
        Clock.schedule_once(self.show_bubbles, .01)
        Clock.schedule_once(self.delete_bubbles, 1.5)
        current = self.ids.money_bar.value
        health = self.ids.health_bar.value
        current -= 10
        health += 20
        self.ids.money_bar.value = current
        self.ids.health_bar.value = health
        if(self.ids.health_bar.value > 40):
            self.ids.poop1.opacity = 0
        if(self.ids.health_bar.value > 30):
            self.ids.poop2.opacity = 0
        if(self.ids.health_bar.value > 20):
            self.ids.poop3.opacity = 0


class TodoCard(FakeRectangularElevationBehavior, MDFloatLayout):
    def remove_content(self, instance):
        the_parent = self.parent
        text = self.ids.description.text
        user = the_parent.parent.parent.parent.parent.get_screen('login').get_row()
        url = "https://api.airtable.com/v0/appE0EnwZFabOiwUP/Tasks/"
        headers = {"Authorization": "Bearer keyonOCTWYREdHmFl"}
        tasks = requests.get(url, headers=headers).json()['records']
        counter = 0
        c = 0
        for a in tasks:
            index = a['fields']['index']
            if int(index) == int(user):
                id = requests.get(url, headers=headers).json()['records'][counter]['id']
                print(tasks[counter]['fields'][str(len(tasks[counter]['fields'])-2)])
                if(text == tasks[counter]['fields'][str(len(tasks[counter]['fields'])-2)]):
                    body = {
                        "records": [
                            {
                                "id": id,
                                "fields": {
                                    str(len(tasks[counter]['fields'])-2): ""
                                }
                            }
                        ]
                    }
                    requests.patch(url, headers=headers, json=body)
                else:
                    for b in range(0, len(tasks[counter]['fields']), 1):
                        if(tasks[counter]['fields'][str(b)] == text):
                            body = {
                                "records": [
                                    {
                                        "id": id,
                                        "fields": {
                                            str(b): tasks[counter]['fields'][str(b+1)]
                                        }
                                    }
                                ]
                            }
                            requests.patch(url, headers=headers, json=body)
                            while(b < len(tasks[counter]['fields'])-2):
                                body = {
                                    "records": [
                                        {
                                            "id": id,
                                            "fields": {
                                                str(b): tasks[counter]['fields'][str(b + 1)],
                                                str(len(tasks[counter]['fields']) - 2): ""
                                            }
                                        }
                                    ]
                                }
                                b += 1
                                requests.patch(url, headers=headers, json=body)
                            break
                break
            counter += 1
        the_parent.remove_widget(instance)
        the_parent.parent.parent.parent.parent.get_screen("addscreen").cancel_event()



class ToDoScreen(Screen):
    task_increment = 0
    habit_increment = 0

    def on_touch_move(self, touch):
        if touch.x < touch.ox:
            self.parent.current = "home"

    def add_task(self):
        url = "https://api.airtable.com/v0/appE0EnwZFabOiwUP/Tasks/"
        headers = {"Authorization": "Bearer keyonOCTWYREdHmFl"}
        user = self.parent.get_screen('login').get_row()
        num = -1
        i = 0
        tasks = requests.get(url, headers=headers).json()['records']
        counter = 0
        for a in tasks:
            index = a['fields']['index']
            if int(index) == int(user):
                id = requests.get(url, headers=headers).json()['records'][counter]['id']
                break
            counter += 1
        while (i < len(tasks[counter]['fields'])):
            num += 1
            i += 1
        body = {
            "records": [
                {
                    "id": id,
                    "fields": {
                        str(num): self.parent.get_screen('addscreen').get_name()
                    }
                }
            ]
        }

        requests.patch(url, headers=headers, json=body)


    def setting_screen(self):
        url = "https://api.airtable.com/v0/appE0EnwZFabOiwUP/Tasks/"
        headers = {"Authorization": "Bearer keyonOCTWYREdHmFl"}
        user = self.parent.get_screen('login').get_row()
        tasks = requests.get(url, headers=headers).json()['records']
        counter = 0
        for a in tasks:
            index = a['fields']['index']
            if int(index) == int(user):
                break
            counter += 1
        if(tasks[counter]['fields']['0'] != ""):
            for b in range(0, len(tasks[counter]['fields'])-1, 1):
                n = tasks[counter]['fields'][str(b)]
                self.add_old_todo(n, b+1)

    def add_todo(self, name, habit):
        if habit:
            self.habit_increment += 1
            the_habit = TodoCard()
            the_habit.ids.task_number.text = f'Habit {self.habit_increment}'
            the_habit.ids.description.text = name
            self.ids.todo_list.add_widget(the_habit)
        else:
            self.task_increment += 1
            the_task = TodoCard()
            the_task.ids.task_number.text = f'Task {self.task_increment}'
            the_task.ids.description.text = name
            self.ids.todo_list.add_widget(the_task)
        self.add_task()
    def add_old_todo(self, name, num):
        the_task = TodoCard()
        self.task_increment = num
        the_task.ids.task_number.text = f'Task {num}'
        the_task.ids.description.text = name
        self.ids.todo_list.add_widget(the_task)
    def get_increment(self):
        return self.task_increment



class AddScreen(Screen):
    a_task = True
    a_habit = False
    name_in_q = ""
    time = ""
    event = ""

    def task_button(self):
        self.a_task = True
        self.a_habit = False
        self.ids.task_button_display.background_color = (0,0.5,0,1)
        self.ids.habit_button_display.background_color = (0.9,0.9,0.9,1)




    def habit_button(self):
        self.a_habit = True
        self.a_task = False
        self.ids.habit_button_display.background_color = (0, 0.5, 0, 1)
        self.ids.task_button_display.background_color = (0.9, 0.9, 0.9, 1)

    def submit_button(self):
        self.name_in_q = self.ids.the_name.text
        self.time = f'{self.ids.time_spinner_1.text}:{self.ids.time_spinner_2.text} {self.ids.time_spinner_3.text}'

        tz_hous = pytz.timezone('America/Chicago')
        the_current_hour = datetime.now(tz_hous).strftime("%I")
        the_current_minutes = datetime.now(tz_hous).strftime("%M")
        start_time = int(the_current_hour) * 60 + int(the_current_minutes)
        sched_hour = int(self.ids.time_spinner_1.text)
        sched_minute = int(self.ids.time_spinner_2.text)
        end_time = sched_hour * 60 + sched_minute
        duration = end_time - start_time
        if duration < 0:
            duration = duration + 1440
        time_elapsed_seconds = duration * 60
        self.event = Clock.schedule_once(self.send_message, time_elapsed_seconds)

        self.ids.the_name.text = "Name"
        self.ids.time_spinner_1.text = "1"
        self.ids.time_spinner_2.text = "00"
        self.ids.time_spinner_3.text = "AM"


    def get_name(self):
        return self.name_in_q

    def get_time(self):
        return self.time

    def get_task_status(self):
        return self.a_task

    def get_habit_status(self):
        return self.a_habit

    def cancel_event(self):
        Clock.unschedule(self.event)

    def send_message(self, time):
        account_id = "AC1ae9e3ecdd730708bdfe8ba5889e7cb7"
        auth_token = "c32286086a4e0f9dbe55cea229f99922"
        client = Client(account_id, auth_token)
        client.messages.create(
            body=f"Complete your task: {self.name_in_q} for {self.time}",
            from_="+13344014430",
            to="+12812487183"
        )


class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        kv = Builder.load_file("login.kv")
        return kv




if __name__ == "__main__":
    MainApp().run()
