from fastapi import FastAPI, Request
app = FastAPI()

# Post_function

usernames = list()


@app.post("/post_data/{user_name}")
def post_data(user_name):
    usernames.append(user_name)
    return{
        "username":usernames
    }