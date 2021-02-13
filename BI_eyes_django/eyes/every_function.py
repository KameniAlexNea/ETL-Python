import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
    print("Modifier ce contenu pour l'utiliser")
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()