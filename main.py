from __future__ import annotations

import argparse
import os


MESSAGES = {
	"en": "Hello world",
	"es": "Hola mundo",
}


def get_language(cli_language: str | None) -> str:
	language = (cli_language or os.getenv("APP_LANG", "es")).strip().lower()
	return language if language in MESSAGES else "en"


def main() -> None:
	parser = argparse.ArgumentParser(description="Aplicación con cambio de idioma")
	parser.add_argument("--lang", help="Código de idioma, por ejemplo: en o es")
	args = parser.parse_args()

	language = get_language(args.lang)
	print(MESSAGES[language])


if __name__ == "__main__":
	main()