# REST API using Flask

This project is a simple REST API built using Flask based off of [an article from Akamai.](https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/) The API manages information about programming languages, allowing you to perform CRUD (Create, Read, Update, Delete) operations on a collection of programming languages.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [List Programming Languages](#list-programming-languages)
  - [Create a Programming Language](#create-a-programming-language)
  - [Get, Update, and Delete a Programming Language](#get-update-and-delete-a-programming-language)
- [Contributing](#contributing)
- [License](#license)

## Features

- List programming languages based on publication year range.
- Create a new programming language entry.
- Get details of a specific programming language.
- Update details of a specific programming language.
- Delete a specific programming language.

## Getting Started

### Prerequisites

- Python (version 3.x)
- Flask (install via `pip install Flask`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
### List Programming Languages
To list programming languages based on publication year range, make a GET request to:

   ```bash
   http://localhost:5000/programming_languages?before_year=2022&after_year=2000
   ```

### Create a Programming Language
To create a new programming language entry, make a POST request to:

   ```bash
   http://localhost:5000/programming_languages
   ```

### Get, Update, and Delete a Programming Language
To get details of a specific programming language, make a GET request to:

   ```bash
   http://localhost:5000/programming_languages/<programming_language_name>
   ```

To update details of a specific programming language, make a PUT request to the same URL with updated JSON data in the request body.

To delete a specific programming language, make a DELETE request to:
   ```bash
   http://localhost:5000/programming_languages/<programming_language_name>
   ```
## Contributing
Feel free to contribute to this project. Fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
