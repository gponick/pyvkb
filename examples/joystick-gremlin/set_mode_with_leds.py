import gremlin
from gremlin.user_plugin import * 

from vkb.devices import find_all_vkb
from vkb.devices import gladiatornxt
from vkb.led import hex_color_to_vkb_color, ColorMode, LEDMode

devs = find_all_vkb()
nxt = devs[0]

def set_guns():
    nxt.set_led(
            nxt.LED_TOP,
            color1='#00FF00',
            color_mode=ColorMode.COLOR1,
            led_mode=LEDMode.CONSTANT,
        )

def set_missiles():
    nxt.set_led(
            nxt.LED_TOP,
            color1='#00FFFF',
            color_mode=ColorMode.COLOR1,
            led_mode=LEDMode.CONSTANT,
        )




toggle_button = PhysicalInputVariable(
        "Button that toggles modes",
        "Button that toggles modes",
        [gremlin.common.InputType.JoystickButton]
)


mode_list = gremlin.control_action.ModeList( ["Guns", "Missiles"] )

toggle_button_default = toggle_button.create_decorator("Default")
toggle_button_guns = toggle_button.create_decorator("Guns")
toggle_button_missiles = toggle_button.create_decorator("Missiles")

@toggle_button_default.button(toggle_button.input_id)
def toggle_button_default_to_missiles(event, vjoy):
    if event.is_pressed:
        gremlin.util.log("Switching to Missiles from Default")
        gremlin.control_action.cycle_modes(mode_list)
        set_missiles()
        #gremlin.control_action.switch_mode("Missiles")

@toggle_button_missiles.button(toggle_button.input_id)
def toggle_button_missiles_to_guns(event, vjoy):
    if event.is_pressed:
        gremlin.util.log("Switching to Guns from Missiles")
        set_guns()
        gremlin.control_action.cycle_modes(mode_list)
        #gremlin.control_action.switch_mode("Guns")


@toggle_button_guns.button(toggle_button.input_id)
def toggle_button_guns_to_missiles(event, vjoy):
    if event.is_pressed:
        gremlin.util.log("Switching to Missiles from Guns")
        set_missiles()
        gremlin.control_action.cycle_modes(mode_list)
        #gremlin.control_action.switch_mode("Missiles")