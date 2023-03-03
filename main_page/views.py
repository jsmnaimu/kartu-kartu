from django.http import response
from django.shortcuts import render, get_object_or_404
from .models import Card, Deck, Tag
import random, json

def main(request):
    cards = Card.objects.all().prefetch_related('tags')
    response = {'cards':cards}
    return render(request, 'main_page.html', response)

def search(request):
    q = request.GET['q']
    response = Card.objects.filter(title__icontains=q)
    return render(request, 'main_page.html', {'cards':response})

def detail_page(request, id):
    card = Card.objects.prefetch_related('deck').get(pk=id) # fetch the card with specified id

    decks = [] 
    for deck in card.deck.all(): # add all decks of the card to a list
        decks.append(deck.message)

    random.shuffle(decks) # shuffle the list
        
    decks = json.dumps(decks) # convert to json

    return render(request, 'detail.html', {'card':card, 'decks':decks})
