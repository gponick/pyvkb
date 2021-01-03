import gremlin
from gremlin.user_plugin import * 

from vkb.devices import find_all_vkb
from vkb.devices import gladiatornxt
from vkb.led import hex_color_to_vkb_color, ColorMode, LEDMode



devs = find_all_vkb()
nxt = devs[0]


toggle_button = PhysicalInputVariable(
        "Button that toggles modes",
        "Button that toggles modes",
        [gremlin.common.InputType.JoystickButton]
)

mode_1 = ModeVariable(
    "Mode 1",
    "Mode 1"
)

mode_2 = ModeVariable( 
    "Mode 2",
    "Mode 2"
)

mode_default = ModeVariable(
    "Mode Default",
    "Mode Default"
)

mode_1_color = StringVariable(
    "Mode_1 Color",
    "Mode_1 Color",
    "#00FFFF"
)

mode_2_color = StringVariable(
    "Mode_2 Color",
    "Mode_2 Color",
    "#00FF00"
)

mode_1.value = "Missiles"
mode_2.value = "Guns"
mode_default.value = "Default"

def set_mode_1():
    nxt.set_led(
            nxt.LED_TOP,
            color1=mode_1_color.value,
            color_mode=ColorMode.COLOR1,
            led_mode=LEDMode.CONSTANT,
        )

def set_mode_2():
    nxt.set_led(
            nxt.LED_TOP,
            color1=mode_2_color.value,
            color_mode=ColorMode.COLOR1,
            led_mode=LEDMode.CONSTANT,
        )


mode_list = gremlin.control_action.ModeList( [mode_1.value, mode_2.value] )

toggle_button_default = toggle_button.create_decorator(mode_default.value)
toggle_button_mode_1 = toggle_button.create_decorator(mode_1.value)
toggle_button_mode_2 = toggle_button.create_decorator(mode_2.value)

@toggle_button_default.button(toggle_button.input_id)
def toggle_button_default_to_mode_1(event, vjoy):
    if event.is_pressed:
        gremlin.util.log(f"Switching to {mode_1.value} from {mode_default.value}!")
        gremlin.control_action.cycle_modes(mode_list)
        set_mode_1()

@toggle_button_mode_1.button(toggle_button.input_id)
def toggle_button_mode_1_to_mode_2(event, vjoy):
    if event.is_pressed:
        gremlin.util.log(f"Switching to {mode_2.value} from {mode_1.value}")
        set_mode_2()
        gremlin.control_action.cycle_modes(mode_list)


@toggle_button_mode_2.button(toggle_button.input_id)
def toggle_button_mode_2_to_mode_1(event, vjoy):
    if event.is_pressed:
        gremlin.util.log(f"Switching to {mode_1.value} from {mode_2.value}")
        set_mode_1()
        gremlin.control_action.cycle_modes(mode_list)


