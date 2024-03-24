# Blackjack Python Game

Blackjack Advantaged Player Tool is a text-based implementation of the popular casino card game, Blackjack. The game allows players to experience the fun of playing Blackjack right from their command line interface which is shown on a webpage as to be accessed from anywhere with an internet connection!

## Gameplay

In Blackjack, the player competes against the dealer (computer). The objective is to have a hand value closer to 21 than the dealer's hand value without exceeding 21. A hand with a value exceeding 21 is considered "bust" and results in an automatic loss. The game begins with each player, including the dealer, receiving two cards. The player can then choose to "hit" (receive another card) or "stand" (end their turn). The dealer must hit until their hand value reaches 17 or higher. The player wins if their hand value is closer to 21 than the dealer's hand value, or if the dealer busts.

Click [here](https://github.com/DrunkenJellies-dev/BlackjackAdvantagedPlayerTool) to access the repository.

Click [here](https://blackjack-advantaged-tool-52d146ec3663.herokuapp.com/) to play the python blackjack game.

<!-- Mock Up Image -->
![mock-up-image](/assets/documentation/mock_up.png)

## Features
* Game Title: The title of the game, "Blackjack", is prominently displayed to provide context for the player.

* Player's Hand: The cards in the player's hand are displayed, showing their current hand value and cards. This allows the player to see their progress and make informed decisions during the game.

* Dealer's Hand: The dealer's hand is partially revealed, with one card face up and the other face down, simulating the experience of playing against a dealer in a real casino.

* Hit, Stand, Double, or Split options: The player is presented with options to either "hit" (receive another card) or "stand" (end their turn). Players are also able to double their hand (receive only one more card and double their bet), and split their hand (only when they have two cards of the same rank, allowing players to play two hands simultaneously). This interactive element allows the player to control their gameplay strategy in any way they see fit allowing for variety.

* Result Display: After the player's turn ends, the outcome of the round is displayed, indicating whether the player wins, loses, or ties with the dealer.

* Game Status: Information about the current game status, such as the player's balance, total wins, losses, and ties, is displayed to provide context and track progress throughout the game.

* Betting Interface: In the betting interface, the player can place their bet for the current round, allowing them to control their risk and potential reward. Bets carry forward into following rounds, allowing players to further their gameplay.

* Interactive Controls: Various interactive controls, such as buttons or keyboard shortcuts, allow the player to navigate the game, make decisions, and interact with different elements seamlessly.

## Deployment 

* Blackjack Advantaged Player Tool was deployed using Heroku:
* Login and navigate to the homepage
* Select create a new app.
* Go to settings.
* Create config var add PORT to key and Value 8000 
* Add buildpack - Python - nodeJS (in that order).
* Go to deploy and connect to the correct github repository.
* Setup automatic deploy.

## Technologies
* Visual Studio Code - used to develop the website
* Github - used to host source code
* Heroku - used to host webpage with terminal of game
* Sourcetree - used to commit and push code 
* Python - used to create Blackjack game
* Techsini.com- used to create the mock up image
* jshint validator - used to check javascript code for errors
* markdownlivepreview.com - used to write the README.md while seeing a preview
* shareX - to gather screenshots for the README