class MissingEnvironError(Exception):
    def __init__(name: str):
        super(f"Must set {name}")
