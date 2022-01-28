from django.shortcuts import render
from django.template import loader
from .models import Eintrag

# Create your views here.
def index2 (request):
    letzer_Eintrag = Eintrag.objects.order_by('datum')
    loader.get_template('Website/index2.html')
    context = {
        'latest_question_list': letzer_Eintrag,
    }
    return render (request,'Website/index2.html',);

def allgemeines (request):
    return render (request,'Website/Allgemeines/Allgemeines.html')

def dcmtk (request):
    return render (request, 'Website/DCMTK/DCMTK.html')

def home (request):
    return render (request, 'Website/Home.html')

def dcmtkErweiterungsmodule (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule/DCMTK-Erweiterungsmodule.html')

def dicomscope (request):
    return render(request, 'Website/DICOMscope.html')

def kontakt (request):
    return render(request, 'Website/Kontakt/Kontakt.html')

def ansprechpartner (request):
    return render(request, 'Website/Kontakt/Ansprechpartner.html')

def dienstleistungen (request):
    return render(request, 'Website/Dienstleistungen/Dienstleistungen.html')

def datenschutz (request):
    return render(request, 'Website/Datenschutz.html')

def impressum (request):
    return render(request, 'Website/Impressum.html')

def offis (request):
    return render(request, 'https://www.offis.de')

def standardisierung (request):
    return render(request, 'Website/Allgemeines/Standardisierung.html')

def dicomEinführung (request):
    return render(request, 'Website/Allgemeines/DICOM-Einführung.html')

def dcmtkEinführung (request):
    return render (request, 'Website/DCMTK/DCMTK-Einführung.html')

def dcmtkTools (request):
    return render (request, 'Website/DCMTK/DCMTK-Tools.html')

def softwareentwicklungMitDcmtk (request):
    return render (request, 'Website/DCMTK/Softwareentwicklung_mit_DCMTK.html')

def spenden (request):
    return render (request, 'Website/DCMTK/Spenden.html')

def support (request):
    return render (request, 'Website/DCMTK/Support.html')

def dcmjp2k (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule/DCMJP2K.html')

def dcmppscu (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule/DCMPPSCU.html')

def dcmprint (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule/DCMPRINT.html')

def ppsmgr (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule/PPSMGR.html')

def testversionen (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule/Testversionen.html')

def dcmpps (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule/DCMPPS.html')

def dcmstcom (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule/DCMSTCOM.html')

def dicomBeratung (request):
    return render(request, 'Website/Dienstleistungen/DICOM-Beratung.html')

def dicomSchulung (request):
    return render(request, 'Website/Dienstleistungen/DICOM-Schulung.html')

def hl7Schulung (request):
    return render(request, 'Website/Dienstleistungen/HL7-Schulung.html')

def iheSchulung (request):
    return render(request, 'Website/Dienstleistungen/IHE-Schulung.html')