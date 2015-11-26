# IVR Phone Tree: IVR for beginners. Powered by Twilio - Python/Flask

An example application implementing an automated phone line using 
Python 2.7 and [Flask](http://flask.pocoo.org/) web framework

## Local development

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```
        mkvirtualenv account-verification-flask
        ```

1. Install the requirements:

    ```
    pip install -r requirements.txt
    ```

1. Start the development server

    ```
    python manage.py runserver
    ```
    
1. Expose the application to the wider Internet using [ngrok](https://ngrok.com/)

    ```
    ngrok http 5000 -host-header="localhost:5000"
    ```
    
1. Provision a number under the [Twilio's Manage Numbers](https://www.twilio.com/user/account/phone-numbers/incoming) 
page on your account. Set the voice URL for the number to http://<your-ngrok-subdomain>.ngrok.io/ivr/welcome

That's it

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests:

    ```
    $ coverage run manage.py test
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
