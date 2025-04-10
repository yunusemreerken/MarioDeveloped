import pygame
import os

	
def display(screen_select):
	# initializing the constructor 
	pygame.init() 


	karakter_path = os.path.join(os.path.dirname(__file__), "assets", "characters", "hero.png")
	karakter = pygame.image.load(karakter_path).convert_alpha()
	#ana menu
	main_menu = ["menu", "start", "learn","creator","exit"]

	
	#color brick
	brick=(0,0,255)
	# screen resolution 
	res = (720,720) 
	# opens up a window 
	screen = pygame.display.set_mode(res) 
	#print(screen)
	
	
	# white color 
	color = (255,255,255) 
	#black color
	black_color =(0,0,0)
	# light shade of the button 
	color_light = (170,170,170) 

	# dark shade of the button 
	color_dark = (100,100,100) 

	# stores the width of the 
	# screen into a variable 
	width = screen.get_width() 

	# stores the height of the 
	# screen into a variable 
	height = screen.get_height() 

	# defining a font 
	smallfont = pygame.font.SysFont('Corbel',30)
	# rendering a text written in 
	# this font 
	menu = smallfont.render('Ana Menü', True, black_color)
	start = smallfont.render('Başla', True, black_color)
	learn = smallfont.render('Oynayış', True, black_color)
	creator = smallfont.render('Yapımcılar', True, black_color)
	exit = smallfont.render('Çıkış', True , black_color)

	secim=True
	while secim: 
		
		for ev in pygame.event.get(): 
			
			if ev.type == pygame.QUIT: 
				pygame.quit() 
			if ev.type == pygame.MOUSEBUTTONDOWN:
				if width/2-75 <= mouse[0] <= width/2+65 and height/2-100 <= mouse[1] <= height/2-50:
					screen_select = main_menu.index("menu")

					print(main_menu[screen_select])
					
			if ev.type == pygame.MOUSEBUTTONDOWN:
				if width/2-75 <= mouse[0] <= width/2+65 and height/2-50 <= mouse[1] <= height/2:
					screen_select = main_menu.index("start")
					print(main_menu[screen_select])
			if ev.type == pygame.MOUSEBUTTONDOWN:
				if width/2-75 <= mouse[0] <= width/2+65 and height/2 <= mouse[1] <= height/2+50:
					screen_select = main_menu.index("learn")
					print(main_menu[screen_select])
			if ev.type == pygame.MOUSEBUTTONDOWN:
				if width/2-75 <= mouse[0] <= width/2+65 and height/2+50 <= mouse[1] <= height/2+100:
					screen_select = main_menu.index("creator")
					print(main_menu[screen_select])

			#checks if a mouse is clicked 
			if ev.type == pygame.MOUSEBUTTONDOWN: 
				
				#if the mouse is clicked on the 
				# button the game is terminated 
				if width/2-75 <= mouse[0] <= width/2+65 and height/2+100 <= mouse[1] <= height/2+150:
					screen_select = main_menu.index("exit") 
					pygame.quit() 
					
		# fills the screen with a color 
		screen.fill("aquamarine")
		
		# stores the (x,y) coordinates into 
		# the variable as a tuple 
		mouse = pygame.mouse.get_pos() 

		# if mouse is hovered on a button it 
		# changes to lighter shade 

		if screen_select==0:

			# superimposing the text onto our button 
			screen.blit(menu , (width/2-75,height/2-100)) 
			screen.blit(start , (width/2-75,height/2-50)) 
			screen.blit(learn , (width/2-75,height/2)) 
			screen.blit(creator , (width/2-75,height/2+50)) 
			screen.blit(exit , (width/2-75,height/2+100))
			screen.blit(karakter,(100,100))

		elif screen_select==1:
				pygame.draw.rect(screen,brick,(0,0,100,50))
				pygame.draw.rect(screen,brick,(0,150,100,50))
				pygame.draw.rect(screen,brick,(0,150,100,50))
				pygame.draw.rect(screen,brick,(100,150,100,50))
				pygame.draw.rect(screen,brick,(150,150,100,50))
				pygame.draw.rect(screen,brick,(200,150,100,50))
				pygame.draw.rect(screen,brick,(250,150,100,50))
				pygame.draw.rect(screen,brick,(300,150,100,50))
				for ev in pygame.event.get(): 
					
					if ev.type == pygame.QUIT: 
						pygame.quit() 
					if ev.type == pygame.MOUSEBUTTONDOWN:
						if 0 <= mouse[0] and 0 <= mouse[1]:
							screen_select = main_menu.index("menu")
							print(main_menu[screen_select])
						
					
		elif screen_select==2:
			print("OYNANIŞ")
			pygame.draw.rect(screen,brick,(0,150,100,50))
			screen_select=0
		elif screen_select==3:
			pygame.draw.rect(screen,brick,(0,0,100,50))
			for ev in pygame.event.get(): 
					
					if ev.type == pygame.QUIT: 
						pygame.quit() 
					if ev.type == pygame.MOUSEBUTTONDOWN:
						if 0 <= mouse[0] and 0 <= mouse[1]:
							screen_select = main_menu.index("menu")
							print(main_menu[screen_select])
			screen.blit(smallfont.render("Y.Emre.E.",True,black_color) , (width/2-75,height/2-100))
			screen.blit(smallfont.render("Yusuf O..",True,black_color) , (width/2-75,height/2-50))
			screen.blit(smallfont.render("Enes Z.",True,black_color) , (width/2-75,height/2))
			screen.blit(smallfont.render("Nurullah K.",True,black_color) , (width/2-75,height/2+50))
			screen.blit(smallfont.render("Berat C.",True,black_color) , (width/2-75,height/2+100))

				

		elif screen_select==4:
			print("ÇIKIŞ")
			screen_select=0

		
		# updates the frames of the game 
		pygame.display.update() 
