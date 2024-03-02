import os

# Get the current directory
current_directory = os.path.dirname(__file__)

# Import all modules in the current directory
for module_file in os.listdir(current_directory):
    if module_file == '__init__.py' or not module_file.endswith('.py'):
        continue

    # Import the module dynamically
    module_name = module_file[:-3]
    __import__(f'recipes.{module_name}', locals(), globals())

# Clean up the namespace
del module_file, module_name
