# file: grimlight/__main__.py

from command import Command
cmd = Command(description="Grimlight")

from client import __main__

class App:

	def __init__(self) -> None:
		pass

	@cmd.subcommand()
	def nothing(self, args) -> None:
		'''This does nothing special'''
		print("Nothing special!")

	@cmd.subcommand(cmd.argument("-d", help="Debug mode"), cmd.argument("-n", help="No mode", action="store_true"))
	def test(self, args) -> None:
		if args.d:
			print(args.d)
		else:
			print(args)

	@cmd.subcommand(cmd.argument("-f", "--filename", help="A thing with a filename"))
	def filename(self, args) -> None:
		print(args.filename)


	@cmd.subcommand()
	def run(self, args) -> None:
		'''Run the client'''
		__main__.Client().run()

if __name__ == '__main__':
	cmd.parse()