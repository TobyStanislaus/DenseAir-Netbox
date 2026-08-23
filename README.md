# DenseAir NetBox

Python application for retrieving and processing **DenseAir network architecture data from NetBox** through its API.

The project was developed during my work at DenseAir and provides a way to compile infrastructure information from NetBox into a format that can be passed to the **Network Management System (NMS)** and used by DenseWare.

## Overview

The system connects the DenseAir infrastructure stored in NetBox with downstream network-management software.

```text
DenseAir Servers
       │
       ▼
    NetBox
       │
       │  API
       ▼
┌─────────────────┐
│  DenseAir       │
│  NetBox Client  │
│                 │
│ Fetch & Process │
│ Infrastructure  │
└────────┬────────┘
         │
         ▼
        NMS
         │
         ▼
     DenseWare
```

NetBox acts as the source of infrastructure information. The Python application retrieves this information through the NetBox API, processes and compiles it, and produces data that can be consumed by the wider DenseAir network-management system.

## Features

* NetBox API integration
* Retrieval of DenseAir network architecture data
* Infrastructure data processing and compilation
* Automated data preparation for downstream systems
* Automated testing
* Test data and expected-result validation

## Technologies

* **Python**
* **NetBox**
* **REST API**
* **Network infrastructure management**
* **Automated testing**

NetBox provides a structured source of truth for network infrastructure and exposes a REST API for programmatic access to resources such as sites, devices and interfaces.

## Project Structure

```text
DenseAir-Netbox/
│
├── main.py             # Main application entry point
├── netbox.py           # NetBox API functionality
├── test_netbox.py      # Automated tests
├── testData.txt        # Test input data
├── testResults.txt     # Expected test results
├── results.txt         # Generated/processed results
├── README.md
└── .gitignore
```

## Testing

The project includes a dedicated test suite in:

```text
test_netbox.py
```

Test data and expected results are maintained separately in:

```text
testData.txt
testResults.txt
```

This allows the NetBox processing functionality to be tested against known inputs and expected outputs.

## Data Pipeline

The application is designed around the following workflow:

1. Connect to the DenseAir NetBox instance.
2. Retrieve network architecture information through the API.
3. Process and compile the returned infrastructure data.
4. Produce structured output for the NMS.
5. Allow the resulting information to be used by DenseWare.

This creates a programmatic link between the infrastructure recorded in NetBox and the systems responsible for monitoring and managing the deployed DenseAir network.

## Context

This project was developed as part of work on the DenseAir network infrastructure.

The resulting data can be used by DenseWare to provide information about the **status and quantities of devices deployed across the DenseAir network**.

## Future Improvements

Potential improvements include:

* More comprehensive API error handling
* Automatic retries for failed API requests
* Configuration through environment variables
* Structured JSON output
* Additional automated test coverage
* Continuous integration
* Automated synchronisation with the NMS
* Improved logging and monitoring


 ## Contact

 toby@stanislaus.co.uk 
 TobyStanislaus on Github

 krishavksingh@gmail.com
 krishavksingh on Github
