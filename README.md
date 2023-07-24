# Django Bitcoin Wallet

![Bitcoin Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/200px-Bitcoin.svg.png)

## Introduction

Django Bitcoin Wallet is a simple web application that allows users to send and receive Bitcoin. It provides a user-friendly interface for managing Bitcoin addresses, checking account balance, and viewing transaction history.

The wallet interacts with the Bitcoin network using a Bitcoin node (or a third-party API) to send and receive transactions securely.

## Features

- User authentication and account management.
- Generation of unique Bitcoin addresses for each user.
- Send Bitcoin to other addresses.
- View transaction history and account balance.
- Real-time notifications for incoming transactions.
- Secure and user-friendly interface.

## Installation

### Prerequisites

- Python 3.x
- Django (>=2.2)
- Bitcoin node or access to a Bitcoin API service

### Setup

1. create an anaconda environment
```
conda create -n btc_wallet_dj python=3.x
conda activate btc_wallet_dj
```

2. Create a virtual environment (optional but recommended):
``` 
python -m venv env
source env/bin/activate # On Windows use env\Scripts\activate
```
2. Install Django:
pip install django>=2.2

1. Clone the repository:


2. Create a virtual environment (optional but recommended):


2. Create a virtual environment (optional but recommended):


4. Configure the Bitcoin node or API:
   - Open `settings.py` and set the appropriate configurations for your Bitcoin node or API service.

5. Run migrations:


6. Start the development server:


7. Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Usage

1. Register a new account or log in with your existing credentials.
2. Upon successful login, you'll be presented with your Bitcoin address and account balance.
3. To receive Bitcoin, share your Bitcoin address with others.
4. To send Bitcoin, enter the recipient's address and the amount you want to send.
5. Confirm the transaction details and authorize the transfer.
6. Check your transaction history for a list of past transactions.
7. Receive real-time notifications when someone sends Bitcoin to your address.

## Security Considerations

- **Protect your private keys:** Ensure that your private keys are kept secure and never shared with anyone. This application does not store private keys on the server.

- **Use HTTPS:** If deploying to a production environment, use HTTPS to secure communication between the client and server.

- **Regular Updates:** Keep all dependencies up to date to mitigate potential security vulnerabilities.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Disclaimer: This application is for educational and demonstrative purposes only. Use it at your own risk. We are not responsible for any loss of funds or damages caused by the use of this application.
