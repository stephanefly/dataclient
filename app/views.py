import os
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import FormulaireEvenementForm
from .models import FormulaireEvenement
import csv
import requests
import webbrowser

# Variable pour suivre l'index de la ligne courante du fichier CSV
current_row_index = 0
# Variable pour stocker les lignes du fichier CSV
rows = []

def lire_csv():
    global rows
    # Ouvrir le fichier CSV en mode lecture
    with open(r"C:\Users\FAURE-Stephane\PycharmProjects\Predict\données\nom_insta.csv", newline='',
              encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

# Appelez cette fonction au début pour charger les données CSV
lire_csv()


def formulaire_evenement(request):
    data = FormulaireEvenement.objects.all()
    global current_row_index

    a = False

    while a == False:
        # Obtenir la ligne courante du fichier CSV
        current_row = rows[current_row_index] if current_row_index < len(rows) else None


        client = {
            'nom': current_row[0],
            'datededemande': current_row[1],
            'path': current_row[2],
        }
        # Vérifier si le nom existe déjà dans la base de données
        existing_entry = FormulaireEvenement.objects.filter(nom_insta=client["nom"]).first()

        try:
            if client["nom"] == existing_entry.nom_insta:
                current_row_index += 1
        except:
            a = True


    # Vérifier si l'utilisateur a cliqué sur "Suivant"
    if request.method == 'POST' and 'next' in request.POST:
        current_row_index += 1

    # Gérer le bouton "Soumettre"
    if request.method == 'POST' and not 'next' in request.POST:
        form = FormulaireEvenementForm(request.POST)  # Réinitialisez le formulaire avec les données POST
        if form.is_valid():
            form.save()

    # Initialiser le formulaire avec les données de la ligne courante
    form = FormulaireEvenementForm(initial={
        'nom_insta': current_row[0] if current_row else '',
        'date_demande': client["datededemande"].split(" ")[0]
    })

    return render(request, 'formulaire.html', {'form': form, 'data': data, 'client': client})



def next_row(request):
    global current_row_index
    current_row_index += 1

    new_row = rows[current_row_index] if current_row_index < len(rows) else None

    return JsonResponse({'row': new_row})


def preparation_text(request):
    out = r'données\reformat'
    a = r'données\instagram\messages\inbox'

    lst_repertory_message = os.listdir(a)
    for repertory in lst_repertory_message:
        message_json = os.path.join(a, repertory, 'message_1.json')
        with open(message_json, 'r') as fichier:
            # Charger les données JSON depuis le fichier
            donnees_json = json.load(fichier)

        # Extraire les messages
        messages = donnees_json.get("messages", [])
        # Créer un fichier texte et y écrire le contenu des messages
        chemin_fichier_texte = os.path.join(out, repertory + '.txt')

        with open(chemin_fichier_texte, 'w', encoding='utf-8') as fichier_texte:
            for message in messages:
                sender_name = message.get("sender_name", "")
                timestamp_ms = message.get("timestamp_ms", "")
                content = message.get("content", "")

                # Écrire le contenu dans le fichier texte
                fichier_texte.write(f"{sender_name} ({timestamp_ms}): {content}\n\n")
