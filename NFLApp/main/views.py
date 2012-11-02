from django.shortcuts import render, redirect

from main.models import Game

def index(request):
    game_list = Game.objects.all()
    context = {
        'game_list': game_list
    }
    return render(request, 'main/index.html', context)

def results(request):
	game_list = Game.objects.all()
	records = {}
	# Update the records of the teams given the game data
	for game in game_list:
		if game.TeamName not in records:
			records[game.TeamName] = { 'Wins': 0, 'Losses': 0 }
		if (game.won()):
			records[game.TeamName]['Wins'] += 1
		else:
			records[game.TeamName]['Losses'] += 1
			
	
	context = {
		'records': records
	}
	return render(request, 'main/results.html', context)