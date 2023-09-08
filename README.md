# SUPER METRO BUS MANAGEMENT SYSTEM

[![license](https://img.shields.io/badge/license-%20MIT%20-green.svg)](./LICENSE)
![python version](https://img.shields.io/badge/python-3.10|3.11-blue.svg)
![SQLAlchemy version](https://img.shields.io/badge/SQLAlchemy-2.0.20-cyan.svg)
![alembic version](https://img.shields.io/badge/alembic-1.12.0-orange.svg)
![faker version](https://img.shields.io/badge/faker-19.3.1-mint.svg)
![colorama version](https://img.shields.io/badge/colorama-0.4.4-white.svg)
![click version](https://img.shields.io/badge/click-8.0.3-red.svg)
![platforms](https://img.shields.io/badge/Platforms-Linux%20|%20Windows%20|%20Mac%20-purple.svg)

---

## Introduction

The Super Metro Bus Management System is a Command-Line Interface (CLI) application built using Python. It is designed to manage and track matatus (minibuses) operated by a Super Metro, a Matatu Sacco in Kenya. This tool empowers users to effortlessly handle various aspects of Matatu Sacco management, including member and fleet information, routes, and financial analysis, providing a comprehensive solution for Sacco owners.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Author & License](#author--license)

---

## Features

- **Add and Manage Matatus:** Easily add new matatus to the fleet, find their details, and remove them when necessary.

- **Member Management:** Keep track of members associated with the matatu operation, including their contact information and ownership details.

- **Route Management:** Maintain a database of routes with corresponding pricing information.

- **Search and Retrieval:** Quickly find matatus, members, and routes using name, number plate, or ID-based search queries.

- **Financial Analysis:** Calculate estimated monthly gross amounts for all matatus to assist in financial reporting and analysis.

---

## Installation

### 1. Clone the repository

```txt
git clone https://github.com/ArshavineRoy/super-metro-bms
```

### 2. Navigate to the project's directory

```txt
cd super-metro-bms
```

### 3. Install required dependencies

The root directory of this repository contains the `Pipfile` with all the required dependencies. Install them by running this command from the `root` directory:

```python
pipenv install
```

If `pipenv` is not already installed, you can do so using `pip`:

```python
pip install pipenv
```

### 4. Activate the virtual environment

```python
pipenv shell
```

### 5. Run the CLI application

The CLI app must be run from within the `app` directory

```python
cd app
```

`main.py` is the enttry into the app

```python
./main.py
```

---

## Usage

- **add-matatu:** This command allows the user to add a new matatu to the fleet.

- **add-member:** This command allows the user to add a new member to the database.

- **add-route:** This command allows the user to add a new route to the database.

- **all-matatu-financials:** This command calculates estimated monthly gross amounts for all matatus and exports the results to a .csv file.

- **delete-matatu:** This command allows the user to delete a matatu by its ID.

- **delete-member:** This command allows the user to delete a member by their ID.

- **delete-route:** This command allows the user to delete a route by its ID.

- **find-matatu-by-driver-name:** This command helps the user find a matatu by its driver's name.

- **find-matatu-by-number-plate:** This command allows the user to find a matatu by its number plate.

- **find-member-by-name:** This command helps the user find a member by their name.

- **find-route-by-name:** This command allows the user to find a route by its name.

- **matatus-on-route:** This command finds all matatus plying a specific route and exports the results to a .csv file.

- **matatus-owned-by:** This command lists all matatus owned by a specific member.

- **owner-of-matatu:** This command helps the user find the owner of a matatu by its number plate.

---

## Author & License

Authored by [Arshavine Waema](https://github.com/ArshavineRoy).

Licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
