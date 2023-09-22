from models.base_model import BaseModel
from models.place import Place
from console import HBNBCommand
from models import storage
import re
import shlex


def do_create(self, args):
    "create an object for a given class"
    if not args:
        print("** class name missing **")
        return False
    
    args_list = shlex.split(args)
    class_name = args_list[0]

    if class_name not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return False
    
    new_instance = HBNBCommand.classes[class_name]()

    for arg in args_list[1:]:
        param_value = arg
        param_value = arg.split("=")
        param = param_value[0]
        value = param_value[1]

        # replace _ with a space and remove any double quotes
        value = value.replace("_", " ").replace('"', '\\"')

        if '.' in value:
            value = float(value)
        elif value.isdigit():
            value = int(value)
        else:
            setattr(new_instance, param, value)

    new_instance.save()
    print(new_instance.id)

