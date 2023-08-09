import json
from pathlib import Path

from cpf_checker import cpf_checker

account_base = [
    {
        "": {
            "Name": "",
            "Age": "",
            "cpf": "",
        }
    },
]


ROOT_FOLDER = Path(__file__).parent
ACCOUNTS = ROOT_FOLDER / "contas"


class AccountChecker:
    def __init__(self, name: str, age: str, cpf: str) -> None:
        self.name = name
        self.age = age
        self.cpf = cpf

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) <= 3:
            raise ValueError("Digite um nome válido.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: str):
        if value.isdigit():
            age_int = int(value)
        else:
            raise ValueError("Digite uma idade válida.")
        self._age = age_int

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        if cpf_checker(value) is False:
            raise ValueError("Por favor, digite um cpf válido.")
        self._cpf = value


def run_accounts():
    try:
        with open(ACCOUNTS / "JsonArchive", "r", encoding="utf8") as archive:
            persons = json.load(archive)
            for keys in persons:
                account_base.append(keys)
    except FileNotFoundError:
        with open(ACCOUNTS / "JsonArchive", "w", encoding="utf8") as archive:
            ...


def create_account(nome_da_conta):
    try:
        account_name = input("Digite seu nome: ")
        account_age = input("Digite sua idade: ")
        account_cpf = input("Digite sua cpf: ")

        AccountChecker(account_name, account_age, account_cpf)
    except ValueError:
        return print("Sua conta não foi cadastrada.")

    account_base[0][f"{nome_da_conta}"] = account_base[0][""]
    del account_base[0][""]
    account_base[0][f"{nome_da_conta}"]["Name"] = account_name
    account_base[0][f"{nome_da_conta}"]["Age"] = account_age
    account_base[0][f"{nome_da_conta}"]["cpf"] = account_cpf

    run_accounts()

    with open(ACCOUNTS / "JsonArchive", "w", encoding="utf8") as archive:
        json.dump(
            account_base,
            archive,
            ensure_ascii=False,
            indent=2,
        )


def deletar(account_name):
    del account_base[0]

    run_accounts()

    for i, keys in enumerate(account_base):
        if account_name in keys:
            del account_base[i]
    with open(ACCOUNTS / "JsonArchive", "w", encoding="utf8") as archive:
        json.dump(
            account_base,
            archive,
            ensure_ascii=False,
            indent=2,
        )


account_id = input("Crie o id da sua conta: ")
create_account(account_id)
