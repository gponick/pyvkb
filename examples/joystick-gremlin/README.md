# Joystick Gremlin Plugin for use with pyvkb

Joystick Gremlin: https://whitemagic.github.io/JoystickGremlin/

This is a plugin for Joystick Gremlin that will alternate between two Joystick Gremlin modes (configurable) with a button press (configurable) and change the top LED of your first VKB Joystick device to the appropriate mode color (configurable).

## How to use

### Requirements
You'll need to put the following packages in your `c:\users\<user>\documents\joystick-gremlin\` directory:
_(This is the default path for Joystick Gremlin's python setup)._

- typing
- pygments
- pygments
- pywinusb
- pyglet
- prompt_toolkit
- libpasteurize 
- nubia
  - nubia_complete (from nubia package)
- ordlookup
- past
- prettytable
- future
- jellyfish
- libfuturize
- altgraph
- bitstruct
- wcwidth

Then put the `set_modes_with_leds.py` file into the same directory.

### Usage

Import it into your user plugins and set the appropriate options. Enjoy! 