from rpa.tasks.task import Task
from rpa.drivers import Sequence
from rpa.jobs import NavigateJob, SelectElementJob, TypeInputMaskJob
from rpa.jobs import ButtonClickJob, LookupBy, SwitchFrameSelectJob
from rpa.jobs import ListJob, LookupStock
from rpa.entitys import User


class Clear(Task):

    _user: User
    _t_date: str

    def __init__(self, user: User, t_date: str):
        self._user = user
        self._t_date = t_date

    def Login(self) -> Sequence:
        return Sequence([
            NavigateJob(url="https://login.clear.com.br/pit/login/", time=5),
            SelectElementJob(
                '//div[@class="form-group cont_inputs filledIdentificationNumber"]//input[@id="identificationNumber"]'),
            TypeInputMaskJob(self._user.login),
            SelectElementJob(
                '//div[@class="form-group cont_inputs fifty sdate filledDob"]//input[@id="dob"]'),
            TypeInputMaskJob(self._t_date),
            SelectElementJob(
                '//div[@class="form-group cont_inputs fifty field filledPassword"]//*[@id="password"]'),
            TypeInputMaskJob(self._user.password),
            ButtonClickJob(
                '/html/body/div/div[2]/div[3]/form/div[2]/div[4]/button'),
        ])

    def ListWallet(self, wallet_name: str) -> Sequence:
        return Sequence([
            NavigateJob(
                "https://pro.clear.com.br/#renda-variavel/swing-trade", 5),
            SwitchFrameSelectJob('content-page', '//div[@class="tabs--items"]/ul').apply(
                LookupBy(wallet_name, lambda el:
                         el.click() if el.get_attribute('class') != 'active' else print('no click but is active'))
            ),
            SelectElementJob('//div[@class="equities widget-stone-equities"]'),
            ListJob('//div[@class="AssetListItem ui-sortable-handle"]').apply(
                LookupStock()
            )
        ])
