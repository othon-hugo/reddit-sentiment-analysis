"""Script de coleta de posts do Reddit para análise de sentimentos."""

from __future__ import annotations

import logging
import os
from sys import exit, argv
from typing import NoReturn, TYPE_CHECKING

from dotenv import load_dotenv

from sa.analysis import Language, Category
from sa.client import create_reddit_client
from sa.collector import RedditScrapper
from sa.parser import parse_reddit_args
from sa.storage import CSVPosts, XLSXPosts, StorageFormat

if TYPE_CHECKING:
    from sa.analysis import CategorizedKeywords

DEFAULT_KEYWORDS: "CategorizedKeywords" = {
    Category.POSITIVE: ["amo", "feliz", "alegre", "adoro"],
    Category.NEGATIVE: ["raiva", "triste", "ódio", "ansioso"],
    Category.NEUTRAL: ["terapia", "autoestima", "sentimento", "apoio"],
}


def fatal(message: str) -> NoReturn:
    logging.getLogger(__name__).fatal(message)
    exit(1)


def main() -> None:
    """Ponto de entrada principal do script de coleta."""

    load_dotenv(".env")

    try:
        reddit_client_id = os.environ["REDDIT_CLIENT_ID"]
        reddit_client_secret = os.environ["REDDIT_CLIENT_SECRET"]
        reddit_client_user_agent = os.environ["REDDIT_CLIENT_USER_AGENT"]
    except KeyError as e:
        fatal(f"erro ao carregar a variável de ambiente {e}")

    args = parse_reddit_args(argv[1:])

    reddit_client = create_reddit_client(
        reddit_client_id,
        reddit_client_secret,
        reddit_client_user_agent,
    )

    for subreddit in args.subreddits:
        logger = logging.Logger(subreddit)
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - r/%(name)s - %(levelname)s - %(message)s")

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        scrapper = RedditScrapper(
            reddit_client=reddit_client,
            subreddit_name=subreddit,
            logger=logger,
        )

        logger.info("Iniciando a coleta de posts...")

        posts = list(
            scrapper.collect(
                ckw=DEFAULT_KEYWORDS,
                lang=Language(args.language),
                total_per_category=args.total,
            )
        )

        logger.info("Coleta finalizada. Total de posts: %d", len(posts))

        output_filepath = args.output.resolve()

        match args.format:
            case StorageFormat.CSV:
                logger.info("Exportando dados para CSV...")

                CSVPosts(output_filepath).save(posts)
            case StorageFormat.XLSX:
                logger.info("Exportando dados para XLSX...")

                XLSXPosts(output_filepath).save(posts)
            case _:
                logger.error("Formato de armazenamento desconhecido: %s", args.format)

        logger.info("Dados exportados com sucesso em %s", output_filepath)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nColeta interrompida pelo usuário.")
