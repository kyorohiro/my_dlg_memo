
from typeguard import typechecked


@typechecked
def main(message:str):
    print(message)

if __name__ == "__main__":
    main("Hello World!!")
    pass

