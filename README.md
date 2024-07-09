# Bulk WhatsApp Message Sender

This project allows you to send bulk WhatsApp messages using a CSV file containing phone and messages. It uses Selenium to automate WhatsApp Web.

## Features

- Send text messages to multiple contacts.
- Optionally attach an image to the messages.
- Uses Chrome user profile to maintain login sessions.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/shivamc489/bulk-whatsapp-message.git
    cd bulk-whatsapp-message
    ```

2. **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Download ChromeDriver:**
    - Ensure that the ChromeDriver version matches your installed Chrome browser version.
    - You can download ChromeDriver from [here](https://developer.chrome.com/docs/chromedriver/downloads).

## Usage

1. **Prepare your CSV file:**
    - The CSV file should have the following columns:
        - `Phone`: The phone number of the recipient (in international format without `+`).
        - `Message`: The message to be sent.

    ### Sample CSV File
    ```csv
    Phone,Message
    1234567890,Hello John! Checkout our app at https://github.com/Shivamc489/bulk-whatsapp-message
    0987654321,Hi Jane! Checkout our app at https://github.com/Shivamc489/bulk-whatsapp-message
    ```

2. **Run the script:**
    ```sh
    python bulk_whatsapp_message.py -d path/to/your/leads.csv [-i path/to/image.jpg] [-l]
    ```

    - `-d, --data`: Path to the CSV file containing contacts and messages (required).
    - `-i, --image`: Path to the image to send (optional).
    - `-l, --login`: Force login to WhatsApp Web (optional).

3. **Login to WhatsApp Web:**
    - If running for the first time or using the `-l` flag, you will need to scan the QR code from your phone to log in to WhatsApp Web.

## Example

```sh
python bulk_whatsapp_message.py -d leads.csv -i image.jpg
```

This command will send the messages listed in `leads.csv` and attach `image.jpg` to each message.

## Notes

- Ensure that the phone numbers in the CSV file are in the correct international format.
- The script uses a Chrome user profile stored in the `chrome_profile` directory to maintain login sessions. If you encounter login issues, you can delete this directory and re-run the script with the `-l` flag to re-login.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
