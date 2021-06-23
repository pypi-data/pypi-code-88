import logging
import time

from sielc_dompser.autosampler.autosampler import Autosampler, ProtocolError

# todo find out the angle for the arm to be over the waste port

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    port = 'COM5'
    # autosampler = Autosampler(port)

    # protocol A - system
    # autosampler.firmware_version()

    # protocol B

    # protocol C
    # autosampler.home_tray_arm()  # not protocol c but the tray should be in the home position
    # autosampler.recalibrate_arm()
    # for i in [90, 45]:
    #     autosampler.arm_angle(i)
    # autosampler.arm_to_injection_port()

    # protocol D - tray
    ## for i in range(0, 4):
    ## autosampler.shaking_mode(i)  # todo setting shaking mode to anything but 0 isnt working?
    ##     autosampler.shaking_duration(i)
    ##     autosampler.command_state_shake()  # todo doesnt seem like it shakes for the set duration... or maybe its
    # because shaking mode is stuck on no shaking
    ##     time.sleep(i)

    # protocol F - needle
    # autosampler.washing()  # todo not working getting absent property error, why?!!
    # autosampler.start_washing()  # todo not working getting absent property error, why?!!
    # autosampler.stop_washing()  # todo not working getting absent property error, why?!!

    # protocol E - tray and arm
    # # autosampler.recalibrate_tray_arm()  # todo get error, 10001 is too big?
    # autosampler.home_tray_arm()
    # autosampler.move_tray_arm(3)
    # autosampler.vial_number()
    # autosampler.needle_min_y()
    # autosampler.move_tray_arm(20)
    # autosampler.vial_number()
    # autosampler.home_tray_arm()
    # try:
    #     autosampler.move_tray_arm(50)
    # except ProtocolError:
    #     pass

    # protocol F - needle
    # autosampler.recalibrate_needle()
    # autosampler.needle_max_y()
    # autosampler.needle_min_y()

    # protocol G - valve
    # autosampler.recalibrate_valve()
    # autosampler.valve_position()
    # autosampler.valve_position(1)
    # autosampler.valve_position(2)
    # # todo with the autosampler being tested, seems like only positions that can be set are only 1 and 2
    # try:
    #     autosampler.valve_position(6)
    # except ProtocolError:
    #     pass

    # # protocol H - syringe
    # autosampler.recalibrate_plunger()
    # autosampler.plunger_position()
    # autosampler.plunger_position(1000)
    # autosampler.zero_plunger()
    # autosampler.plunger_position(1000)
    # autosampler.zero_plunger(wait=False)
    # time.sleep(1)
    # autosampler.stop_plunger()
    # autosampler.plunger_position()
    # todo seems like after stopping the plunger, it will need to be recalibrated because the autosampler will not
    #  know what the plunger position after it has been stopped
    # autosampler.recalibrate_plunger()
    # autosampler.plunger_position()

    # # protocol I - fan
    # autosampler.fan_speed()
    # autosampler.fan_speed(50)
    # autosampler.fan_speed()
    # autosampler.fan_speed(100)
    # autosampler.fan_speed()
    # autosampler.fan_speed(65)
    # autosampler.fan_speed()

    print('done')
