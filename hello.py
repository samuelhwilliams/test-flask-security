from flask_security.utils import validate_redirect_url


def main():
    validate_redirect_url('/')
    print("Hello from test-flask-security!")


if __name__ == "__main__":
    main()
