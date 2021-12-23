import zipfile, argparse, os

parser = argparse.ArgumentParser(description = "Crea un void world")

parser.add_argument('folder', help = 'Cartella in cui creare il mondo')

args = parser.parse_args()

with zipfile.ZipFile("~/.void", 'r') as zip_ref:
	if not os.path.exists(args.folder):
		os.mkdir(args.folder)
	zip_ref.extractall(args.folder)