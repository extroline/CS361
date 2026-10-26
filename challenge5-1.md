<!-- Let's come up with the system interface definitions for an elevator!

The elevator is a cable type—suspended by a counter-weighted cable with the motor fixed at the top of the shaft. This motor is controlled by an external computer.

We also have a computer in the car that is wired to:

The buttons
A screen showing the current floor number
A bell
The doors
A position sensor (that tells us what floor the car is at)
The elevator lift motor controller computer
What to Do
We're going to define the interfaces for two systems:

The on-car computer
The lift motor computer
The on-car computer has both inputs and outputs. You can split these into two sections. For the input, you might have a function called handle_button_press(button: int), for example.

The goal here is to come up with the function signatures and types, not the implementation of those functions -->


# Interfaces 

## On Car-Computer
### Input 
```python 
def handle_button_press(button:int):
    return button

def get_weight(total_weight:int):
    return weight 

def get_floor(floorNum:int):
    return floorNum
```
### Output
```python 
doors_status = bool ## True when open false when close 
def doors(button):
    if(handle_button_press(button) == door_button):
        !doors_status


def get_floorNum(floorNum:int):
    return floorNum:int

def weight_overflow(capacity:int):
    if self.get_weight() < capacity: 
        return pass
    else:
        speaker.voice(Over-Weight.mp3)
        raise Exception("Car over weight") 
```
## Lift Motor

