from dishamodule import show

# __name__ is a special built-in variable in Python
#
# Case 1: If this file is run directly: (i.e. dishamodule.py is executed directly)
# __name__ = "__main__" --> ptyhon sets this variable name to "__main__"
# -> if block executes
#
# Case 2: If this file is imported in another file (i.e. 08_main.py - in which we have imported dishamodule.py):
# __name__ = module_name (example: "dishamodule") --> Python sets __name__ as the module name 
# whenever this file is called from another file using an import statement.
# -> if block does NOT execute 
#
# Therefore:
# if __name__ == "__main__":
# is used to run code only when file is executed directly,
# not when imported as a module.