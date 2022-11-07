import requests
import PySimpleGUI as gui


#put the path of the Images here
path = ''
def Weather():
   
    api_key = '30d4741c779ba94c470ca1f63045390a'
    
    playout=[
                [
                    [gui.Text("Enter City: ")],
                    [gui.InputText(key='weather'),gui.Button(image_filename=path+"/p.png",image_size=(200,200),key='OK')],
                    [gui.Text("The weather is: ",key='wet')],
                    [gui.Text("The temperature is: ",key='temp')]
                ]
            ]
    wp=gui.Window(title='Weather App',layout=playout,size=(550,300))

    while True:
        events,values=wp.read()
        if values is not None:
            user_input=values['weather']

        if events==gui.WIN_CLOSED:
            break
        if events=='OK':
            weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            wp["wet"].update(f"City not found")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            temp2=(temp-30)/2
            wp["wet"].update(f"The weather in {user_input} is: {weather}")
            wp["temp"].update(f"The temperature in {user_input} is: {temp2}ºC")
            if weather == 'Clouds':
                wp["OK"].update(image_filename=path+"/clouds.png",image_size=(200,200))
            if weather == 'Clear':
                wp["OK"].update(image_filename=path+"/clear.png",image_size=(200,200))
        

    wp.close()
    
Weather()