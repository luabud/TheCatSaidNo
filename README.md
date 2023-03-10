This is a Useful Website written in Flask for demo purposes.

## Set up

- Clone this repository 
- Open it in [Visual Studio Code](https://code.visualstudio.com/). You can do that by launching VS Code and running **File*** > **Open Folder...**, and selecting the cloned project. 
- Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Make sure you have Python >= 3.8 installed. If not, install it from [python.org](https://www.python.org/downloads/).
- Open the `app.py` file to activate the Python extension.
- Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run the **Python: Create Environment** command to create a new virtual environment and automatically install the dependencies.  
    - For the following prompts. select `venv`, then the latest available version of Python on your machine, and then `requirements.txt`.

## Run/Debug locally
- Open the Terminal in VS Code (**View** > **Terminal**) and run `flask run`; OR
- Run it with the debugger by opening the Run and Debug view (`Ctrl+Shift+D` or `Cmd+Shift+D`) and selecting **Show all automatic debug configurations**. 
    - Select **Python** and then select **Python: Flask**  


## Optional: Deploy to Azure with `azd`
### Install `azd`
- Install the [Azure Developer CLI extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.azure-dev)
- Open the Command Palette `Ctrl+Shift+P` / `Cmd+Shift+P`) and run the **Azure Developer: Install or Update Azure Developer CLI** command.
- Verify `azd` is succesfully installed by running `azd` in the terminal. 
    - If the command fails, first check if `azd` is installed but not on PATH. 
    - Otherwise try installing it manually by following the instructions at https://aka.ms/azd-install. 
- Login Azure by running the **Azure Developer: Sign in with the Azure Developer CLI** command in the Command Palette. 
- Initialize your application by running


> NOTE: This may take a while to complete as it executes three commands: `azd init` (initializes environment), `azd provision` (provisions Azure resources), and `azd deploy` (deploys application code). You will see a progress indicator as it provisions and deploys your application.

When `azd up` is complete it will output the following URLs:

- Azure Portal link to view resources
- ToDo Web application frontend
- ToDo API application

!["azd up output"](assets/urls.png)

Click the web application URL to launch the ToDo app. Create a new collection and add some items. This will create monitoring activity in the application that you will be able to see later when you run `azd monitor`.

> NOTE:
>
> - The `azd up` command will create Azure resources that will incur costs to your Azure subscription. You can clean up those resources manually via the Azure portal or with the `azd down` command.
> - You can call `azd up` as many times as you like to both provision and deploy your solution, but you only need to provide the `--template` parameter the first time you call it to get the code locally. Subsequent `azd up` calls do not require the template parameter. If you do provide the parameter, all your local source code will be overwritten if you agree to overwrite when prompted.
> - You can always create a new environment with `azd env new`.

### Application Architecture

This application utilizes the following Azure resources:

- [**Azure App Services**](https://docs.microsoft.com/azure/app-service/) to host the Web frontend and API backend
- [**Azure Cosmos DB API for MongoDB**](https://docs.microsoft.com/azure/cosmos-db/mongodb/mongodb-introduction) for storage
- [**Azure Monitor**](https://docs.microsoft.com/azure/azure-monitor/) for monitoring and logging
- [**Azure Key Vault**](https://docs.microsoft.com/azure/key-vault/) for securing secrets

Here's a high level architecture diagram that illustrates these components. Notice that these are all contained within a single [resource group](https://docs.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal), that will be created for you when you create the resources.

<img src="assets/resources.png" width="60%" alt="Application architecture diagram"/>

> This template provisions resources to an Azure subscription that you will select upon provisioning them. Please refer to the [Pricing calculator for Microsoft Azure](https://azure.microsoft.com/pricing/calculator/) and, if needed, update the included Azure resource definitions found in `infra/main.bicep` to suit your needs.

### Application Code

The repo is structured to follow the [Azure Developer CLI](https://aka.ms/azure-dev/overview) conventions including:

- **Source Code**: All application source code is located in the `src` folder.
- **Infrastructure as Code**: All application "infrastructure as code" files are located in the `infra` folder.
- **Azure Developer Configuration**: An `azure.yaml` file located in the root that ties the application source code to the Azure services defined in your "infrastructure as code" files.
- **GitHub Actions**: A sample GitHub action file is located in the `.github/workflows` folder.
- **VS Code Configuration**: All VS Code configuration to run and debug the application is located in the `.vscode` folder.

### Azure Subscription

This template will create infrastructure and deploy code to Azure. If you don't have an Azure Subscription, you can sign up for a [free account here](https://azure.microsoft.com/free/). Make sure you have contributor role to the Azure subscription.
