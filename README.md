# Personal Image Repository

Perosnal Image Repository is a great way to upload and store your personal images. When uploading, you give your images a title and category to easily search with in the future. Changed your mind? Deleting an image is as easy as clicking it hitting the 'Delete Selected Images' button.

## Installation

Personal Image Repository is built using the Django Web Framework, which runs on Python. Python3 and Pip are required to run this application.

To get started, please create a virtual environemnt. I recommend using virutalenv. Detailed instructions can be found [here](https://docs.python.org/3/library/venv.html).

Then please use the command below to automatically install the required libraries. This will install Django as well.

```bash
$ pip install -r requirements.txt
```

Run the following commands in the specified order to set up the database models:

```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Finally, run the following command to start up the test server:

```bash
$ python3 manage.py runserver
```

You should then be able to go the address provided in your terminal. I have created a test account already for you to use:

Username: "shopifyrocks", Password: "hireme123"

**Note: If you cannot log in with the provided user details, you may have to set up an account yourself. Please follow the instructions below only if you cannot log in with the provided details.**

Run the following command:

```bash
$ python3 manage.py createsuperuser
```

Then follow the instructions on the screen to create a new superuser account. When finished, run the following command again:

```bash
$ python3 manage.py runserver
```

Then append '/admin' to the address provided by Django. It will prompt you to sign in, do so with the superuser account you recently created. You will then be able to create additional users by clicking on the User object link on the left side of the page. For detailed instructions, please refer to [Django documentation](https://docs.djangoproject.com/en/1.8/intro/tutorial02/).

## Usage

### Main Page

The main page has a file upload section, a search section, and buttons to view all files and delete files. All currently uploaded images are available here, ordered by most recently uploaded to earliest uploaded.

### Uploading

Once you have successfully logged in, the application will take you to the main page. From here, you can upload images. Each image to be uploaded requires a name and category for search puproses. Only one file can be uploaded at a time but you can upload as many images as you like, given you have space.

### Search

You can search using either image name, image category, or both. The search results are automatically ordered with the latest uploads showing up first. After you are finished with your search, simple click 'See All Images' to take you back to the main page.

### Deleting Images

Images can be deleted. Simply click on an image to select it and it will be highlighted with a red border. You can select as many images as you like. Once you are done, simply click the 'Delete Selected Files' button. All selected images will be deleted and you will see the remaining images only.

**WARNING: Deleting files is permanent and cannot be undone.**

## Testing

To run tests, please use the following command once you have succesfully setup.

```bash
$ python3 manage.py test
```

**Note: You may have to update login details for the tests in the file shop_challenge/image_repo/tests.py.**
