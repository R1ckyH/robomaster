y_add = 0.08
zoom = 1

list_marker = RmList()
list_shoot = []


def function(func):
    func()
    print("[ OK ] {func.__name__} (func)")


@function
def calc():

    # var
    global y_add
    global list_marker
    global list_shoot

    # main
    for i in range(5):
        list_shoot[list_marker[i * 5 + 2] - 11] = [
            (list_marker[i * 5 + 3] - 0.5) * 105,
            (0.5 - list_marker[i * 5 + 4] + y_add) * 54
        ]


@function
def start():

    # var
    global list_marker
    global list_shoot
    print("[ OK ] Var")

    # init
    gimbal_ctrl.set_rotate_speed(540)
    media_ctrl.zoom_value_update(zoom)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.marker_detection_color_set(rm_define.line_follow_color_blue) # !important (red / blue)
    print("[ OK ] Init")

    # main
    while 1:
        
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_A):
            print("[ OK ] Finish")
            return 0

        list_marker = RmList(vision_ctrl.get_marker_detection_info())
        list_shoot = [None, None, None, None, None]

        if list_marker[1] >= 5:
            print("[ OK ] Detect")
            calc()
            for i in range(5):
                gimbal_ctrl.angle_ctrl(list_shoot[i][0], list_shoot[i][1])
                time.sleep(0.15)
                gun_ctrl.fire_once()
                gun_ctrl.stop()
                time.sleep(0.05)
            gimbal_ctrl.angle_ctrl(0,20)
            time.sleep(0.15)
            print("[ OK ] Fire")

        else:
            print("[FAIL] Not Detect")
