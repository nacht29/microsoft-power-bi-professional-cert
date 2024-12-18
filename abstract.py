while True:
	try:
		filename = input("File name: ").lower()
	except Exception:
		print()
		break
	except KeyboardInterrupt:
		print()
		break
	else:
		output = filename.replace(' ', '-')
		print(output)
