def get_flag():
    # mmm_pie_is_very_tasty
    # this_flag_is_redacted

    give_flag = False

    if give_flag:
        x = [ 0x09, 0x09, 0x09, 0x3b, 0x14, 0x0d, 0x01, 0x3b, 0x0d, 0x17, 0x3b, 0x12, 0x01, 0x16, 0x1d, 0x3b, 0x10, 0x05, 0x17, 0x10, 0x1d ]
    else:
        x = [ 0x10, 0x0c, 0x0d, 0x17, 0x3b, 0x02, 0x08, 0x05, 0x03, 0x3b, 0x0d, 0x17, 0x3b, 0x16, 0x01, 0x00, 0x05, 0x07, 0x10, 0x01, 0x00 ]

    fl = "".join([ chr(i ^ 0x64) for i in x ])

    return "CTF{" + fl + "}"
