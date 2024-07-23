#!/usr/bin/python3
"""The Base class modul"""
import json
import os
import csv


class Base:
    """Base class
        private class attribute __nb_objects = 0"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize attricutes

            args: id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that returns:
        the JSON string representation of list_dictionaries
        list_dictionaries is a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that:
        writes the JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of Base"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        json_txt = cls.to_json_string(list_objs)
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="UTF8") as f:
            f.write(json_txt)

    @staticmethod
    def from_json_string(json_string):
        """a static method that:
        returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """a class method that:
        returns an instance with all attributes already set
        **dictionary can be thought of as a double pointer to a dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """a class method that:
        returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r', encoding="UTF8") as f:
            return [cls.create(**n) for n in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """a class method to serializes in CSV"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w') as f:
            csv_txt = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_txt.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                        ])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_txt.writerow([
                        obj.id,
                        obj.size,
                        obj.x,
                        obj.y
                        ])

    @classmethod
    def load_from_file_csv(cls):
        """a class method to deserializes in CSV"""
        filename = "{}.csv".format(cls.__name__)
        list_objs = []
        with open(filename, 'r') as f:
            txt = csv.reader(f)
            for line in txt:
                if cls.__name__ == "Rectangle":
                    obj = cls(
                            int(line[0]),
                            int(line[1]),
                            int(line[2]),
                            int(line[3]),
                            int(line[4])
                            )
                elif cls.__name__ == "Square":
                    obj = cls(
                            int(line[0]),
                            int(line[1]),
                            int(line[2]),
                            int(line[3])
                            )
                list_objs.append(obj)
                return list_objs
