# Sports Calendar

The Sports Calendar project is a web application that displays the schedules and current matches of various sports including Formula 1, Football (UEFA Champions League and Premier League), and Cricket. The application fetches data from different sports APIs and presents it in a user-friendly format using Streamlit.

## Features

- **Formula 1**: Displays the schedule of Formula 1 meetings for the current year.
- **Football**: Shows the scheduled matches for UEFA Champions League and Premier League, including the total number of matches, first and last scheduled match dates, and details of the next match.
- **Cricket**: Lists the current cricket matches with details such as match type, status, teams, venue, date, and scores.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SportsCalendar.git
    ```
2. Navigate to the project directory:
    ```bash
    cd SportsCalendar
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    python -m streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501` to view the Sports Calendar.

## API Keys

The application requires API keys for accessing sports data. Replace the placeholder API keys in the `app.py` file with your own API keys.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.