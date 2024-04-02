#!/usr/bin/python3
import fliclib
import requests

client = fliclib.FlicClient("localhost")

buttons = {
    "80:e4:da:7c:5d:fb": "button1", 
    "80:e4:da:7c:74:19": "button2", 
    "80:e4:da:7c:78:66": "button3" 
}

tables = {
    "button1": "dKN6a8rsZyHmmGVTuyk4",
    "button2": "632VErZVzQUaK4brLuQ0",
    "button3": "N2Rnx8MAp5iFwurlx0o8"
}

def belleatInterface(addr, click_type):
    button = buttons[addr]
    click_type = click_type.split(".")[1]
    url = f"http://localhost:3000/api/request?tableId={tables[button]}&onRequest="
    if click_type == "ButtonClick":
        response = requests.post(url + "true")
    if click_type == "ButtonHold":
        response = requests.post(url + "false")

def got_button(bd_addr):
    cc = fliclib.ButtonConnectionChannel(bd_addr)
    cc.on_button_click_or_hold = \
            lambda channel, click_type, was_queued, time_diff: \
                    belleatInterface(channel.bd_addr, str(click_type))
    client.add_connection_channel(cc)

def got_info(items):
    print(items)
    for bd_addr in items["bd_addr_of_verified_buttons"]:
            got_button(bd_addr)

client.get_info(got_info)

client.on_new_verified_button = got_button

client.handle_events()


