from objects import Profile, Card, Deck, CompProfile, card_display, print_card
print('------------------------------------------')
print('| *Welcome to object oriented BlackJack* |')
print('------------------------------------------')
while True:  # First while loop to ask player for Name 
    player_name = input('Please input your name:')
    if isinstance(player_name, str) and len(str(player_name)) >= 6:
        player = Profile(player_name, 1000)
        print(f'the name, {player_name} has being created\nYou have been given a balance of 1000 to play the game\n')
        print(player)
        break
    else:
        print(f'Your input {player_name} is less than 6 characters\nTry again!!.. ') 
conti = True

while True and conti == True: # Second while loop to begin game play
    card_deck = Deck()
    card_deck.card_shuffle()
    comp_dealer = CompProfile()

    while True: # Third while loop to authenticate bet
        try:
            stake = int(input(f'Please input what you want to stake from {player.money}!!\nThe max bet is 1000 and min is 100:  '))
            if 100 <= stake <= 1000:
                player.stake(stake)
                print(f'\nYour bet of {stake} has accepted\nYour new balance is {player.money}')
        except:
            print('\nError!! only ingeters are accepted \nTry again')
        else:
            break
    
    for n in range(2): # For loop to share the cards 
        removed_card = card_deck.card_remove()
        player.card(removed_card)
        removed_card = card_deck.card_remove()
        comp_dealer.card(removed_card)
    comp_hidden = comp_dealer.playercards[0]
    comp_dealer.playercards[0] = Card('hidden', 'hidden')

    print_card(comp_dealer, player)
    # This block checks if the player has a BLACKJACK 
    if player.check_bust() == 'BJ':
        bet_won = player.deposite(stake, 3/2)
        print(f'BLACKJACK!! {player.name}, you won the bet and gained {bet_won}!!!\nYour new balance is {player.money}')
        play_again = input('\nDo you want to play again?? Y/N: ').lower()
        if play_again == 'y':
            player.reset()
            comp_dealer.reset()
            cont = True
            continue
        elif play_again == 'n':
            conti = False
            break
    # Runs block to continue if no BLACKJACK detected
    elif player.check_bust() == 'NB':
        cont = False

    while True and cont == False: # Fouth while loop to begin hit and stand
        asker = input('Do you want to hit or stand? enter H/S: ').lower()
        if asker == 'h':
            removed_card = card_deck.card_remove()
            player.card(removed_card)
            print_card(comp_dealer, player)

            # This block checks if the player has a BLACKJACK during hit and stand 'BJ'
            if player.check_bust() == 'BJ':
                bet_won = player.deposite(stake, 3/2)
                print(f'BLACKJACK!! {player.name}, you won the bet and gained {bet_won}!!!\nYour new balance is {player.money}')
                play_again = input('\nDo you want to play again?? Y/N: ').lower()
                if play_again == 'y':
                    player.reset()
                    comp_dealer.reset()
                    cont = True
                    break
                elif play_again == 'n':
                    conti = False
                    break

            # this block checks of PLayer has BURSTED 'B'
            elif player.check_bust() == 'B':
                print(f'BURST {player.name}, you lost the bet and {stake}!!!\nYour balance is {player.money}')
                play_again = input('\nDo you want to play again?? Y/N: ').lower()
                if play_again == 'y':
                    player.reset()
                    comp_dealer.reset()
                    cont = True
                    break
                elif play_again == 'n':
                    conti = False
                    break

        elif asker == 's':
            comp_dealer.playercards[0] = comp_hidden
            print_card(comp_dealer, player, True)

            # Checks if Computer Dealer already has a BLACKJACK 'BJ' 
            if comp_dealer.check_bust() == 'BJ':
                bet_won = player.deposite(stake, 1)
                print(f'BLACKJACK!! {player.name}, you won the bet and gained {bet_won}!!!\nYour new balance is {player.money}')
                play_again = input('\nDo you want to play again?? Y/N: ').lower()
                if play_again == 'y':
                    player.reset()
                    comp_dealer.reset()
                    cont = True
                    break
                elif play_again == 'n':
                    conti = False
                    break

            # Checks if Computer Dealer is BURSTED 'B'
            elif comp_dealer.check_bust() == 'B':
                print(f'BURST {player.name}, you lost the bet and {stake}!!!\nYour balance is {player.money}')
                play_again = input('\nDo you want to play again?? Y/N: ').lower()
                if play_again == 'y':
                    player.reset()
                    comp_dealer.reset()
                    cont = True
                    break
                elif play_again == 'n':
                    conti = False
                    break

            while True:

                #Runs when the Computer dealer card is no up to 17 in a TOTAL
                if comp_dealer.numtot < 17:
                    removed_card = card_deck.card_remove()
                    comp_dealer.card(removed_card)
                    print_card(comp_dealer, player, True)

                    # Checks if Computer Dealer already has a BLACKJACK 'BJ'
                    if comp_dealer.check_bust() == 'BJ':
                        print(f'DEALER BLACKJACK!! {player.name}, you lost {stake}!!!\nYour balance is {player.money}')
                        play_again = input('\nDo you want to play again?? Y/N: ').lower()
                        if play_again == 'y':
                            player.reset()
                            comp_dealer.reset()
                            cont = True
                            break
                        elif play_again == 'n':
                            cont = True
                            conti = False
                            break

                    # Checks if Computer Dealer is BURSTED 'B'
                    elif comp_dealer.check_bust() == 'B':
                        bet_won = player.deposite(stake, 1)
                        print(f'DEALER BURST!!! {player.name}, you won the bet and {bet_won}!!!\nYour balance is {player.money}')
                        play_again = input('\nDo you want to play again?? Y/N: ').lower()
                        if play_again == 'y':
                            player.reset()
                            comp_dealer.reset()
                            cont = True
                            break
                        elif play_again == 'n':
                            cont = True
                            conti = False
                            break
                
                #Runs when the Computer dealer card is more 17 in a TOTAL
                elif comp_dealer.numtot >= 17:

                    # Compares value of Computer Dealer and player to know the wins
                    if comp_dealer.numtot > player.numtot:
                        print_card(comp_dealer, player, True)
                        print(f'FAILED {player.name}, you lost {stake}!!!\nYour balance is {player.money}')
                        play_again = input('\nDo you want to play again?? Y/N: ').lower()
                        if play_again == 'y':
                            player.reset()
                            comp_dealer.reset()
                            cont = True
                            break
                        elif play_again == 'n':
                            cont = True
                            conti = False
                            break

                    # if the Computer Total and the player Total are equal then player gets his initial bet back
                    elif comp_dealer.numtot == player.numtot:
                        print_card(comp_dealer, player, True)
                        player.deposite(stake, 0)
                        print(f'No winner, You get your stake back; {stake} ')
                        play_again = input('\nDo you want to play again?? Y/N: ').lower()
                        if play_again == 'y':
                            player.reset()
                            comp_dealer.reset()
                            cont = True
                            break
                        elif play_again == 'n':
                            cont = True
                            conti = False
                            break

                    # if the computer total is lesser than the player total then the player wins the land
                    elif comp_dealer.numtot < player.numtot:
                        bet_won = player.deposite(stake, 1)
                        print_card(comp_dealer, player, True)
                        print(f'WON {player.name}, you won is {bet_won}!!!\nYour balance is {player.money}')
                        play_again = input('\nDo you want to play again?? Y/N: ').lower()
                        if play_again == 'y':
                            player.reset()
                            comp_dealer.reset()
                            cont = True
                            break
                        elif play_again == 'n':
                            cont = True
                            conti = False
                            break
