# Django Bitcoin Wallet

## Introduction

Django Bitcoin Wallet is a simple web application that allows users to send and receive Bitcoin. It provides a user-friendly interface for managing Bitcoin addresses, checking account balance, and viewing transaction history.

The wallet interacts with the Bitcoin network using a Bitcoin node (or a third-party API) to send and receive transactions securely.

## Features

- User authentication and account management.
- Generation of unique Bitcoin addresses for each user.
- Send Bitcoin to other addresses.
- View transaction history and account balance.

## Installation

### Prerequisites

- Python 3.x
- Django (>=2.2)
- Bitcoin node or access to a Bitcoin API service

## Environment setup
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


## Git setup

4. Clone the repository:
```
git clone https://github.com/HMFazleRabbi/bitcoinwallet_dj.git
cd django-bitcoin-wallet
```

5. Install dependencies:

```pip install -r requirements.txt```

## Setting up the database
6. We will be using the posgres sql library, which can be installed as [follows](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04).


## Django setup

7. Run migrations:
```python manage.py runserver```

8. Start the development server:
```python manage.py runserver```
Visit `http://127.0.0.1:8000/` in your web browser to access the application.



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

## Sample Webpages
![a1](https://github.com/HMFazleRabbi/bitcoinwallet_dj/assets/55730363/14f38ce6-1644-496d-9d22-9166e5896159)
![a2](https://github.com/HMFazleRabbi/bitcoinwallet_dj/assets/55730363/e8e899e2-9e85-4bf0-98da-70bbcfc7a9cf)
![a3](https://github.com/HMFazleRabbi/bitcoinwallet_dj/assets/55730363/2a023f9f-3679-42e3-8a56-7456a5f8af57)
![a4](https://github.com/HMFazleRabbi/bitcoinwallet_dj/assets/55730363/03837769-8d34-42cb-8629-8d7eae559ee7)






