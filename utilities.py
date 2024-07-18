import time

def pause(seconds: float, statement: str):
    print("\n" + statement)
    time.sleep(seconds)

def start(statement: str):
    pause(2, statement)

def completion(seconds: int):
    pause(1, "Finished phase " + str(seconds))

def step(statement: str):
    pause(0.5, " ~ " + statement)
