from fastapi import FastAPI, Request
app = FastAPI()
from enum import Enum

@app.get("/addTwoValue")
def submitStudent():
    firstNum = 7
    secondNum = 6
    sum = firstNum + secondNum
    return sum


@app.get("/addThreeValue")
def submitStudent():
    firstNum = 7
    secondNum = 6
    thirdNum = 10
    sum = firstNum + secondNum + thirdNum
    return sum

@app.get("/")
def submitStudent():
    return "Nothing to print"

@app.get("/books/{book_id}")
def get_book_by_id(book_id):
    return {"book_id": book_id}


@app.get("/addTwoValue/{firstNum}/{secondNum}")
def submitStudent(firstNum,secondNum):
    sum = int(firstNum)+ int(secondNum)
    return sum
    
#path parameters with types
@app.get("/addTwoValue/{firstNum}/{secondNum}")
def submitStudent(firstNum:int,secondNum:int):
    sum = firstNum+ secondNum
    return sum


# Get_items
class Availablecountries(str, Enum):
    indian = "Indian"
    american = "American"
    italian = "Italian"


food_items = {"Indian":["Idli", "Dosa"],
        "American":["Hot Dog", "Apple Pie"],
        "Italian":["Pizza", "Berger"]}

@app.get("/get_items/{country}")
async def get_items(country:Availablecountries):
    print(food_items)
    return food_items.get(country)


# get_Coupon_code
coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return { 'discount_amount': coupon_code.get(code) }




usernames = list()
# Put_Function
@app.put("/put_data/{user_name}")
def put_data(user_name):
    usernames.append(user_name)
    print(usernames)
    return {
        "user_name":user_name
    }

# Post_function
@app.post("/post_data/{user_name}")
def post_data(user_name):
    usernames.append(user_name)
    return{
        "username":usernames
    }

@app.delete("/delete_data/{user_name}")
def delete_user(user_name):
    usernames.remove(user_name)
    return {
        "username":usernames
    }