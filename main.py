from __future__ import annotations

import argparse
import os


MESSAGES = {
	"en": "Hello world",
	"es": "Hola mundo",
}

FLAG_PREFIX = "APP_FLAG_"


def get_flag(name: str) -> bool:
	raw_value = os.getenv(f"{FLAG_PREFIX}{name.upper()}", "false").strip().lower()
	return raw_value in {"1", "true", "yes", "on"}


def get_language(cli_language: str | None) -> str:
	language = (cli_language or os.getenv("APP_LANG", "es")).strip().lower()
	return language if language in MESSAGES else "en"


def build_message(language: str, name: str | None) -> str:
	message = MESSAGES[language]
	if not name:
		return message

	if get_flag("concat_name"):
		separator = ", " if language == "es" else ", "
		return f"{message}{separator}{name}"

	return message


def main() -> None:
	parser = argparse.ArgumentParser(description="Aplicación con cambio de idioma")
	parser.add_argument("--lang", help="Código de idioma, por ejemplo: en o es")
	parser.add_argument("--name", help="Nombre a concatenar si el feature flag está activo")
	args = parser.parse_args()

	language = get_language(args.lang)
	print(build_message(language, args.name))


if __name__ == "__main__":
	main()