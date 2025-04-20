import json
import typing


END_SIGNAL = "END"
END_INIT_SIGNAL = "END_INIT"


def post_message(message: typing.Dict):
    """
    Converts the given message to a JSON and prints it for the game server.
    :param message: Message to be printed - it should be a dict and should convert to JSON without error.
    """
    print(json.dumps(message))


def read_message() -> typing.Union[str, typing.Dict[str, dict]]:
    """
    Reads the next message from the game server.
    :return: The parsed message. If the message is a signal (end game or end init) then the return type will be string
        otherwise it will be a dict.
    """
    return json.loads(input())
