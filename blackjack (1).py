#!/usr/bin/env
#-*- coding: utf-8 -*-
#Authored by Aus10

from random import shuffle

def createDeck(): #create Deck of cards
	Deck = []
	
	faceValues = ["A", "J", "Q", "K"]
	for i in range(4): #four different suits
		for card in range(2,11): #number cards
			Deck.append(str(card))
			
		for card in faceValues: 
			Deck.append(card)
	
	return Deck
	
Deck = createDeck()
shuffle(Deck)

#print(Deck)

class Player: #player class definition or create and define a user to a system
	def __init__(self, hand = [], money = 0):
		self.hand = hand
		self.score = self.setScore()
		self.money = money
		self.bet = 0
		
	def __str__(self): #print(Player)
		currentHand = ""
		for card in self.hand:
			currentHand += str(card) + " "
			
		finalStatus = currentHand + "score: " + str(self.score)
		
		return finalStatus
		
	def setScore(self):
		self.score = 0
		
		print(self.score)
		faceCardsDict = {"A":11, "J":10, "Q":10, "K":10,
						 "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,
						 "9":9,"10":10}#store card values within a dictionary
		aceCounter = 0
		for card in self.hand:
			self.score += faceCardsDict[card]
			if card == "Ace":
				aceCounter += 1
			if self.score > 21 and aceCounter != 0:
				self.score -= 10
				aceCounter -= 1
				
		return self.score
	
	def hit(self, card):
		self.hand.append(card)
		self.score = self.setScore()
		
	def play(self, newHand):
		self.hand = newHand
		self.score = self.setScore()
		
	def betMoney(self, amount):
		self.money -= amount #money = 100
		self.bet += amount #money = 80 bet = 20
	
	def win(self, result):
		if result == True:
			if self.score == 21 and len(self.hand) == 2:
				self.money += 2.5*self.bet
			else:
				self.money =+ 2*self.bet
			
			self.bet = 0
		else:
			self.bet = 0
	
	def draw(self):
		self.money += self.bet
		self.bet = 0
		
	def hasBlackJack(self):
		if self.score == 21 and len(self.hand) == 2:
			return True
		else: 
			return False
			
def printHouse(House):
	for card in range(len(House.hand)):
		if card == 0:
			print("House hand: ", "X", end = " ")
		elif card == len(House.hand) - 1:
			print(House.hand[card])
		else:
			print(House.hand[card], end = " ")
			
cardDeck = createDeck()
shuffle(cardDeck)
firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]
Player1 = Player(firstHand)
House = Player(secondHand)
printHouse(House)

cardDeck = createDeck()
while(True):
	if len(cardDeck) < 20:
		cardDeck = createDeck()
	firstHand = [cardDeck.pop(), cardDeck.pop()]
	secondHand = [cardDeck.pop(), cardDeck.pop()]
	Player1.play(firstHand)
	House.play(secondHand)
	#Prompt to place bets	
	Bet = int(input("Place your bet ($): "))
	Player1.betMoney(Bet)

	print("Your Hand: ",Player1)

	#before prompting user to play check for black jack
	if Player1.hasBlackJack():
		if House.hasBlackJack():
			Player1.draw()
		else:
			Player1.win(True)
	else:
		#prompt user to play
		while(Player1.score < 21):
			action = input("Do you want another card?(y/n): ")
			if action == "y":
				Player1.hit(cardDeck.pop())
				print("Your Hand: ", Player1)
				printHouse(House)
			else:
				break
		while(House.score < 20):
			House.hit(cardDeck.pop())
			print(House)
	
		if Player1.score > 21:
			if House.score > 21:
				Player1.draw()
			else:
				Player1.win(False)
	
		elif Player1.score > House.score:
			Player1.win(True)
		
		elif Player1.score == House.score:
			Player1.draw()
		else:
			if House.score > 21:
				Player1.win(True)
			else:
				Player1.win(False)
			
	print("House Hand: ", House)
	print("Money: ", Player1.money)
	playAgain = input("Do you want to play again or Quit? (y/n): ")
	if playAgain =="n":
		exit()
