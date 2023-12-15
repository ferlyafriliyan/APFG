#!/usr/bin/python3
# coding=utf-8
# Recode Boleh,Tapi Jangan Lupa Follow Dan Kasih Bintangnya...
__Author__ = "Juan Hulu"
__Whatsapp__ = "082298962122"
import os, sys, time, random, re, json, datetime, shutil, urllib

try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import bs4
except ImportError:
    os.system("pip install bs4")
try:
    import rich
except ImportError:
    os.system("pip install rich")
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
try:
    import names
except ImportError:
    os.system("pip install names")
try:
    import requests_toolbelt
except ImportError:
    os.system("pip install requests_toolbelt")
from bs4 import BeautifulSoup as bs
from rich import print
from rich.panel import Panel as panel
from rich.console import Console
from rich.columns import Columns as colum
from time import sleep, strftime
from concurrent.futures import ThreadPoolExecutor
from random import choice as rc
from random import randrange as rr

dic = {
    "1": "Januari",
    "2": "Februari",
    "3": "Maret",
    "4": "April",
    "5": "Mei",
    "6": "Juni",
    "7": "Juli",
    "8": "Agustus",
    "9": "September",
    "10": "Oktober",
    "11": "November",
    "12": "Desember",
}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
dic2 = {
    "Monday": "Senin",
    "Tuesday": "Selasa",
    "Wednesday": "Rabu",
    "Thursday": "Kamis",
    "Friday": "Jumat",
    "Saturday": "Sabtu",
    "Sunday": "Minggu",
}
hari = dic2[(str(strftime("%A")))]
default_ua_windows = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
random_ua_windows = (
    lambda: "Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36"
    % (rc(["10", "11"]), rr(110, 201), rr(0, 10), rr(0, 10), rr(0, 10))
)
headers_get = lambda i=default_ua_windows: {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Dpr": "1",
    "Pragma": "akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-True-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace",
    "Sec-Ch-Prefers-Color-Scheme": "dark",
    "Sec-Ch-Ua": "",
    "Sec-Ch-Ua-Full-Version-List": "",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "",
    "Sec-Ch-Ua-Platform": "",
    "Sec-Ch-Ua-Platform-Version": "",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": i,
}
headers_post = lambda i=default_ua_windows: {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.facebook.com",
    "Sec-Ch-Prefers-Color-Scheme": "dark",
    "Sec-Ch-Ua": "",
    "Sec-Ch-Ua-Full-Version-List": "",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "",
    "Sec-Ch-Ua-Platform": "",
    "Sec-Ch-Ua-Platform-Version": "",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": i,
}
input = Console(style="bold white").input


def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ---> Get Data From Dapunta
def GetData(req):
    try:
        actor = re.search('"actorID":"(.*?)"', str(req)).group(1)
        haste = re.search('"haste_session":"(.*?)"', str(req)).group(1)
        conne = re.search('"connectionClass":"(.*?)"', str(req)).group(1)
        spinr = re.search('"__spin_r":(.*?),', str(req)).group(1)
        spinb = re.search('"__spin_b":"(.*?)"', str(req)).group(1)
        spint = re.search('"__spin_t":(.*?),', str(req)).group(1)
        hsi = re.search('"hsi":"(.*?)"', str(req)).group(1)
        comet = re.search('"comet_env":(.*?),', str(req)).group(1)
        dtsg = re.search('{"token":"(.*?)"', str(req)).group(1)
        jazoest = re.search('&jazoest=(.*?)"', str(req)).group(1)
        lsd = re.search('"LSD",\[\],{"token":"(.*?)"}', str(req)).group(1)
        dta = {
            "av": actor,
            "__user": actor,
            "__a": "1",
            "__hs": haste,
            "dpr": "1",
            "__ccg": conne,
            "__rev": spinr,
            "__hsi": hsi,
            "__comet_req": comet,
            "fb_dtsg": dtsg,
            "jazoest": jazoest,
            "lsd": lsd,
            "__spin_r": spinr,
            "__spin_b": spinb,
            "__spin_t": spint,
        }
        return dta
    except Exception as e:
        Console(style="bold white").print(f"   └─> [bold red]Error:{e}", end="\r")
        sleep(2)


def myname(cookie, token):
    with requests.Session() as r:
        r.headers.update(
            {
                "cookie": cookie,
                "user-agent": "Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]",
                "host": "graph.facebook.com",
            }
        )
        response = r.get(
            "https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}".format(
                token
            )
        ).json()
        if "name" in str(response) and "id" in str(response):
            return response["name"].title(), response["id"]
        else:
            Console(width=60).print(
                panel("[bold red]Cookie Invalid", width=60, style="bold white"),
                justify="center",
            )
            sleep(2)
            login_cookie().login()


class Terminal_Size:
    def __init__(self):
        self.lebar, self.panjang = shutil.get_terminal_size()
        self.__main__()

    def __main__(self):
        if self.lebar == 60 or self.lebar > 60:
            pass
        else:
            clear()
            Console(width=self.lebar).print(
                "Harap Perkecil Layar Terminal Anda Dengan Cara Mencubit Layar Hingga Tampilan Garis Dibawah Tidak Terlihat Putus-Putus",
                justify="center",
            )
            Console().print("_" * 60)
            exit()


class baner:
    def __init__(self):
        clear()
        self.__main__()

    def __main__(self):
        Console(width=60, style="bold white").print(
            panel(
                """[bold green] ____  ____        [bold red]____  ____  ____  ____   \n[bold green]( ___)(  _ \  [bold white]___ [bold red]( ___)( ___)( ___)(  _ \   \n[bold green]  )__)  ) _ < [bold white](___) [bold red])__)  )__)  )__)  )(_) )  \n[bold green](__)  (____/      [bold red](__)  (____)(____)(____/    \n""",
                width=60,
                title="[bold yellow]>[bold green]>[bold cyan]> [bold white]AUTO POST FACEBOOK in GRUP[bold cyan]<[bold green]<[bold yellow]<",
            ),
            justify="center",
        )


class login_cookie:
    def __init__(self):
        self.r______ = requests.Session()

    def login(self):
        baner()
        Console(width=60).print(
            panel(
                "Masukan Cookie Akun Facebook",
                width=60,
                style="bold white",
                subtitle="┌",
                subtitle_align="left",
            ),
            justify="center",
        )
        self.cookie = input("   └─> ")
        self.language(self.cookie)
        head = {
            "cookie": self.cookie,
            "user-agent": "Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]",
            "host": "business.facebook.com",
        }
        response = self.r______.get(
            "https://business.facebook.com/business_locations", headers=head
        ).text
        tokenku = re.search("(EAAG\w+)", str(response)).group(1)
        name, id = myname(self.cookie, tokenku)
        open("Data/Cookie.txt", "w").write(self.cookie)
        open("Data/Token.txt", "w").write(tokenku)
        Console(width=60).print(
            panel(
                f"[bold green]{name}",
                width=60,
                style="bold white",
                title="[bold yellow]>[bold green]>[bold cyan]> [bold white]Anda Login Ke Facebook Sebagai [bold cyan]<[bold green]<[bold yellow]<",
            ),
            justify="center",
        )
        sleep(2)
        clear()
        ________________________Menu________________________()

    def language(self, cookiee):
        try:
            cookie = {"cookie": cookiee}
            req = self.r______.get(
                "https://mbasic.facebook.com/language/", cookies=cookie
            )
            pra = bs(req.content, "html.parser")
            for x in pra.find_all("form", {"method": "post"}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {
                        "fb_dtsg": re.search(
                            'name="fb_dtsg" value="(.*?)"', str(req.text)
                        ).group(1),
                        "jazoest": re.search(
                            'name="jazoest" value="(.*?)"', str(req.text)
                        ).group(1),
                        "submit": "Bahasa Indonesia",
                    }
                    url = "https://free.facebook.com" + x["action"]
                    post = self.r______.post(url, data=bahasa, cookies=cookie)
        except Exception as e:
            pass


class ________________________Menu________________________:
    def __init__(self):
        baner()
        try:
            cookie, tokenku = (
                open("Data/Cookie.txt", "r", encoding="utf-8").read(),
                open("Data/Token.txt", "r", encoding="utf-8").read(),
            )
            self.name, self.id = myname(cookie, tokenku)
        except Exception as e:
            Console(width=60, style="bold white").print(
                panel(
                    f"[bold red]Cookie Expired Silahkan Masukan Cookie Baru !",
                    width=60,
                    title=f"[bold red]>[bold yellow]>[bold green]>[bold red]Expired[bold green]<[bold yellow]<[bold red]<",
                ),
                justify="center",
            )
            sleep(3)
            login_cookie().login()
        self.__main__()

    def __main__(self):
        Console(width=60, style="bold white").print(
            panel(
                f"""Name : {self.name}   ID : {self.id}""",
                width=60,
                title="[bold yellow]>[bold green]>[bold cyan]> [bold white]Welcome [bold cyan]<[bold green]<[bold yellow]<",
            ),
            justify="center",
        )
        Console(width=60, style="bold white").print(
            panel(
                """[bold green][[bold white]01[bold green]].[bold white]Auto Posting Group Image\n[bold green][[bold white]02[bold green]].[bold white]Auto Posting Group Text\n[bold green][[bold white]03[bold green]].[bold white]Requests Fitur\n[bold green][[bold white]04[bold green]].[bold red]Logout""",
                width=60,
                subtitle="┌",
                subtitle_align="left",
                title="[bold yellow]>[bold green]>[bold cyan]> [bold white]MENU [bold cyan]<[bold green]<[bold yellow]<",
            )
        )
        ______Choice______ = input("   └─> ").lower()
        if ______Choice______ in ("1", "01"):
            __________________________________________________________________________()
        elif ______Choice______ in ("2", "02"):
            ___________________________________________________________________________()
        elif ______Choice______ in ("3", "03"):
            ____________________________________________________________________________()
        elif ______Choice______ in ("4", "04"):
            try:
                open("Data/Cookie.txt", "w")
                open("Data/Token.txt", "w")
                sleep(2)
                login_cookie().login()
            except:
                login_cookie().login()
        else:
            Console().print("   └─> [bold red]Pilih Yang Benar")
            sleep(2)
            ________________________Menu________________________()


class __________________________________________________________________________:
    def __init__(self):
        try:
            Cookie, Tokenku = (
                open("Data/Cookie.txt", "r", encoding="utf-8").read(),
                open("Data/Token.txt", "r", encoding="utf-8").read(),
            )
        except Exception as e:
            Console(width=60, style="bold white").print(
                panel(
                    f"[bold red]Cookie Expired Silahkan Masukan Cookie Baru !",
                    width=60,
                    title=f"[bold red]>[bold yellow]>[bold green]>[bold red]Expired[bold green]<[bold yellow]<[bold red]<",
                ),
                justify="center",
            )
            sleep(3)
            login_cookie().login()
        self.GroupID = []
        self.GroupInfoPrivacy = {}
        self.GroupInfoName = {}
        self.__________________Author__________________(Cookie, Tokenku)
        Console(width=60).print(
            panel(
                f"[bold white]Jumlah Grup Dimana Anda Bergabung [bold green]({len(self.GroupID)})",
                width=60,
                style="bold white",
                title="[bold yellow]>[bold green]>[bold cyan]> [bold white]Jumlah Grup [bold cyan]<[bold green]<[bold yellow]<",
            ),
            justify="center",
        )
        Console(width=60).print(
            panel(
                "Masukan Text Untuk Postingan",
                width=60,
                style="bold white",
                subtitle="┌",
                subtitle_align="left",
            ),
            justify="center",
        )
        PostText = input("   └─> ")
        Console(width=60).print(
            panel(
                "Masukan Lokasi Gambar,Misalnya [bold green]/sdcard/image.jpg\n[white]Anda Juga Dapat Memasukan URl,Misalnya [bold green]https://example.com/image.jpg",
                width=60,
                style="bold white",
                subtitle="┌",
                subtitle_align="left",
            ),
            justify="center",
        )
        PathImage = input("   └─> ")
        Console(width=60).print(
            panel(
                "Masukan Delay Dalam Menit,Saran 2-3 Menit",
                width=60,
                style="bold white",
                subtitle="┌",
                subtitle_align="left",
            ),
            justify="center",
        )
        InputDelay = input("   └─> ")
        Delay = int(InputDelay) * 60
        Console(width=60).print(
            panel('Tekan "Ctrl + C" Untuk Berhenti', width=60, style="bold white"),
            justify="center",
        )
        self.____________________Author____________________(
            Cookie, PostText, PathImage, Delay
        )
        self.Selesai()

    def _________________Author_________________(self, Delay):
        for x in range(Delay + 1):
            Console(style="bold white").print(
                f"\r   └─> Tunggu {str(Delay)} Detik               ", end="\r"
            )
            Delay -= 1
            if Delay == 0:
                break
            else:
                sleep(1)

    def __________________Author__________________(self, Cookie, Tokenku):
        with requests.Session() as r:
            r.cookies.update({"cookie": Cookie})
            url = "https://graph.facebook.com/v13.0/me/groups?access_token={}".format(
                Tokenku
            )
            response = r.get(url)
            for data in response.json()["data"]:
                GrupName = data["name"]
                GrupID = data["id"]
                Privacy = data["privacy"]
                self.GroupID.append(GrupID)
                self.GroupInfoPrivacy.update({GrupID: Privacy})
                self.GroupInfoName.update({GrupID: GrupName})
            if "next" in response.text:
                next = response.json()["paging"]["next"]
                self.___________________Author___________________(
                    r, next, Cookie, Tokenku
                )

    def ___________________Author___________________(self, r, next, Cookie, Tokenku):
        response = r.get(next, cookies={"cookie": Cookie})
        for data in response.json()["data"]:
            GrupName = data["name"]
            GrupID = data["id"]
            Privacy = data["privacy"]
            if GrupID in self.GroupInfoPrivacy:
                pass
            else:
                self.GroupID.append(GrupID)
                self.GroupInfoPrivacy.update({GrupID: Privacy})
                self.GroupInfoName.update({GrupID: GrupName})
        if "next" in response.text:
            next = response.json()["paging"]["next"]
            self.___________________Author___________________(r, next, Cookie, Tokenku)

    def ____________________Author____________________(
        self, Cookie, PostText, PathImage, Delay
    ):
        try:
            if __Author__ != "uluH nauJ"[::-1]:
                exit("Stop Recode Bg...!!!")
            else:
                with requests.Session() as r:
                    r.cookies.update({"cookie": Cookie})
                    for IDGrup in self.GroupID:
                        try:
                            NameGrup = self.GroupInfoName[IDGrup]
                            privasi = self.GroupInfoPrivacy[IDGrup]
                            if (
                                privasi == "OPEN"
                                or "OPEN" in privasi
                                or privasi in ["OPEN"]
                            ):
                                GrupStatus = "Publik"
                            else:
                                GrupStatus = "Private"
                            response = bs(
                                r.get(
                                    "https://www.facebook.com/{}".format(IDGrup),
                                    headers=headers_get(),
                                    allow_redirects=True,
                                    timeout=(10, 20),
                                ).content,
                                "html.parser",
                            )
                            data = GetData(response)
                            sessionID = re.search(
                                '"sessionID":"(.*?)"', str(response)
                            ).group(1)
                            if "https://" in str(PathImage):
                                if ".png" in str(PathImage):
                                    dtf = {
                                        "file": (
                                            "image.png",
                                            urllib.request.urlopen(PathImage).read(),
                                        )
                                    }
                                else:
                                    dtf = {
                                        "file": (
                                            "image.jpg",
                                            urllib.request.urlopen(PathImage).read(),
                                        )
                                    }
                                dat = data.copy()
                                dat.update(
                                    {
                                        "source": "8",
                                        "profile_id": data["__user"],
                                        "waterfallxapp": "comet",
                                        "farr": dtf,
                                    }
                                )
                                pos = r.post(
                                    "https://upload.facebook.com/ajax/react_composer/attachments/photo/upload",
                                    data=dat,
                                    files=dtf,
                                    cookies={"cookie": Cookie},
                                    allow_redirects=True,
                                ).textid_foto = re.search(
                                    '"photoID":"(.*?)"', str(pos)
                                ).group(1)
                                PostImage = [{"photo": {"id": id_foto}}]
                            else:
                                if ".png" in str(PathImage):
                                    dtf = {
                                        "file": (
                                            "image.png",
                                            open(PathImage, "rb").read(),
                                        )
                                    }
                                else:
                                    dtf = {
                                        "file": (
                                            "image.jpg",
                                            open(PathImage, "rb").read(),
                                        )
                                    }
                                dat = data.copy()
                                dat.update(
                                    {
                                        "source": "8",
                                        "profile_id": data["__user"],
                                        "waterfallxapp": "comet",
                                        "farr": dtf,
                                    }
                                )
                                pos = r.post(
                                    "https://upload.facebook.com/ajax/react_composer/attachments/photo/upload",
                                    data=dat,
                                    files=dtf,
                                    cookies={"cookie": Cookie},
                                    allow_redirects=True,
                                ).text
                                id_foto = re.search(
                                    '"photoID":"(.*?)"', str(pos)
                                ).group(1)
                                PostImage = [{"photo": {"id": id_foto}}]
                                var = {
                                    "input": {
                                        "composer_entry_point": "publisher_bar_media",
                                        "composer_source_surface": "group",
                                        "composer_type": "group",
                                        "logging": {"composer_session_id": sessionID},
                                        "source": "WWW",
                                        "attachments": PostImage,
                                        "message": {"ranges": [], "text": PostText},
                                        "with_tags_ids": [],
                                        "inline_activities": [],
                                        "explicit_place_id": "0",
                                        "text_format_preset_id": "0",
                                        "navigation_data": {
                                            "attribution_id_v2": "CometGroupDiscussionRoot.react,comet.group,unexpected,1701586943269,191889,2361831622,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1701586925298,355211,391724414624676,304#10#230#301,"
                                        },
                                        "tracking": [None],
                                        "event_share_metadata": {"surface": "newsfeed"},
                                        "audience": {"to_id": IDGrup},
                                        "actor_id": data["__user"],
                                        "client_mutation_id": "15",
                                    },
                                    "displayCommentsFeedbackContext": None,
                                    "displayCommentsContextEnableComment": None,
                                    "displayCommentsContextIsAdPreview": None,
                                    "displayCommentsContextIsAggregatedShare": None,
                                    "displayCommentsContextIsStorySet": None,
                                    "feedLocation": "GROUP",
                                    "feedbackSource": 0,
                                    "focusCommentID": None,
                                    "gridMediaWidth": None,
                                    "groupID": None,
                                    "scale": 1,
                                    "privacySelectorRenderLocation": "COMET_STREAM",
                                    "checkPhotosToReelsUpsellEligibility": False,
                                    "renderLocation": "group",
                                    "useDefaultActor": False,
                                    "inviteShortLinkKey": None,
                                    "isFeed": False,
                                    "isFundraiser": False,
                                    "isFunFactPost": False,
                                    "isGroup": True,
                                    "isEvent": False,
                                    "isTimeline": False,
                                    "isSocialLearning": False,
                                    "isPageNewsFeed": False,
                                    "isProfileReviews": False,
                                    "isWorkSharedDraft": False,
                                    "UFI2CommentsProvider_commentsKey": "CometGroupDiscussionRootSuccessQuery",
                                    "hashtag": None,
                                    "canUserManageOffers": False,
                                    "__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider": False,
                                    "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": True,
                                    "__relay_internal__pv__IsWorkUserrelayprovider": False,
                                    "__relay_internal__pv__IsMergQAPollsrelayprovider": False,
                                    "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider": False,
                                    "__relay_internal__pv__StoriesRingrelayprovider": True,
                                }
                                data.update(
                                    {
                                        "fb_api_caller_class": "RelayModern",
                                        "fb_api_req_friendly_name": "ComposerStoryCreateMutation",
                                        "variables": json.dumps(var),
                                        "doc_id": "7567571293271079",
                                        "fb_api_analytics_tags": '["qpl_active_flow_ids=431626709"]',
                                    }
                                )
                                response = r.post(
                                    "https://www.facebook.com/api/graphql",
                                    data=data,
                                    headers=headers_post(),
                                )
                                Time = strftime("%T")
                            if '"Postingan Anda menunggu persetujuan"' in response.text:
                                Console(width=60, style="bold white").print(
                                    panel(
                                        f"""[bold yellow]Status    : [white]Ditinjau\n[bold yellow]Nama Grup : [white]{NameGrup}\n[bold yellow]ID Grup   : [white]{IDGrup}\n[bold yellow]Privacy   : [white]{GrupStatus}\n[bold yellow]Time      : [white]{Time}"""
                                    )
                                )
                                self._________________Author_________________(Delay)
                            elif (
                                '"is_marked_as_spam_by_admin_assistant": true'
                                in response.text
                            ):
                                Console(width=60, style="bold white").print(
                                    panel(
                                        f"""[bold yellow]Status    : [white]Sedang Ditinjau (Berpotensi Spam)\n[bold yellow]Nama Grup : [white]{NameGrup}\n[bold yellow]ID Grup   : [white]{IDGrup}\n[bold yellow]Privacy   : [white]{GrupStatus}\n[bold yellow]Time      : [white]{Time}"""
                                    )
                                )
                                self._________________Author_________________(Delay)
                            else:
                                BsResponse = response.text
                                PostUrl = re.findall(
                                    '"scheduled_publish_time":0,"url":"(.*?)"',
                                    BsResponse,
                                )[0].replace("\\", "")
                                Console(width=60, style="bold white").print(
                                    panel(
                                        f"""[bold green]Status    : [white]Success\n[bold green]Nama Grup : [white]{NameGrup}\n[bold green]ID Grup   : [white]{IDGrup}\n[bold green]Privacy   : [white]{GrupStatus}\n[bold green]Url Post  : [white]{PostUrl}\n[bold green]Time      : [white]{Time}"""
                                    )
                                )
                                self._________________Author_________________(Delay)
                        except Exception as e:
                            Console(style="bold white").print(
                                f"   └─> [bold red]Error:[bold white]{IDGrup}", end="\r"
                            )
                            sleep(2)
        except (NameError, Exception):
            exit("Stop Recode Bg...!!!")

    def Selesai(self):
        Console(width=60).print(
            panel(
                "[bold green]Selesai",
                width=60,
                style="bold white",
                title="[bold yellow]>[bold green]>[bold cyan]> [bold white]Selesai [bold cyan]<[bold green]<[bold yellow]<",
            ),
            justify="center",
        )
        exit()


class ____________________________________________________________________________:
    def __init__(self):
        self.__main__()

    def __main__(self):
        Console(width=60, style="bold white").print(
            panel(
                "Silahkan Kirim Pesan Ke Whatsapp : [bold green]{}".format(
                    __Whatsapp__
                ),
                width=60,
            ),
            justify="center",
        )


class ___________________________________________________________________________:
    def __init__(self):
        try:
            Cookie, Tokenku = (
                open("Data/Cookie.txt", "r", encoding="utf-8").read(),
                open("Data/Token.txt", "r", encoding="utf-8").read(),
            )
        except Exception as e:
            Console(width=60, style="bold white").print(
                panel(
                    f"[bold red]Cookie Expired Silahkan Masukan Cookie Baru !",
                    width=60,
                    title=f"[bold red]>[bold yellow]>[bold green]>[bold red]Expired[bold green]<[bold yellow]<[bold red]<",
                ),
                justify="center",
            )
            sleep(3)
            login_cookie().login()
        self.GroupID = []
        self.GroupInfoPrivacy = {}
        self.GroupInfoName = {}
        self.__________________Author__________________(Cookie, Tokenku)
        Console(width=60).print(
            panel(
                f"[bold white]Jumlah Grup Dimana Anda Bergabung [bold green]({len(self.GroupID)})",
                width=60,
                style="bold white",
                title="[bold yellow]>[bold green]>[bold cyan]> [bold white]Jumlah Grup [bold cyan]<[bold green]<[bold yellow]<",
            ),
            justify="center",
        )
        Console(width=60).print(
            panel(
                "Masukan Text Untuk Postingan",
                width=60,
                style="bold white",
                subtitle="┌",
                subtitle_align="left",
            ),
            justify="center",
        )
        PostText = input("   └─> ")
        Console(width=60).print(
            panel(
                "Masukan Delay Dalam Menit,Saran 2-3 Menit",
                width=60,
                style="bold white",
                subtitle="┌",
                subtitle_align="left",
            ),
            justify="center",
        )
        InputDelay = input("   └─> ")
        Delay = int(InputDelay) * 60
        Console(width=60).print(
            panel('Tekan "Ctrl + C" Untuk Berhenti', width=60, style="bold white"),
            justify="center",
        )
        self.____________________Author____________________(Cookie, PostText, Delay)
        self.Selesai()

    def _________________Author_________________(self, Delay):
        for x in range(Delay + 1):
            Console(style="bold white").print(
                f"\r   └─> Tunggu {str(Delay)} Detik               ", end="\r"
            )
            Delay -= 1
            if Delay == 0:
                break
            else:
                sleep(1)

    def __________________Author__________________(self, Cookie, Tokenku):
        with requests.Session() as r:
            r.cookies.update({"cookie": Cookie})
            url = "https://graph.facebook.com/v13.0/me/groups?access_token={}".format(
                Tokenku
            )
            response = r.get(url)
            for data in response.json()["data"]:
                GrupName = data["name"]
                GrupID = data["id"]
                Privacy = data["privacy"]
                self.GroupID.append(GrupID)
                self.GroupInfoPrivacy.update({GrupID: Privacy})
                self.GroupInfoName.update({GrupID: GrupName})
            if "next" in response.text:
                next = response.json()["paging"]["next"]
                self.___________________Author___________________(
                    r, next, Cookie, Tokenku
                )

    def ___________________Author___________________(self, r, next, Cookie, Tokenku):
        response = r.get(next, cookies={"cookie": Cookie})
        for data in response.json()["data"]:
            GrupName = data["name"]
            GrupID = data["id"]
            Privacy = data["privacy"]
            if GrupID in self.GroupInfoPrivacy:
                pass
            else:
                self.GroupID.append(GrupID)
                self.GroupInfoPrivacy.update({GrupID: Privacy})
                self.GroupInfoName.update({GrupID: GrupName})
        if "next" in response.text:
            next = response.json()["paging"]["next"]
            self.___________________Author___________________(r, next, Cookie, Tokenku)

    def ____________________Author____________________(self, Cookie, PostText, Delay):
        try:
            if __Author__ != "uluH nauJ"[::-1]:
                exit("Stop Recode Bg...!!!")
            else:
                with requests.Session() as r:
                    r.cookies.update({"cookie": Cookie})
                    for IDGrup in self.GroupID:
                        try:
                            NameGrup = self.GroupInfoName[IDGrup]
                            privasi = self.GroupInfoPrivacy[IDGrup]
                            if (
                                privasi == "OPEN"
                                or "OPEN" in privasi
                                or privasi in ["OPEN"]
                            ):
                                GrupStatus = "Publik"
                            else:
                                GrupStatus = "Private"
                            response = bs(
                                r.get(
                                    "https://www.facebook.com/{}".format(IDGrup),
                                    headers=headers_get(),
                                    allow_redirects=True,
                                    timeout=(10, 20),
                                ).content,
                                "html.parser",
                            )
                            data = GetData(response)
                            sessionID = re.search(
                                '"sessionID":"(.*?)"', str(response)
                            ).group(1)
                            Variable = {
                                "input": {
                                    "composer_entry_point": "hosted_inline_composer",
                                    "composer_source_surface": "group",
                                    "composer_type": "group",
                                    "logging": {"composer_session_id": sessionID},
                                    "source": "WWW",
                                    "attachments": [],
                                    "message": {"ranges": [], "text": PostText},
                                    "with_tags_ids": [],
                                    "inline_activities": [],
                                    "explicit_place_id": "0",
                                    "text_format_preset_id": "0",
                                    "navigation_data": {
                                        "attribution_id_v2": "CometGroupDiscussionRoot.react,comet.group,unexpected,1702608397313,343676,2361831622,,;GroupsCometCrossGroupFeedRoot.react,comet.groups.feed,tap_tabbar,1702608390446,78408,2361831622,,"
                                    },
                                    "tracking": [None],
                                    "event_share_metadata": {"surface": "newsfeed"},
                                    "audience": {"to_id": f"{IDGrup}"},
                                    "actor_id": data["__user"],
                                    "client_mutation_id": "2",
                                },
                                "displayCommentsFeedbackContext": None,
                                "displayCommentsContextEnableComment": None,
                                "displayCommentsContextIsAdPreview": None,
                                "displayCommentsContextIsAggregatedShare": None,
                                "displayCommentsContextIsStorySet": None,
                                "feedLocation": "GROUP",
                                "feedbackSource": 0,
                                "focusCommentID": None,
                                "gridMediaWidth": None,
                                "groupID": None,
                                "scale": 1,
                                "privacySelectorRenderLocation": "COMET_STREAM",
                                "checkPhotosToReelsUpsellEligibility": False,
                                "renderLocation": "group",
                                "useDefaultActor": False,
                                "inviteShortLinkKey": None,
                                "isFeed": False,
                                "isFundraiser": False,
                                "isFunFactPost": False,
                                "isGroup": True,
                                "isEvent": False,
                                "isTimeline": False,
                                "isSocialLearning": False,
                                "isPageNewsFeed": False,
                                "isProfileReviews": False,
                                "isWorkSharedDraft": False,
                                "UFI2CommentsProvider_commentsKey": "CometGroupDiscussionRootSuccessQuery",
                                "hashtag": None,
                                "canUserManageOffers": False,
                                "__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider": False,
                                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False,
                                "__relay_internal__pv__IsWorkUserrelayprovider": False,
                                "__relay_internal__pv__IsMergQAPollsrelayprovider": False,
                                "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider": False,
                                "__relay_internal__pv__StoriesRingrelayprovider": False,
                            }
                            data.update(
                                {
                                    "fb_api_caller_class": "RelayModern",
                                    "fb_api_req_friendly_name": "ComposerStoryCreateMutation",
                                    "variables": json.dumps(Variable),
                                    "server_timestamps": True,
                                    "doc_id": "6833151356803352",
                                }
                            )
                            response = r.post(
                                "https://www.facebook.com/api/graphql",
                                data=data,
                                headers=headers_post(),
                            )
                            Time = strftime("%T")
                            if '"Postingan Anda menunggu persetujuan"' in response.text:
                                Console(width=60, style="bold white").print(
                                    panel(
                                        f"""[bold yellow]Status    : [white]Ditinjau\n[bold yellow]Nama Grup : [white]{NameGrup}\n[bold yellow]ID Grup   : [white]{IDGrup}\n[bold yellow]Privacy   : [white]{GrupStatus}\n[bold yellow]Time      : [white]{Time}"""
                                    )
                                )
                                self._________________Author_________________(Delay)
                            elif (
                                '"is_marked_as_spam_by_admin_assistant": true'
                                in response.text
                            ):
                                Console(width=60, style="bold white").print(
                                    panel(
                                        f"""[bold yellow]Status    : [white]Sedang Ditinjau (Berpotensi Spam)\n[bold yellow]Nama Grup : [white]{NameGrup}\n[bold yellow]ID Grup   : [white]{IDGrup}\n[bold yellow]Privacy   : [white]{GrupStatus}\n[bold yellow]Time      : [white]{Time}"""
                                    )
                                )
                                self._________________Author_________________(Delay)
                            else:
                                BsResponse = response.text
                                PostUrl = re.findall(
                                    '"scheduled_publish_time":0,"url":"(.*?)"',
                                    BsResponse,
                                )[0].replace("\\", "")
                                Console(width=60, style="bold white").print(
                                    panel(
                                        f"""[bold green]Status    : [white]Success\n[bold green]Nama Grup : [white]{NameGrup}\n[bold green]ID Grup   : [white]{IDGrup}\n[bold green]Privacy   : [white]{GrupStatus}\n[bold green]Url Post  : [white]{PostUrl}\n[bold green]Time      : [white]{Time}"""
                                    )
                                )
                                self._________________Author_________________(Delay)
                        except Exception as e:
                            Console(style="bold white").print(
                                f"   └─> [bold red]Error:[white]{IDGrup}", end="\r"
                            )
                            sleep(2)
        except (NameError, Exception):
            exit("Stop Recode Bg...!!!")

    def Selesai(self):
        Console(width=60).print(
            panel(
                "[bold green]Selesai",
                width=60,
                style="bold white",
                title="[bold yellow]>[bold green]>[bold cyan]> [bold white]Selesai [bold cyan]<[bold green]<[bold yellow]<",
            ),
            justify="center",
        )
        exit()


if __name__ in ("__main__"):
    try:
        os.system("git pull")
    except:
        pass
    try:
        os.mkdir("Data")
    except:
        pass
    try:
        Terminal_Size()
        ________________________Menu________________________()
    except Exception as e:
        print(e)
