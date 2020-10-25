from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivy.core.window import Window


Window.size = (400,300)
Builder.load_file("main.kv")
class RegistrationWindow(Screen):
	def register(self,user, password):
		with open("usersinformation.json") as file:
			users= json.load(file)
		if user in users:
			self.ids.register_message.text= "'"+ user+ "'" + " already exists. Choose another username!!"
		
		else:
			users[user] ={
				'username': user,
				'password': password
			}

			with open("usersinformation.json", "w") as file:
				json.dump(users, file)
			self.ids.register_message.text= user + " has been created successfully.Sing in now."
		

class DashboardWindow(Screen):
	def search_country(self,country):
		input = country
		with open("countries.txt") as country:
			countries = country.readlines()
		results= []
		for country in countries:
			if input.lower() in country.lower():
				results.append(country)
		
		if results:
			self.ids.founded_countries.text= ''.join(results)
		else:
			self.ids.founded_countries.text= "No country was founded!"
		

class LoginWindow(Screen):
	def authenticate(self,user,password):
		with open("usersinformation.json") as file:
			users= json.load(file)
		if user in users and users[user]["password"]==password:
			print("soheila")
			self.manager.current= "dashboard"
			
			
		else:
			self.ids.message.text= "Username/Password is wrong. Try again!!"

class WindowManager(ScreenManager):
	pass


class MainApp(App):
	def build(self):
		return WindowManager()


if __name__ == "__main__":
	MainApp().run()