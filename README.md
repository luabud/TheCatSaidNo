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

### Create an Azure account
- If you don't have one, create an Azure account at https://azure.microsoft.com/free/. You'll start with USD 200 of credits when signing up for the first time. 
    - Make sure you have contributor role to the Azure subscription when you create it.
### Install `azd`
- Install the [Azure Developer CLI extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.azure-dev)
- Open the Command Palette `Ctrl+Shift+P` / `Cmd+Shift+P`) and run the **Azure Developer: Install or Update Azure Developer CLI** command.
- Verify `azd` is succesfully installed by running `azd` in the terminal. 
    - If the command fails, first check if `azd` is installed but not on PATH. 
    - Otherwise try installing it manually by following the instructions at https://aka.ms/azd-install. 
- Login Azure by running the **Azure Developer: Sign in with the Azure Developer CLI** command in the Command Palette. 
- Initialize your application by running the **Azure Developer: init** command, or running `azd init` in the terminal.
    - Select **Empty Template**
    - Provide an environment name (e.g. "thecatsaidno")
    - Pick a region
    - Provide an Azure subscription
- When `azd init` is complete, you will see a folder named **infra** has been created at the root of your project folder.
- Under the **infra** folder, create the following files:
    - `abbreviations.json`:
        <details> <summary> File content </summary> 

        ```
        {
            "analysisServicesServers": "as",
            "apiManagementService": "apim-",
            "appConfigurationConfigurationStores": "appcs-",
            "appManagedEnvironments": "cae-",
            "appContainerApps": "ca-",
            "authorizationPolicyDefinitions": "policy-",
            "automationAutomationAccounts": "aa-",
            "blueprintBlueprints": "bp-",
            "blueprintBlueprintsArtifacts": "bpa-",
            "cacheRedis": "redis-",
            "cdnProfiles": "cdnp-",
            "cdnProfilesEndpoints": "cdne-",
            "cognitiveServicesAccounts": "cog-",
            "cognitiveServicesFormRecognizer": "cog-fr-",
            "cognitiveServicesTextAnalytics": "cog-ta-",
            "computeAvailabilitySets": "avail-",
            "computeCloudServices": "cld-",
            "computeDiskEncryptionSets": "des",
            "computeDisks": "disk",
            "computeDisksOs": "osdisk",
            "computeGalleries": "gal",
            "computeSnapshots": "snap-",
            "computeVirtualMachines": "vm",
            "computeVirtualMachineScaleSets": "vmss-",
            "containerInstanceContainerGroups": "ci",
            "containerRegistryRegistries": "cr",
            "containerServiceManagedClusters": "aks-",
            "databricksWorkspaces": "dbw-",
            "dataFactoryFactories": "adf-",
            "dataLakeAnalyticsAccounts": "dla",
            "dataLakeStoreAccounts": "dls",
            "dataMigrationServices": "dms-",
            "dBforMySQLServers": "mysql-",
            "dBforPostgreSQLServers": "psql-",
            "devicesIotHubs": "iot-",
            "devicesProvisioningServices": "provs-",
            "devicesProvisioningServicesCertificates": "pcert-",
            "documentDBDatabaseAccounts": "cosmos-",
            "eventGridDomains": "evgd-",
            "eventGridDomainsTopics": "evgt-",
            "eventGridEventSubscriptions": "evgs-",
            "eventHubNamespaces": "evhns-",
            "eventHubNamespacesEventHubs": "evh-",
            "hdInsightClustersHadoop": "hadoop-",
            "hdInsightClustersHbase": "hbase-",
            "hdInsightClustersKafka": "kafka-",
            "hdInsightClustersMl": "mls-",
            "hdInsightClustersSpark": "spark-",
            "hdInsightClustersStorm": "storm-",
            "hybridComputeMachines": "arcs-",
            "insightsActionGroups": "ag-",
            "insightsComponents": "appi-",
            "keyVaultVaults": "kv-",
            "kubernetesConnectedClusters": "arck",
            "kustoClusters": "dec",
            "kustoClustersDatabases": "dedb",
            "logicIntegrationAccounts": "ia-",
            "logicWorkflows": "logic-",
            "machineLearningServicesWorkspaces": "mlw-",
            "managedIdentityUserAssignedIdentities": "id-",
            "managementManagementGroups": "mg-",
            "migrateAssessmentProjects": "migr-",
            "networkApplicationGateways": "agw-",
            "networkApplicationSecurityGroups": "asg-",
            "networkAzureFirewalls": "afw-",
            "networkBastionHosts": "bas-",
            "networkConnections": "con-",
            "networkDnsZones": "dnsz-",
            "networkExpressRouteCircuits": "erc-",
            "networkFirewallPolicies": "afwp-",
            "networkFirewallPoliciesWebApplication": "waf",
            "networkFirewallPoliciesRuleGroups": "wafrg",
            "networkFrontDoors": "fd-",
            "networkFrontdoorWebApplicationFirewallPolicies": "fdfp-",
            "networkLoadBalancersExternal": "lbe-",
            "networkLoadBalancersInternal": "lbi-",
            "networkLoadBalancersInboundNatRules": "rule-",
            "networkLocalNetworkGateways": "lgw-",
            "networkNatGateways": "ng-",
            "networkNetworkInterfaces": "nic-",
            "networkNetworkSecurityGroups": "nsg-",
            "networkNetworkSecurityGroupsSecurityRules": "nsgsr-",
            "networkNetworkWatchers": "nw-",
            "networkPrivateDnsZones": "pdnsz-",
            "networkPrivateLinkServices": "pl-",
            "networkPublicIPAddresses": "pip-",
            "networkPublicIPPrefixes": "ippre-",
            "networkRouteFilters": "rf-",
            "networkRouteTables": "rt-",
            "networkRouteTablesRoutes": "udr-",
            "networkTrafficManagerProfiles": "traf-",
            "networkVirtualNetworkGateways": "vgw-",
            "networkVirtualNetworks": "vnet-",
            "networkVirtualNetworksSubnets": "snet-",
            "networkVirtualNetworksVirtualNetworkPeerings": "peer-",
            "networkVirtualWans": "vwan-",
            "networkVpnGateways": "vpng-",
            "networkVpnGatewaysVpnConnections": "vcn-",
            "networkVpnGatewaysVpnSites": "vst-",
            "notificationHubsNamespaces": "ntfns-",
            "notificationHubsNamespacesNotificationHubs": "ntf-",
            "operationalInsightsWorkspaces": "log-",
            "portalDashboards": "dash-",
            "powerBIDedicatedCapacities": "pbi-",
            "purviewAccounts": "pview-",
            "recoveryServicesVaults": "rsv-",
            "resourcesResourceGroups": "rg-",
            "searchSearchServices": "srch-",
            "serviceBusNamespaces": "sb-",
            "serviceBusNamespacesQueues": "sbq-",
            "serviceBusNamespacesTopics": "sbt-",
            "serviceEndPointPolicies": "se-",
            "serviceFabricClusters": "sf-",
            "signalRServiceSignalR": "sigr",
            "sqlManagedInstances": "sqlmi-",
            "sqlServers": "sql-",
            "sqlServersDataWarehouse": "sqldw-",
            "sqlServersDatabases": "sqldb-",
            "sqlServersDatabasesStretch": "sqlstrdb-",
            "storageStorageAccounts": "st",
            "storageStorageAccountsVm": "stvm",
            "storSimpleManagers": "ssimp",
            "streamAnalyticsCluster": "asa-",
            "synapseWorkspaces": "syn",
            "synapseWorkspacesAnalyticsWorkspaces": "synw",
            "synapseWorkspacesSqlPoolsDedicated": "syndp",
            "synapseWorkspacesSqlPoolsSpark": "synsp",
            "timeSeriesInsightsEnvironments": "tsi-",
            "webServerFarms": "plan-",
            "webSitesAppService": "app-",
            "webSitesAppServiceEnvironment": "ase-",
            "webSitesFunctions": "func-",
            "webStaticSites": "stapp-"
        }
        ```
        </details>
    - `main.bicep`:
        <details> <summary> File content </summary> 

        ```
        targetScope = 'subscription'

        @minLength(1)
        @maxLength(64)
        @description('Name of the the environment which is used to generate a short unique hash used in all resources.')
        param environmentName string

        @minLength(1)
        @description('Primary location for all resources')
        param location string

        // Optional parameters to override the default azd resource naming conventions. Update the main.parameters.json file to provide values. e.g.,:
        // "resourceGroupName": {
        //      "value": "myGroupName"
        // }
        param appServicePlanName string = ''
        param resourceGroupName string = ''
        param webServiceName string = ''
        // serviceName is used as value for the tag (azd-service-name) azd uses to identify
        param serviceName string = 'web'

        @description('Id of the user or app to assign application roles')
        param principalId string = ''

        var abbrs = loadJsonContent('./abbreviations.json')
        var resourceToken = toLower(uniqueString(subscription().id, environmentName, location))
        var tags = { 'azd-env-name': environmentName }

        // Organize resources in a resource group
        resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
        name: !empty(resourceGroupName) ? resourceGroupName : '${abbrs.resourcesResourceGroups}${environmentName}'
        location: location
        tags: tags
        }

        // The application frontend
        module web './core/host/appservice.bicep' = {
        name: serviceName
        scope: rg
        params: {
            name: !empty(webServiceName) ? webServiceName : '${abbrs.webSitesAppService}web-${resourceToken}'
            location: location
            tags: union(tags, { 'azd-service-name': serviceName })
            appServicePlanId: appServicePlan.outputs.id
            runtimeName: 'python'
            runtimeVersion: '3.8'
            scmDoBuildDuringDeployment: true
        }
        }

        // Create an App Service Plan to group applications under the same payment plan and SKU
        module appServicePlan './core/host/appserviceplan.bicep' = {
        name: 'appserviceplan'
        scope: rg
        params: {
            name: !empty(appServicePlanName) ? appServicePlanName : '${abbrs.webServerFarms}${resourceToken}'
            location: location
            tags: tags
            sku: {
            name: 'B1'
            }
        }
        }

        // App outputs
        output AZURE_LOCATION string = location
        output AZURE_TENANT_ID string = tenant().tenantId
        output REACT_APP_WEB_BASE_URL string = web.outputs.uri
        ```
        </details>
    - `main.parameters.json`:
        <details> <summary> File content </summary> 

        ```
        {
            "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
            "contentVersion": "1.0.0.0",
            "parameters": {
                "environmentName": {
                    "value": "${AZURE_ENV_NAME}"
                },
                "location": {
                    "value": "${AZURE_LOCATION}"
                },
                "principalId": {
                    "value": "${AZURE_PRINCIPAL_ID}"
                },
                "useAPIM": {
                    "value": "${USE_APIM=false}"
                }
            }
        }
        ```
        </details>
- Open the `azure.yaml` file that was automatically created on `azd init`. 
    - Provide **TheCatSaidNo** to the `name` field
    - Provide **web** to `serviceName`. The important thing is to match what is under the `serviceName` field in the `main.bicep` file.
    - Provide **.** under the `project` field to indicate the project root is the path to the application.
    - The resulting file should look like this:
        ```
        name: TheCatSaidNo
        services:
        web:
            project: .
            language: py
            host: appservice
        ```
        
 - Deploy the app by running the **Azure Developer: Deploy** command, or by running `azd deploy` in the terminal. 

> NOTE:
>
> - These commands will create Azure resources that will incur costs to your Azure subscription. You can clean up those resources manually via the Azure portal or with the `azd down` command.
