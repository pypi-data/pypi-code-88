# -*- coding: utf-8 -*-
import inspect
import sys


def all_classes_name(module: str):
	clsmembers = inspect.getmembers(sys.modules[module], inspect.isclass)
	result = []
	for class_tuple in clsmembers:
		result.append(class_tuple[0])
	return result




def singleton(class_):
	instances = {}

	def get_instance(*args, **kwargs):
		if class_ not in instances:
			instances[class_] = class_(*args, **kwargs)
		return instances[class_]

	return get_instance
