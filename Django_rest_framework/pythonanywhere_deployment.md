# PythonAnywhere Deployment Guide

To deploy this Django REST API to PythonAnywhere and test the live `/api/send-email/` endpoint:

1. **Create an Account:**
   - Go to [PythonAnywhere](https://www.pythonanywhere.com/) and create a free Beginner account.

2. **Upload Your Code:**
   - Go to the **Files** tab.
   - You can upload your project files directly (zip them up and upload, then unzip via the bash console) OR push your code to GitHub and clone it using the bash console:
     ```bash
     git clone https://github.com/your-username/Django_rest_framework.git
     ```

3. **Set Up a Virtual Environment:**
   - Go to the **Consoles** tab and start a new Bash console.
   - Run the following commands:
     ```bash
     mkvirtualenv myenv --python=python3.10
     cd Django_rest_framework
     pip install -r requirements.txt
     ```
   - Make sure you also install the new packages we just added:
     ```bash
     pip install requests twilio stripe django-allauth dj-rest-auth djangorestframework-simplejwt
     ```

4. **Configure the Web App:**
   - Go to the **Web** tab and click **Add a new web app**.
   - Choose **Manual Configuration** (do NOT choose the Django option, manual is better for existing projects).
   - Choose Python 3.10.
   - Under **Virtualenv**, enter the path to your virtual environment (e.g., `/home/yourusername/.virtualenvs/myenv`).
   - Under **Code**, set the Source Code directory to `/home/yourusername/Django_rest_framework`.

5. **Edit the WSGI Configuration File:**
   - Still on the **Web** tab, click the link to edit the WSGI configuration file (it's under the "Code" section).
   - Delete everything in the file and replace it with:
     ```python
     import os
     import sys

     path = '/home/yourusername/Django_rest_framework'
     if path not in sys.path:
         sys.path.append(path)

     os.environ['DJANGO_SETTINGS_MODULE'] = 'Django_rest_framework.settings'

     from django.core.wsgi import get_wsgi_application
     application = get_wsgi_application()
     ```
   - Save the file.

6. **Update ALLOWED_HOSTS:**
   - Open your `Django_rest_framework/settings.py` file.
   - Update the `ALLOWED_HOSTS` to include your PythonAnywhere domain:
     ```python
     ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
     ```
   - Ensure `DEBUG = False` (Optional for testing, but good practice).

7. **Migrate and Collect Static Files:**
   - In your Bash console, run:
     ```bash
     python manage.py migrate
     python manage.py collectstatic
     ```

8. **Reload the App:**
   - Go back to the **Web** tab and click the big green **Reload** button at the top.

9. **Test the Live Endpoint:**
   - Open Postman.
   - Set the method to **POST**.
   - Set the URL to `https://yourusername.pythonanywhere.com/api/send-email/`.
   - Go to the **Body** tab, select **raw** and **JSON**, and add:
     ```json
     {
         "email": "test@example.com"
     }
     ```
   - Hit **Send**. You should get a `200 OK` response with `{"message": "Email sent successfully!"}`.

10. **Screenshot:**
    - Take a screenshot of the Postman response showing the live PythonAnywhere URL and the success message for your submission.
