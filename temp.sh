# how to install python packages in linux with pip

# The command 'pip install package_name' install packages in a user folder, 
# that means the package is installed only for the current user and not system-wide (for all the users)

# What "Defaulting to user installation because normal site-packages is not writeable" means?
# This message means that pip is defaulting to installing the package in the user-level site-packages
# directory because it does not have permission to write to the system-level site-packages directory

# How do I check which packages are installed in user-level site-packages?
ls /home/`whoami`/.local/lib/python3.9/site-packages

# How do I check which packages are installed in system-level site-packages?
ls /usr/lib/python3.9/site-packages

