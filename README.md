# SGCM-back
BackEnd repository using Python and Django REST Framwork for the Final Paper on Computer Engineering by the student Gabriel Sana Ferreira da Silva @UTFPR. 
SGCM stands for Sistema Gerenciador de Clínicas Médicas (Medical clinic management system).

## How to build

 You will need to install
 
    pip install requirements-dev.txt
  
Then you can make the database migrations by using

    python manage.py makemigrations
    python manage.py migrate
 
 
Finnaly, run your server using:

    python manage.py runserver
 
(Default port: 8000)
