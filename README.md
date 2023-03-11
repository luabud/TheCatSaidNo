This is a Useful Website written in Flask for demo purposes.

## Set up

- Clone this repository 
- Open it in [Visual Studio Code](https://code.visualstudio.com/). You can do that by launching VS Code and running **File** > **Open Folder...**, and selecting the cloned project. 
- Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Make sure you have Python >= 3.8 installed. If not, install it from [python.org](https://www.python.org/downloads/).
- Open the `app.py` file to activate the Python extension.
- Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run the **Python: Create Environment** command to create a new virtual environment and automatically install the dependencies.  
    - For the following prompts. select `venv`, then the latest available version of Python on your machine, and then `requirements.txt`.

## Run/Debug locally
- Open the Terminal in VS Code (**View** > **Terminal**) and run `flask run`; OR
- Run it with the debugger by opening the Run and Debug view (`Ctrl+Shift+D` or `Cmd+Shift+D`) and selecting **Show all automatic debug configurations**. 
    - Select **Python** and then select **Python: Flask**  

## Containarize your app 
- Install and run [Docker](https://www.docker.com/)
- Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- Run the **Dev Containers: Add Dev Container Configuration Files...** command 
    - Select "Python 3"
    - Select "3.11" version
    - Select any other features you'd like to install, or skip by selecting "OK"
- Open the `devcontainer.json` file and uncomment the line with the `postCreateCommand` field, so the requirements can be installed after the container is created
- Click on the "Reopen in Container" button from the notification displayed by VS Code once the container configuration files were created, or run the **Dev Containers: Open Folder in Container...**. 
- Wait for container to be created and set up
- You're ready to develop your app in the dev container!
