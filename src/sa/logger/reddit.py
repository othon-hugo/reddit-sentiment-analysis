from logging import INFO, Formatter, Logger, StreamHandler


class RedditLogger(Logger):
    """
    Subclasse especializada de Logger destinada ao acompanhamento das coletas no Reddit.

    Encapsula o formato de apresentação em texto, identificando de modo padrão o
    subreddit alvo como o nome do canal ("nome" dentro do record) ao qual o
    log pertence. Facilita o monitoramento ao estruturar as mensagens em um
    formato claro, sendo projetada para acompanhar processos baseados em tempo.

    Herda de:
        Logger: Herda do logger padrão Python da biblioteca interna `logging`.

    Attributes:
        formatter (Formatter): Objeto compartilhando as formatações estáticas da string
            imprimida contendo campos temporais asctime, o nome e status (level).

    Observações:
        - Esta classe aplica configurações base, mas os manipuladores (Handlers)
          reais precisam ser adicionados pelo construtor factory da classe.
    """

    formatter = Formatter("%(asctime)s - r/%(name)s - %(levelname)s - %(message)s")


def create_reddit_logger(subreddit: str) -> RedditLogger:
    """
    Função factory que instancia e anexa manipuladores a um recém criado `RedditLogger`.

    Constrói e monta o conduto necessário de saída padrão console e fixa o
    status level de report para o nível INFO. Anexa efetivamente o `StreamHandler`
    através da constante de formatadores pre-definidas da classe invocada.

    Args:
        subreddit (str): A string referente ao nome da comunidade sem abreviaturas
            sendo usada também como identificação de nome contextual do logger (r/nome).

    Returns:
        RedditLogger: O objeto estendido com permissão INFO, dotado de conector
            exibidor na interface do sistema que executa e configurado visualmente.

    Observações:
        - Padrão utilizado: Factory Method voltado para configuração em logging.
    """

    logger = RedditLogger(subreddit)
    logger.setLevel(INFO)

    handler = StreamHandler()
    handler.setFormatter(RedditLogger.formatter)

    logger.addHandler(handler)

    return logger
