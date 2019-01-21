# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
#Objets de base
from soccersimulator import Vector2D, SoccerState, SoccerAction
#Objets pour un match
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
#Stratégie de base 
from soccersimulator import Strategy
#Constantes
from soccersimulator import settings
#Modules maths
import math

#w = Vector2D(angle=3.14/2, norm=1)    ±(GAME_WIDTH, GAME_GOAL_HEIGHT /2.)

GAME_WIDTH = 150
GAME_HEIGHT = 90
GAME_GOAL_HEIGHT = 10
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65
MAX_GAME_STEPS = 2000
maxPlayerSpeed = 1.
maxPlayerAcceleration = 0.2
maxBallAcceleration = 5


class MaStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        
        acceleration = state.ball.position - state.player_state(id_team, id_player).position
        shoot = Vector2D (BALL_RADIUS ,BALL_RADIUS)
        d = acceleration.norm
        if (d < PLAYER_RADIUS + BALL_RADIUS):
            shoot = ((GAME_WIDTH, GAME_HEIGHT /2.) - Vector2D(3.14/2 ,maxBallAcceleration))*v
            #shoot.angle+=3.14/2
            #shoot.angle = 0
            #shoot = Vector2D.angle

        Action = SoccerAction(acceleration , shoot)
        return Action


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Karis", MaStrategy())  # Random strategy
team2.add("Static", Strategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)