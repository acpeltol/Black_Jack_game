import pygame
import random
import time

pygame.font.init()

WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

GREEN = 50, 205, 50

WHITE = 255, 255, 255

BLUE = 30,144,255

IMAGE_SIZEX, IMAGE_SIZEY = 115, 150

FPS = 60

TXT_FONT = pygame.font.SysFont(None,40)

ASKING_FONT = pygame.font.SysFont(None,20)

HUGE_FONT = pygame.font.SysFont(None,120)

HUGE_FONT2 = pygame.font.SysFont(None,80)

# Game variablse

cards = [{'Ace of Spades': 11},{'Ace of Hearts': 11}, {'King of Spades': 10}, {'Jack of Spades': 10},{'Nine of Hearts': 9}, {'Four of Hearts': 4}, {'Four of Diamonds': 4}, {'Six of Clubs': 6}, {'Nine of Spades': 9}, 
         {'Jack of Hearts': 10}, {'Six of Spades': 6}, {'King of Hearts': 10}, {'Jack of Diamonds': 10}, {'Seven of Diamonds': 7}, 
         {'Queen of Spades': 10}, {'Two of Spades': 2}, {'Three of Hearts': 3}, {'Ten of Diamonds': 10}, {'Five of Clubs': 5}, {'Queen of Diamonds': 10}, {'Nine of Diamonds': 9}, 
         {'Three of Spades': 3}, {'Nine of Clubs': 9}, {'Ace of Clubs': 11}, {'Three of Clubs': 3}, {'Queen of Clubs': 10}, {'Seven of Clubs': 7}, {'Four of Clubs': 4}, {'Five of Diamonds': 5}, 
         {'Eight of Diamonds': 8}, {'Two of Hearts': 2}, {'King of Clubs': 10}, {'Ace of Diamonds': 11}, {'Ten of Hearts': 10}, {'Two of Diamonds': 2}, {'Two of Clubs': 2}, {'Three of Diamonds': 3},
        {'Eight of Spades': 8}, {'Eight of Clubs': 8}, {'Eight of Hearts': 8}, {'Four of Spades': 4}, {'Queen of Hearts': 10}, {'King of Diamonds': 10}, {'Seven of Spades': 7}, {'Seven of Hearts': 7}, 
         {'Five of Spades': 5}, {'Six of Hearts': 6}, {'Six of Diamonds': 6}, {'Five of Hearts': 5}, {'Jack of Clubs': 10}, {'Ten of Spades': 10}, {'Ten of Clubs': 10}]

random.shuffle(cards)

pygame.display.set_caption("Black Jack")

print(cards)

# Exit window

def exit(run):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
       run = False
       break
  time.sleep(1)
  return run

# Asking for bet

def bet_ask(cash,player_score, dealer_score, player_carden, dealer_carden,bet):
  asking = True
  user_text = ""
  draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
  geisho = ASKING_FONT.render("Please place your bet: ", True, WHITE)
  WIN.blit(geisho, (20, 680))
  pygame.display.update()
  while asking:

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
          pygame.quit()
        elif event.key == pygame.K_BACKSPACE:
          user_text = user_text[0:-1]
          draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
          geisho = ASKING_FONT.render("Please place your bet: ", True, WHITE)
          WIN.blit(geisho, (20, 680))
          bagio = ASKING_FONT.render(user_text, True, WHITE)
          WIN.blit(bagio, (160, 680))
          pygame.display.update()
        elif event.key == pygame.K_RETURN:
          asking = False
        else:
          user_text += event.unicode
          draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
          geisho = ASKING_FONT.render("Please place your bet: ", True, WHITE)
          WIN.blit(geisho, (20, 680))
          bagio = ASKING_FONT.render(user_text, True, WHITE)
          WIN.blit(bagio, (160, 680))
          pygame.display.update()
  return user_text

def bet_check(cash,player_score, dealer_score, player_carden, dealer_carden,bet):
  right = True
  while right:
    goida = bet_ask(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
    try:
      goida = int(goida)
      print(cash)
      if goida > cash:
        faitro = HUGE_FONT2.render("You don't have that much cash!",True, BLUE)
        WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
        pygame.display.update()
        time.sleep(2)
        continue
      elif goida <= 0:
        faitro = HUGE_FONT2.render("You can't bet a negative nuber or zero!",True, BLUE)
        WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
        pygame.display.update()
        time.sleep(2)
        continue
      else:
        right = False
    except:
        faitro = HUGE_FONT.render("Pelase add an integer!", True, BLUE)
        WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
        pygame.display.update()
        time.sleep(2)
        continue
  cash -= goida
  return cash, goida

# Player get cards!

def player_cardo(player_carden):
    fiat = cards[0]
    player_carden.append(fiat)
    del cards[0]
    cards.append(fiat)
    return player_carden

# Dealer get cards!

def dealer_cardo(dealer_carden):
    fiat = cards[0]
    dealer_carden.append(fiat)
    del cards[0]
    cards.append(fiat)
    return dealer_carden

# First round check

def first_check(player_carden, dealer_carden, cash, bet):
  player_score = 0
  dealer_score = 0

  for kit in player_carden:
      for fito in kit: 
        if kit[fito] == 11 and player_score > 10:
          player_score += 1
        else:
          player_score += kit[fito]

  for kit in dealer_carden:
      for fito in kit: 
        if kit[fito] == 11 and dealer_score > 10:
          dealer_score += 1
        else:
          dealer_score += kit[fito]
  
  if player_score == 21 and dealer_score < 21:
    faitro = HUGE_FONT.render("Black Jack!",True,BLUE)
    WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
    pygame.display.update()

    time.sleep(2)

    player_score = 0
    dealer_score = 0

    draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
    faitro = HUGE_FONT.render("You Won!", True, BLUE)
    WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
    pygame.display.update()

    time.sleep(2)

    cash += 2 * bet

    gonda = False

  elif dealer_score == 21 and player_score < 21:

    faitro = HUGE_FONT.render("Black Jack!",True, BLUE)
    WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
    pygame.display.update()

    time.sleep(2)

    player_score = 0
    dealer_score = 0

    draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
    faitro = HUGE_FONT.render("You Lost!", True, BLUE)
    WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
    pygame.display.update()

    time.sleep(2)

    gonda = False

  elif dealer_score == player_score and player_score == 21:

    faitro = HUGE_FONT.render("Draw!",True,BLUE)
    WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
    pygame.display.update()

    time.sleep(2)

    cash += bet

    gonda = False
  else: 
    gonda = True
  
  return gonda, cash

# Asking for more cards!

def asking_cards(cash,player_score, dealer_score, player_carden, dealer_carden,bet):
  asking = True
  user_text = ""
  draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
  geisho = ASKING_FONT.render("Do You want to take anothe card(Yes(y) or No(n)): ", True, WHITE)
  WIN.blit(geisho, (20, 680))
  pygame.display.update()
  while asking:

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
          pygame.quit()
        elif event.key == pygame.K_BACKSPACE:
          user_text = user_text[0:-1]
          draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)

          geisho = ASKING_FONT.render("Do You want to take anothe card(Yes(y) or No(n)): ", True, WHITE)
          WIN.blit(geisho, (20, 680))

          bagio = ASKING_FONT.render(user_text, True, WHITE)
          WIN.blit(bagio, (330, 680))
          pygame.display.update()
        elif event.key == pygame.K_RETURN:
          asking = False
        else:
          user_text += event.unicode
          draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)

          geisho = ASKING_FONT.render("Do You want to take anothe card(Yes(y) or No(n)): ", True, WHITE)
          WIN.blit(geisho, (20, 680))

          bagio = ASKING_FONT.render(user_text, True, WHITE)
          WIN.blit(bagio, (330, 680))
          pygame.display.update()
  return user_text

def morep_cards(cash,player_score, dealer_score, player_carden, dealer_carden,bet):
  asko = True
  while asko:
    goida = asking_cards(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
    print(goida)
    if goida.lower() == "y" or goida.lower() == "yes" or goida.lower() == "n" or goida.lower() == "no":
      if goida.lower() == "y" or goida.lower() == "yes":
        player_carden = player_cardo(player_carden)
        scato = 0
        for card in player_carden:
          for score in card:
            if card[score] == 11 and scato > 10:
              scato += 1
            else:
              scato += card[score]
        if scato > 21:
          draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
          time.sleep(1)
          faitro = HUGE_FONT.render("You Lost!", True, BLUE)
          WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
          pygame.display.update()
          time.sleep(2)
          next = False
          asko = False
        elif scato == 21:
          draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
          time.sleep(2)
          asko = False
          next = True
        else:
          continue
      elif goida.lower() == "n" or goida.lower() == "no":
        asko = False
        next = True
    else:
      faitro = HUGE_FONT2.render("Please write yes(y) or no(n)!", True, BLUE)
      WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
      pygame.display.update()
      time.sleep(2)
      continue
  return player_carden, next

# Dealer takes card!

def opposite_cards(cash,player_score, dealer_score, player_carden, dealer_carden, bet):
  taking = True
  while taking:
    player_score = 0
    dealer_score = 0
    for kit in player_carden:
      for fito in kit: 
        if kit[fito] == 11 and player_score > 10:
          player_score += 1
        else:
          player_score += kit[fito]

    for kit in dealer_carden:
      for fito in kit: 
        if kit[fito] == 11 and dealer_score > 10:
          dealer_score += 1
        else:
          dealer_score += kit[fito]
    
    if player_score > dealer_score:
      dealer_carden = dealer_cardo(dealer_carden)
      player_score = 0
      dealer_score = 0
      draw_window(cash,player_score, dealer_score, player_carden, dealer_carden, bet)
      time.sleep(1)


    elif dealer_score > player_score and dealer_score < 22:
      player_score = 0
      dealer_score = 0
      draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
      time.sleep(1)
      faitro = HUGE_FONT.render("You Lost!", True, BLUE)
      WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
      pygame.display.update()
      time.sleep(2)
      taking = False


    elif dealer_score > 21:    
      player_score = 0
      dealer_score = 0
      draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
      time.sleep(1)
      faitro = HUGE_FONT.render("You won!", True, BLUE)
      WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
      pygame.display.update()
      cash += 2 * bet
      time.sleep(2)
      taking = False


    elif dealer_score == player_score:
      player_score = 0
      dealer_score = 0
      draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
      time.sleep(1)
      faitro = HUGE_FONT.render("Draw!", True, BLUE)
      WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
      
      pygame.display.update()
      cash += bet
      time.sleep(2)
      taking = False


  return cash

# Drawing main window!

def draw_window(cash,player_score, dealer_score, player_carden, dealer_carden, bet):
    WIN.fill(GREEN)

    player_cardx, player_cardy = 100, 150

    dealer_cardx, dealer_cardy = 100, 425

    for kit in player_carden:
      for fito in kit: 
        if kit[fito] == 11 and player_score > 10:
          pygame.draw.rect(WIN,WHITE,pygame.Rect(player_cardx, player_cardy,IMAGE_SIZEX, IMAGE_SIZEY))
          image = pygame.image.load("images/"+fito+".png")
          image = pygame.transform.scale(image, (IMAGE_SIZEX, IMAGE_SIZEY))
          player_score += 1
          WIN.blit(image,(player_cardx, player_cardy))
        else:
          kaido = kit[fito]
          pygame.draw.rect(WIN,WHITE,pygame.Rect(player_cardx, player_cardy,IMAGE_SIZEX, IMAGE_SIZEY))
          image = pygame.image.load("images/"+fito+".png")
          image = pygame.transform.scale(image, (IMAGE_SIZEX, IMAGE_SIZEY))
          player_score += kaido
          WIN.blit(image,(player_cardx, player_cardy))
        player_cardx += 155

    for kit in dealer_carden:
      for fito in kit:
        if kit[fito] == 11 and dealer_score > 10:
          pygame.draw.rect(WIN,WHITE,pygame.Rect(dealer_cardx, dealer_cardy,IMAGE_SIZEX, IMAGE_SIZEY))
          image = pygame.image.load("images/"+fito+".png")
          image = pygame.transform.scale(image, (IMAGE_SIZEX, IMAGE_SIZEY))
          dealer_score += 1
          WIN.blit(image,(dealer_cardx, dealer_cardy))
        else:
          kaido = kit[fito]
          pygame.draw.rect(WIN,WHITE,pygame.Rect(dealer_cardx, dealer_cardy,IMAGE_SIZEX, IMAGE_SIZEY))
          image = pygame.image.load("images/"+fito+".png")
          image = pygame.transform.scale(image, (IMAGE_SIZEX, IMAGE_SIZEY))
          dealer_score += kaido
          WIN.blit(image,(dealer_cardx, dealer_cardy))
        dealer_cardx += 155

    caisheo = TXT_FONT.render("Cash: "+str(cash), True, WHITE)
    WIN.blit(caisheo, (20, 20))

    caisheo = TXT_FONT.render("Bet: "+str(bet), True, WHITE)
    WIN.blit(caisheo, (900, 20))

    geisho = TXT_FONT.render("Your score: "+str(player_score), True, WHITE)
    WIN.blit(geisho, (20, 75))

    geisho = TXT_FONT.render("Dealers score: "+str(dealer_score), True, WHITE)
    WIN.blit(geisho, (20, 350))
    
    pygame.display.update()

def main():
  clock = pygame.time.Clock()

  cash = 2500

  run = True
  while run:
    bet = 0

    player_score = 0

    dealer_score = 0

    player_carden = []

    dealer_carden = []

    clock.tick(FPS)
    draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)

    cash, bet = bet_check(cash,player_score, dealer_score, player_carden, dealer_carden,bet)

    run = exit(run)

    player_carden = player_cardo(player_carden)
    draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)

    run = exit(run)

    dealer_carden = dealer_cardo(dealer_carden)
    draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)

    run = exit(run)

    player_carden = player_cardo(player_carden)
    draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)

    run = exit(run)

    dealer_carden = dealer_cardo(dealer_carden)
    draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)

    run = exit(run)

    next, cash = first_check(player_carden, dealer_carden, cash, bet)
    
    if next:
      player_carden, next = morep_cards(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
      if next:
        draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
        cash = opposite_cards(cash,player_score, dealer_score, player_carden, dealer_carden, bet)
    
    if cash == 0:
      player_score = 0
      dealer_score = 0
      draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
      time.sleep(1)
      faitro = HUGE_FONT2.render("You lost all your money!", True, BLUE)
      WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
      pygame.display.update()
      time.sleep(2)
      draw_window(cash,player_score, dealer_score, player_carden, dealer_carden,bet)
      faitro = HUGE_FONT2.render("Thank you for the game!", True, BLUE)
      WIN.blit(faitro,(WIDTH/2-faitro.get_width()/2,HEIGHT/2-faitro.get_height()/2))
      pygame.display.update()
      time.sleep(2)
      run = False

  pygame.quit()

main()