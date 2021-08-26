import requests
import json
from shools import sed


class Pipf:
    def __init__(self) -> None:
        pass

    @property
    def packages_list(self) -> list:
        doc = requests.get("https://pypi.org/simple").text
        expr = 's/<a href="\/simple\/.*\/">//g; s/<\/a>//g; s/ //g; s/<.*>//g; /^$/d'
        doc = sed(doc, expr)
        return doc.splitlines()

    def get_package_info(self, package_name: str) -> dict:
        resp = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        return json.loads(resp.text)["info"]


class FzfPipf(Pipf):
    def get_package_preview(self, package_name: str) -> str:
        info = self.get_package_info(package_name)
        name = info["name"]
        version = info["version"]
        description = info["summary"]
        keywords = info["keywords"].replace(",", ", ")
        license = info["license"]
        author = info["author"]
        python_version = info["requires_python"].replace(",", ", ")
        return f"""Name           : {name}
Version        : {version}
Description    : {description}
Keywords       : {keywords}
License        : {license}
Author         : {author}
Python version : {python_version}
"""
