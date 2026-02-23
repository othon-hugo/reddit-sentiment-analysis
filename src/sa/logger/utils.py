from logging import INFO
from logging import Logger as _Logger
from logging import StreamHandler


class Logger(_Logger):
    """
    Classe de logging customizável exposta como padrão utilitário no pacote global.

    Interface primária para os demais elementos e plugins do framework
    que necessitam emitir reports porém com comportamentos genéricos.
    Delega atualmente todas definições para seu "Super", estando aberta a
    implantações vindouras de novos recursos de logging que afetem
    toda arquitetura geral, se valendo da técnica de composição por Subclassing.

    Herda de:
        logging.Logger (via alias _Logger)
    """


def create_logger(name: str) -> Logger:
    """
    Função factory que configura a infraesturura mínima em um logger novo.

    Produz e encapsula objetos criados instanciando um console de saída
    básico limitando os reportes através do nível semântico inicial `INFO`.

    Args:
        name (str): Título principal ou classificador que assina de onde a
             referência das informações sendo logadas se despacharam.

    Returns:
        Logger: A interface abstrata para disparo de trace estendido, apontado
           para `stdout` básico nativo.

    Observações:
        - Sem um vinculador de estilo explícito como formatador na linha original,
          ele assumirá saídas plain-texts inerentes ao python/logging.
    """

    logger = Logger(name)
    logger.setLevel(INFO)

    handler = StreamHandler()
    logger.addHandler(handler)

    return logger
