dicom.offis.de|dcmtk.org website
=============================
To run locally, do the usual:
#. install Python 3.8 (command for ubuntu/debian)::

    sudo apt install python3
#. install pip3 (command for ubuntu/debian)::

    sudo apt install python3-pip
#. Install django::

    sudo pip3 install django
#. clone source::

    git clone https://github.com/pfagomez/DICOMOFFIS; cd DICOMOFFIS
#. migrate project django::

    python3 manage.py migrate
#. run project::

    python3 manage.py runserver
Open http://localhost:8000/
