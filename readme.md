# Weather SMS Notification Service

This project integrates Twilio API to send SMS notifications and OpenWeather API to retrieve live current weather data. The script is deployed on PythonAnywhere to execute daily at 7 am EST.

## Technologies Used:
- **Twilio API:** Used for sending SMS notifications.
- **OpenWeather API:** Provides current weather data based on geographical coordinates.
- **PythonAnywhere:** Hosting platform for scheduling script execution.

## How It Works:
- The script queries OpenWeatherMap for weather data based on specified coordinates.
- It constructs an SMS message with relevant weather details.
- Twilio sends the SMS notification to the specified recipient number.
- The script is scheduled to run daily at 7 am EST on PythonAnywhere for automated updates.
