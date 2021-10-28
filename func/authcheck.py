import time

tokens = []


async def checkauthtime(x, u):
    global tokens
    print(tokens)
    for tp in tokens:
        for k in tp:
            if k == u :
                if x and tp[k]==x:
                    t = x[4:6] + x[8:11] + x[14:17] + x[24:]
                    print(t + " *** " + str(int(time.time())))
                    if int(t) > int(time.time()):
                        return True
    return False


async def updateoldtk(x, c):
    global tokens
    updated = False
    for tk in tokens:
        p = tk
        for k in p:
            if k == x:
                tk[x] = c
                updated = True
    if not updated:
        tokens += [{x: c}]
    return tokens
