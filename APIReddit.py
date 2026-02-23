"""Script de coleta de posts do Reddit para análise de sentimentos."""

from __future__ import annotations

import logging
import os
from sys import exit
from pathlib import Path
from typing import NoReturn

from dotenv import load_dotenv

from sa.analysis import Category, Language, CategorizedKeywords
from sa.collector import RedditScrapper
from sa.storage import ExcelPosts
from sa.client import create_reddit_client


OUTPUT_DIR: Path = Path("./data").resolve()
KEYWORDS: CategorizedKeywords = {
    Category.POSITIVE: ["amo", "feliz", "alegre", "adoro"],
    Category.NEGATIVE: ["raiva", "triste", "ódio", "ansioso"],
    Category.NEUTRAL: ["terapia", "autoestima", "sentimento", "apoio"],
}


def fatal(message: str) -> NoReturn:
    logging.getLogger(__name__).fatal(message)
    exit(1)


def main() -> None:
    """Ponto de entrada principal do script de coleta."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    logger = logging.getLogger(__name__)

    load_dotenv(".env")

    try:
        reddit_client_id = os.environ["REDDIT_CLIENT_ID"]
        reddit_client_secret = os.environ["REDDIT_CLIENT_SECRET"]
        reddit_client_user_agent = os.environ["REDDIT_CLIENT_USER_AGENT"]
    except KeyError as e:
        fatal(f"erro ao carregar a variável de ambiente {e}")

    reddit_client = create_reddit_client(
        reddit_client_id,
        reddit_client_secret,
        reddit_client_user_agent,
    )

    scrapper = RedditScrapper(
        reddit_client=reddit_client,
        subreddit_name="conversas",
        logger=logger,
    )

    logger.info("Iniciando a coleta de posts...")

    posts = list(scrapper.collect(ckw=KEYWORDS, lang=Language.PT, total_per_category=100))

    logger.info("Coleta finalizada. Total de posts: %d", len(posts))

    storage = ExcelPosts(OUTPUT_DIR / "teste.xlsx")
    storage.save(posts)

    logger.info("Dados exportados com sucesso.")


if __name__ == "__main__":
    main()
