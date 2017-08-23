#!/usr/bin/env python

import nest

# Example of uses
def set_duration(duration=15):
    if nest.get_variable('is_online') == True:
        if nest,get_variable('has_fan') == True:
            nest.get_variable('fan_timer_duration', duration)
            return True
    return False

def fan_on():
    if nest.get_variable('is_online') == True:
        if nest.get_variable('has_fan') == True:
            print nest.set_variable('fan_timer_active', True)
            return True
    return False

def is_running():
    if nest.get_variable('is_online') == True:
        if nest.get_variable('hvac_state') != 'off':
            return True
    return False

def too_damn_hot():
    if arrow.get(get_timeout()) < arrow.now():
        if not is_running():
            set_duration()
            fan_on()

if __name__ == '__main__':
    print is_running()

