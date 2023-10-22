# Weather Information Retriever

## Overview

The Weather Information Retriever is a Python project that retrieves and displays weather information for a specified city using the OpenWeatherMap API. This application provides users with the city's temperature in Celsius and the weather description. It also stores the retrieved data in a text file for future reference.

## Features

- **API Integration**: The project integrates with the OpenWeatherMap API to fetch weather data for a specified city.

- **User Interaction**: Users can input a city name to receive immediate weather information in the terminal.

- **Data Storage**: The retrieved weather information is appended to a text file named "weather_info.txt" for future reference.

- **Temperature Conversion**: Temperature is presented in Celsius for user convenience.

- **Error Handling**: The project gracefully handles API request errors and informs users when weather data is not available.

## How to Use

1. **Clone the Repository**: Clone this repository to your local machine using the `git clone` command.

2. **Install Dependencies**: Ensure you have the required packages installed. If not, you can install them using `pip`:

   ```bash
   pip install requests

## Get an API Key

To use this application, you'll need to obtain an API key from OpenWeatherMap. Follow these steps:

1. Visit [OpenWeatherMap](https://openweathermap.org/) to sign up for an account.

2. After signing up and logging in, go to your account settings to generate a new API key.

3. Replace `"YOUR_API_KEY"` with your actual API key in the `api_key` variable within the `weather_app.py` file.

## Run the Program

To run the program, follow these steps:

1. Open your terminal.

2. Navigate to the project directory where the `weather_app.py` file is located.

3. Run the program using the following command:

   ```bash
   python weather_app.py

## Usage

- **Enter City Name**: You will be prompted to enter the name of a city. To exit the program, type 'exit'.

- **View Weather Information**: The program will display the weather information for the specified city, including temperature and weather description. The data is also appended to the "weather_info.txt" file for future reference.

## Python Aspects Demonstrated

This project demonstrates various aspects of Python:

- **API Integration**: The project showcases how to interact with web APIs using Python's `requests` library. It makes HTTP requests to the OpenWeatherMap API and processes the JSON response.

- **User Input and Control Structures**: It effectively utilizes user input to allow users to specify the city and employs control structures to handle user interactions.

- **Data Display and Storage**: The retrieved weather data is presented in the terminal for immediate use and simultaneously saved to a text file for future reference.

- **Error Handling**: The program handles API request errors gracefully, ensuring a smooth user experience.

## License

This project is open-source and available under the MIT License.

Enjoy exploring the world's weather with this simple Python application!

