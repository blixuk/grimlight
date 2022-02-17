# file: grimlight/client/__main__.py

import pygame

class Client:

	def __init__(self) -> None:
		self.running = False
		self.width = 1080
		self.height = 720
		self.display = pygame.display.set_mode((self.width, self.height))

		self.display.set_caption("Grimlight")

	def run(self) -> None:
		self.running = True
		print("Running client")

		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					pygame.quit()

			self.update()
	
	def update(self) -> None:
		self.display.fill((0, 0, 0))
		self.display.update()

if __name__ == '__main__':
	Client().run()