# Product Price Comparison Application (coding-project-template)
Created two backend applications to be used as microservices on Code Engine and deployed one front-end application that uses the microservices.

## BUILD CMD formula ibmcloud CLI:

ibmcloud ce application create --name <NAME> --image <IMAGE> --registry-secret icr-secret --port <00PORT00> --build-context-dir <BUILD_CONTEXT> --build-source <GIT REPO/LOCAL DIRECTORY LOCATION>

### 1st cmd for deployment of frontend:

ibmcloud ce application create --name prodlist --image us.icr.io/${SN_ICR_NAMESPACE}/prodlist --registry-secret icr-secret --port 5000 --build-context-dir products_list --build-source https://github.com/ibm-developer-skills-network/dealer_evaluation_backend.git

## prod_details_url:
https://prodlist.1g1kteeyhg45.us-south.codeengine.appdomain.cloud

second cmd for deployment of backend:

ibmcloud ce application create --name dealerdetails --image us.icr.io/${SN_ICR_NAMESPACE}/dealerdetails --registry-secret icr-secret --port 8080 --build-context-dir dealer_details --build-source https://github.com/ibm-developer-skills-network/dealer_evaluation_backend.git

## dealer_details_url:

https://dealerdetails.1g1kteeyhg45.us-south.codeengine.appdomain.cloud

### builddirected to local html CMD

ibmcloud ce application create --name frontend2 --image us.icr.io/${SN_ICR_NAMESPACE}/frontend --registry-secret icr-secret --port 5001 --build-source .

## Visual Overview
![product_all_dealers_prices](https://github.com/hihassan1998/pythonapps/assets/150392365/df2b6ed8-d813-49eb-b110-66ee2e302f95)

