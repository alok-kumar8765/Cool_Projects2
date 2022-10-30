from time import time


def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1]==words[i+1]) & (inwords[i-1]==words[i-1]):
                    continue
                else:
                    errors +=1
            else:
                errors +=1
    return errors

def speed(inprompt,stime,etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time
    return speed

def elapsedtime(stime,etime):
    time = etime - stime
    return time

if __name__ == '__main__':
    prompt = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed."
    print("Type This : '", prompt)
    input("Press Enter when you ready to Start\n\n")
    stime = time()
    inprompt = input()
    etime = time()

    time = round(elapsedtime(stime,etime))
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)

    print('#####################################')
    print("Total time elapsed : ", time,"second")
    print('your average speed', speed)
    print('total errors: ', errors)
    print('#####################################')
