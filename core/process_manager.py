process_list = []

def register_process(name):
    process_list.append(name)

def unregister_process(name):
    if name in process_list:
        process_list.remove(name)

def get_processes():
    return process_list