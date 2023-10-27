import requests


# @dataclass
# class Info:
#     names: str = "Unknown"
#     namesPhoneBooks: str = "Unknown"
#     namesDatabaseItems: str = "Unknown"
#     borns: str = "Unknown"
#     phones: str = "Unknown"
#     phoneInfos: str = "Unknown"
#     emails: str = "Unknown"
#     adressess: str = "Unknown"
#     passwords: str = "Unknown"
#     snUrls: str = "Unknown"
#     icQs: str = "Unknown"
#     skypes: str = "Unknown"
#     telegrams: str = "Unknown"
#     iPs: str = "Unknown"
#     snScreenNames: str = "Unknown"
#     professionTypes: str = "Unknown"
#     professions: str = "Unknown"
#     workAdresses: str = "Unknown"
#     passpCompiles: str = "Unknown"
#     inns: str = "Unknown"
#     omses: str = "Unknown"
#     snilses: str = "Unknown"
#     carNs: str = "Unknown"
#     carVins: str = "Unknown"
#     carModels: str = "Unknown"
#     carComments: str = "Unknown"
#     infoAddInfo: str = "Unknown"
#     infoStatuses: str = "Unknown"
#     infoApps: str = "Unknown"
#     infoUserAgents: str = "Unknown"
#     databaseInfo: str = "Unknown"

class Quick:
    def __init__(self, api_key):
        self.token = api_key
        self.url = "https://quickosintapi.com/api/v1/search/agregate/"

    @staticmethod
    def parse_info(findings: dict, query: str) -> tuple[list, list, list]:
        # info = Info()
        # info.names = ", ".join(findings['names'])
        # info.namesPhoneBooks = ", ".join(findings['namesPhoneBooks'])
        # info.namesDatabaseItems = ", ".join(findings['namesDatabaseItems'])
        # info.borns = ", ".join(findings['borns'])
        # info.phones = ", ".join(findings['phones'])
        # info.phoneInfos = ", ".join(findings['phoneInfos'])
        # info.emails = ", ".join(findings['emails'])
        # info.adressess = ", ".join(findings['adressess'])
        # info.passwords = ", ".join(findings['passwords'])
        # info.snUrls = ", ".join(findings['snUrls'])
        # info.icQs = ", ".join(findings['icQs'])
        # info.skypes = ", ".join(findings['skypes'])
        # info.telegrams = ", ".join(findings['telegrams'])
        # info.iPs = ", ".join(findings['iPs'])
        # info.snScreenNames = ", ".join(findings['snScreenNames'])
        # info.professionTypes = ", ".join(findings['professionTypes'])
        # info.professions = ", ".join(findings['professions'])
        # info.workAdresses = ", ".join(findings['workAdresses'])
        # info.passpCompiles = ", ".join(findings['passpCompiles'])
        # info.inns = ", ".join(findings['inns'])
        # info.omses = ", ".join(findings['omses'])
        # info.snilses = ", ".join(findings['snilses'])
        # info.carNs = ", ".join(findings['carNs'])
        # info.carVins = ", ".join(findings['carVins'])
        # info.carModels = ", ".join(findings['carModels'])
        # info.carComments = ", ".join(findings['carComments'])
        # info.infoAddInfo = ", ".join(findings['infoAddInfo'])
        # info.infoStatuses = ", ".join(findings['infoStatuses'])
        # info.infoApps = ", ".join(findings['infoApps'])
        # info.infoUserAgents = ", ".join(findings['infoUserAgents'])
        # info.databaseInfo = ", ".join(findings['databaseInfo'])
        info = [
            {"name": "🔎 Поисковый запрос",
             "result": query},
            {"name": "🤠 Все ФИО объекта",
             "result": ", ".join(findings['names'])},
            {"name": "🥚 ФИО объекта найденные в базах телефонных книг",
             "result": ", ".join(findings['namesPhoneBooks'])},
            {"name": "🥚 ФИО объекта найденные в обычных базах",
             "result": ", ".join(findings['namesDatabaseItems'])},
            {"name": "🎂  Даты рождения",
             "result": ", ".join(findings['borns'])},
            {"name": "📟 Абонентские номера",
             "result": ", ".join(findings['phones'])},
            {"name": "🏬 Страна, регион, оператор сотовой связи",
             "result": ", ".join(findings['phoneInfos'])},
            {"name": "📩 Электронные почты",
             "result": ", ".join(findings['emails'])},
            {"name": "🏠 Адреса",
             "result": ", ".join(findings['adressess'])},
            {"name": "🔐 Пароли",
             "result": ", ".join(findings['passwords'])},
            {"name": "📧 Ссылки на страницы социальных сетей",
             "result": ", ".join(findings['snUrls'])},
            {"name": "😎 Адреса ICQ",
             "result": ", ".join(findings['icQs'])},
            {"name": "👤 Адреса Skype",
             "result": ", ".join(findings['skypes'])},
            {"name": "👤 Аккаунты в мессенджере Телеграм",
             "result": ", ".join(findings['telegrams'])},
            {"name": "🖥 IP адреса",
             "result": ", ".join(findings['iPs'])},
            {"name": "😎 Никнеймы пользователя на сайтах и в соцсетях",
             "result": ", ".join(findings['snScreenNames'])},
            {"name": "💵 Тип профессии",
             "result": ", ".join(findings['professionTypes'])},
            {"name": "💵 Работа/профессия",
             "result": ", ".join(findings['professions'])},
            {"name": "🏠 Рабочий адрес",
             "result": ", ".join(findings['workAdresses'])},
            {"name": "🏷 Паспортные данные",
             "result": ", ".join(findings['passpCompiles'])},
            {"name": "🏷 ИНН",
             "result": ", ".join(findings['inns'])},
            {"name": "🏷 ОМС",
             "result": ", ".join(findings['omses'])},
            {"name": "🏷 СНИЛС",
             "result": ", ".join(findings['snilses'])},
            {"name": "🚘 Гос. номер автомобиля",
             "result": ", ".join(findings['carNs'])},
            {"name": "🚘 VIN номер автомобиля",
             "result": ", ".join(findings['carVins'])},
            {"name": "🚘 Модель автомобиля",
             "result": ", ".join(findings['carModels'])},
            {"name": "🚘 Дополнительная информация по автомобилю",
             "result": ", ".join(findings['carComments'])},
            {"name": "🏦 Статус пользователя",
             "result": ", ".join(findings['infoStatuses'])},
            {"name": "💻 Приложение пользователя через которое он получал доступ к сервису",
             "result": ", ".join(findings['infoApps'])},
            {"name": "🌐 Юзер агент браузера пользователя",
             "result": ", ".join(findings['infoUserAgents'])},
        ]

        info_user = []
        for el in findings['databaseInfo']:
            info_user.append({"result": el})
        info_add_info = []
        for el in findings['infoAddInfo']:
            info_add_info.append({"result": el})
        return info, info_add_info, info_user

    def make_query(self, link: str) -> dict:
        result = requests.get(link, headers={"Authorization": f"Bearer {self.token}",
                                             "X-ClientId": "myClient-896357090909090"})
        return result.json()

    def get_info(self, info: dict, query) -> tuple[list, list, list] | None:
        if info["items"]:
            info = self.parse_info(info["items"][0], query)
            return info

    def get_request_api(self, link, query):
        request = self.make_query(link)
        if "Error" not in request:
            info = self.get_info(request, query)
            return info

    def find(self, choice, query) -> tuple[list, list, list] | None:
        match choice:
            case "по телефону":
                link = f"{self.url}{query}"

            case "по почте":
                link = f"{self.url}{query}"

            case "по паролю":
                link = f"{self.url}pas%20{query}"

            case "по ФИО":
                link = f"{self.url}RU%7C{query}"

            case "по skype":
                link = f"{self.url}skype%20{query}"

            case "по Telegram ID":
                link = f"{self.url}%23id{query}"

            case "по Telegram UserName":
                link = f"{self.url}%40{query}"

            case "по паспорту":
                link = f"{self.url}pasp%20{query}"

            case "по ИНН":
                link = f"{self.url}inn%20{query}"

            case "по СНИЛС":
                link = f"{self.url}snils%20{query}"

            case "по номеру авто":
                link = f"{self.url}{query}"

            case "по VIN авто":
                link = f"{self.url}{query}"

            case "по соцсетям":
                link = f"{self.url}{query.replace('/', '%2F')}"

            case _:
                link = None

        if link:
            info = self.get_request_api(link, query)
            return info
