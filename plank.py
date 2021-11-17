import requests
import json
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

url = 'https://tenbis-static.azureedge.net/restaurant-menu/19156_en'
response = requests.get(url)


class Drinks(Resource):
    def get(self):
        res = []
        for drink in response.json()["categoriesList"][-1]["dishList"]:
            res.append(drink["dishId"])
            res.append(drink["dishName"])
            res.append(drink["dishDescription"])
            res.append(drink["dishPrice"])
        return {'DRINKS': res}, 200
        
api.add_resource(Drinks, '/drinks')

class Drink(Resource):
    def get(self, id):
        res = []
        for drink in response.json()["categoriesList"][-1]["dishList"]:
            if drink["dishId"] == id:
                res.append(drink["dishId"])
                res.append(drink["dishName"])
                res.append(drink["dishDescription"])
                res.append(drink["dishPrice"])
        return {'DRINK': res}, 200
        
api.add_resource(Drink, '/drink/<int:id>')



class Pizzas(Resource):
    def get(self):
        res = []
        for drink in response.json()["categoriesList"][3]["dishList"]:
            res.append(drink["dishId"])
            res.append(drink["dishName"])
            res.append(drink["dishDescription"])
            res.append(drink["dishPrice"])
        return {'PIZZAS': res}, 200

api.add_resource(Pizzas, '/pizzas')

class Pizza(Resource):
    def get(self, id):
        res = []
        for pizza in response.json()["categoriesList"][3]["dishList"]:
            if pizza["dishId"] == id:
                res.append(pizza["dishId"])
                res.append(pizza["dishName"])
                res.append(pizza["dishDescription"])
                res.append(pizza["dishPrice"])
        return {'DRINK': res}, 200
        
api.add_resource(Pizza, '/pizza/<int:id>')



class Desserts(Resource):
    def get(self):
        res = []
        for drink in requests.get(url).json()["categoriesList"][4]["dishList"]:
            res.append(drink["dishId"])
            res.append(drink["dishName"])
            res.append(drink["dishDescription"])
            res.append(drink["dishPrice"])
        return {'DESSERTS': res}, 200

api.add_resource(Desserts, '/desserts')

class Dessert(Resource):
    def get(self, id):
        res = []
        for dessert in response.json()["categoriesList"][4]["dishList"]:
            if dessert["dishId"] == id:
                res.append(dessert["dishId"])
                res.append(dessert["dishName"])
                res.append(dessert["dishDescription"])
                res.append(dessert["dishPrice"])
        return {'DESSERT': res}, 200
        
api.add_resource(Dessert, '/dessert/<int:id>')



class Order(Resource):
    def post(self):
        drinkList = response.json()["categoriesList"][-1]["dishList"]
        pizzaList = response.json()["categoriesList"][3]["dishList"]
        dessertList = response.json()["categoriesList"][4]["dishList"]

        total = 0
        parser = reqparse.RequestParser()
        parser.add_argument('drinks', required=False)
        parser.add_argument('desserts', required=False)
        parser.add_argument('pizzas', required=False)
        
        args = parser.parse_args()

        new_data = {
            'drinks': args['drinks'],
            'desserts': args['desserts'],
            'pizzas': args['pizzas']
        }

        for i in range(0, len(drinkList)):
            if new_data["drinks"] == drinkList[i]["dishName"]:
                total += drinkList[i]["dishPrice"]
                
        for i in range(0, len(dessertList)):
            if new_data["desserts"] == dessertList[i]["dishName"]:
                total += dessertList[i]["dishPrice"]

        for i in range(0, len(pizzaList)):
            if new_data["pizzas"] == pizzaList[i]["dishName"]:
                total += pizzaList[i]["dishPrice"]

        return {'price': total}, 200

api.add_resource(Order, '/order')



if __name__ == '__main__':
    app.run()

