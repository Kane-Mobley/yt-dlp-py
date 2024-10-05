import os
package = "inquirer"
try:
    import inquirer
    print(package+" has been installed already")
    input("Press enter to close...")
except:
    print("Package not available, running install command")
    os.system("pip install "+ package)
    input("Press enter to close...")