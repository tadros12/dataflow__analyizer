import os

def create_folder(path):
    for i in range (20):
        inner_path = os.path.join(path,"dir"+str(i))
        if not os.path.exists(inner_path):
            os.makedirs(inner_path)


