import random

x1 = {
    "x11": 0,
    "x12": 0,
    "x13": 0,
    "x14": 0,
    "x15": 0,
    "x16": 0,
    "x17": 0,
    "x18": 0,
    "x19": 0
}

x2 = {
    "x21": 0,
    "x22": 0,
    "x23": 0,
    "x24": 0,
    "x25": 0,
    "x26": 0,
    "x27": 0,
    "x28": 0,
    "x29": 0
}

x3 = {
    "x31": 0,
    "x32": 0,
    "x33": 0,
    "x34": 0,
    "x35": 0,
    "x36": 0,
    "x37": 0,
    "x38": 0,
    "x39": 0
}

board = {
    "x1": x1,
    "x2": x2,
    "x3": x3
}

for x in board:
    
    if x1["x11"] == 0:
        num = random.randint(1, 9)
        x1["x11"] = num
        if x1["x12"] == 0:
            for x in board:
                num = random.randint(1, 9)
                if x1["x11"] != num:
                    x1["x12"] = num
                    for x in board:
                        num = random.randint(1, 9)
                        if x1["x13"] == 0 and x1["x11"] != num and x1["x12"] != num:
                            x1["x13"] = num
                        
    for x in board:
        num = random.randint(1, 9)
        if x2["x21"] == 0 and num != x1["x11"] and num != x1["x12"] and num != x1["x13"]:
            x2["x21"] = num
            for x in board:
                num = random.randint(1, 9)
                if x2["x22"] == 0 and num != x1["x11"] and num != x1["x12"] and num != x1["x13"] and num != x2["x21"]:
                    x2["x22"] = num
                    for x in board:
                        num = random.randint(1, 9)
                        if x2["x23"] == 0 and num != x1["x11"] and num != x1["x12"] and num != x1["x13"] and num != x2["x21"] and num != x2["x22"]:
                            x2["x23"] = num
    
    for x in board:
        num = random.randint(1, 9)
        if x3["x31"] == 0 and num != x1["x11"] and num != x1["x12"] and num != x1["x13"] and num != x2["x21"] and num != x2["x22"] and num != x2["x23"]:
            x3["x31"] = num
            for x in board:
                num = random.randint(1, 9)
                if x3["x32"] == 0 and num != x1["x11"] and num != x1["x12"] and num != x1["x13"] and num != x2["x21"] and num != x2["x22"] and num != x2["x23"] and num != x3["x31"]:
                    x3["x32"] = num
                    for x in board:
                        num = random.randint(1, 9)
                        if x3["x33"] == 0 and num != x1["x11"] and num != x1["x12"] and num != x1["x13"] and num != x2["x21"] and num != x2["x22"] and num != x2["x23"] and num != x3["x31"] and num != x3["x32"]:
                            x3["x33"] = num

    print(x1)
    print(x2)
    print(x3)
