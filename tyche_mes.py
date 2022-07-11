from collections import OrderedDict

def USERMES(username,bio,WalletInfo,email):
    return f'🌅 Name:{username}\n\n\n📜Description:{bio}\ncategory:{WalletInfo}\n{email}\n '

def COLLEC(name,desc,blck):
    return f'🌅 Name:{name}\n\n\n📜Description:{desc}\ncategory:{blck}\n\n '

def NFTMES(name,desc,blck,price):
    # return 'sss'
    return f'🌅 Name:{name}\n\n\n📜Description:{desc}\n💈BlockChain:{blck}\n💰Price:{price}eth\n '

def MUST_SIGNUP(name):
    return f' سلام {name} عزیز❤    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام کن'



def HELP(name):
    return f' سلام {name}  خوش امدید  عزیز❤    \n\n به ربات  🎖️tyche NFT🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 tyche.ludushub.io \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبت نام کن'


def CONNECTSITE(name):
    return 'راهنمای اتصال'

def COMMANDS(name,id):
    # return   "<a href='/price'>Jordan B. Peterson</a>"
    return   "<a href='https://twitter.com/jordanbpeterson'>Jordan B. Peterson</a>\n /price \n قیمت ها" + f"""<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id={id}">هرپیامی این یارو بهت داد بدون زر زده</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>"""



def WELLCOME(name):
    return f' سلام {name}  خوش امدید  عزیز❤    \n\n به ربات  🎖️tyche NFT🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 tyche.ludushub.io \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبت نام کن'

# def NEWS(name):
#     return f' سلام {name}  خوش خبرنامهههههههههههه  عزیز❤    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام کن'



# def CURRENCYNEWS(name):
#     return name
    
# def NEWSDAY(news):
#     return f"fstring{news['a']}"

# def MYNEWS(news):
#     return f"fstring{news['a']}"

# def CURRENCYNEWS(news):
# return f"fstring{news['a']}"





# def MONITORMENU(name):
# return f'کدوم تایم فریمیی؟{name}'

def MONITOR(name):
    return f'{name}'

# def CURRENCYMONITOR(name):
#     return f' سلام {name}  مانیتورررررررررر  عزیز❤    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام کن'

def CURRENCYINFO(name,per_name,symbol,daily_change,price,marketcap,high_24h,low_24h,close_24h,time):
    return f""" symbol :{symbol}\n
                price :{price}\n
                market_cap :{marketcap}\n
                name :{name}\n
                time :{time}\n
                high_24h:{high_24h}\n
                low_24h:{low_24h}\n
                close_24h{close_24h}\n
                daily_change:{daily_change}\n
                per_name{per_name}\n
                
                """


# def CHANGE(name,tf,volume,volume_change,price_change,price_change_pct):
#     return f'{name}{tf}\n\n\nvolume:{volume}volume_change:{volume_change}price_change:{price_change}price_change_pct:{price_change_pct}'

def BACK(name):
    return f' سلام {name}  LK  چی میخایییییییییی    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام کن'

# def SETTING(name):
#     return f' سلام {name}  LK  چی تنظیماتت     \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام کن'

def CONTACTUS(name):
    return f' سلام {name}  LK  چی ارتباط باما    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام کن'

# def SETBASECURRENCY(name):
#     return f' سلام {name}  LK  چکدوم ارزپایه ر    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام کن'

# def SETEXCHANGE(name):
#     return f' سلام {name}  LK  چکدوم صرافی زیر ر    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام ک'




tokens=[
    OrderedDict(
        [
            ("name", "conflux-network"),
            ("symbol", "CFX"),
            ("persian_name", "Conflux Network"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/conflux-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "maker"),
            ("symbol", "MKR"),
            ("persian_name", "میکر"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/maker.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "theta"),
            ("symbol", "THETA"),
            ("persian_name", "تتا"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/theta-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bitcoin-cash-abc"),
            ("symbol", "BCHA"),
            ("persian_name", "Bitcoin Cash ABC"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin-cash-abc-2.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "orchid"),
            ("symbol", "OXT"),
            ("persian_name", "اورکید"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/orchid.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "grin"),
            ("symbol", "GRIN"),
            ("persian_name", "گرین"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/grin.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "waves-enterprise"),
            ("symbol", "WEST"),
            ("persian_name", "Waves Enterprise"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/waves-enterprise.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "super-zero-protocol"),
            ("symbol", "SERO"),
            ("persian_name", "Super Zero Protocol"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/super-zero-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "blockstack"),
            ("symbol", "STX"),
            ("persian_name", "بلاک استک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/blockstack.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "power-ledger"),
            ("symbol", "POWR"),
            ("persian_name", "پاور لجر"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/power-ledger.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "marlin"),
            ("symbol", "POND"),
            ("persian_name", "Marlin"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/marlin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "wings"),
            ("symbol", "WINGS"),
            ("persian_name", "وینگز"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/wings.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "aeternity"),
            ("symbol", "AE"),
            ("persian_name", "ایترنیتی"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/aeternity.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "darwinia-network"),
            ("symbol", "RING"),
            ("persian_name", "Darwinia Network"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/darwinia-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "emercoin"),
            ("symbol", "EMC"),
            ("persian_name", "Emercoin"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/emercoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "pigeoncoin"),
            ("symbol", "PGN"),
            ("persian_name", "Pigeoncoin"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/pigeoncoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "investfeed"),
            ("symbol", "IFT"),
            ("persian_name", "InvestFeed"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/investfeed.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "filecoin"),
            ("symbol", "FIL"),
            ("persian_name", "فایل کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/filecoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "loom-network"),
            ("symbol", "LOOM"),
            ("persian_name", "لوم نتورک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/loom-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "oneledger"),
            ("symbol", "OLT"),
            ("persian_name", "OneLedger"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/oneledger.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "iost"),
            ("symbol", "IOST"),
            ("persian_name", "آی او اس تی"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/iostoken.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "kun"),
            ("symbol", "KUN"),
            ("persian_name", "KUN"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/kun.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "zcash"),
            ("symbol", "ZEC"),
            ("persian_name", "زی کش"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/zcash.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "solana"),
            ("symbol", "SOL"),
            ("persian_name", "سولانا"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/solana.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "yusra"),
            ("symbol", "YUSRA"),
            ("persian_name", "YUSRA"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/yusra.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "namecoin"),
            ("symbol", "NMC"),
            ("persian_name", "نیم کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/namecoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "beam"),
            ("symbol", "BEAM"),
            ("persian_name", "بیم"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/beam.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "the-graph"),
            ("symbol", "GRT"),
            ("persian_name", "The Graph"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/the-graph.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "siacoin"),
            ("symbol", "SC"),
            ("persian_name", "سیا کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/siacoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "wax"),
            ("symbol", "WAXP"),
            ("persian_name", "وکس"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/wax.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bytom"),
            ("symbol", "BTM"),
            ("persian_name", "بایتوم"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/bytom.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "zilliqa"),
            ("symbol", "ZIL"),
            ("persian_name", "زیلیکا"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/zilliqa.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "swerve"),
            ("symbol", "SWRV"),
            ("persian_name", "Swerve"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/swerve.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "augur"),
            ("symbol", "REP"),
            ("persian_name", "آگر"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/augur.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "harmony"),
            ("symbol", "ONE"),
            ("persian_name", "هارمونی"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/harmony.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "basic-attention-token"),
            ("symbol", "BAT"),
            ("persian_name", "بت"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/basic-attention-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bytecoin"),
            ("symbol", "BCN"),
            ("persian_name", "بایت کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bytecoin-bcn.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "elrond-egld"),
            ("symbol", "EGLD"),
            ("persian_name", "الروند"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/elrond-egld.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "avalanche"),
            ("symbol", "AVAX"),
            ("persian_name", "اولنچ"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/avalanche.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "okb"),
            ("symbol", "OKB"),
            ("persian_name", "اوکی بی"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/okb.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "dxdao"),
            ("symbol", "DXD"),
            ("persian_name", "DXdao"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/dxdao.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "crypto.com-coin"),
            ("symbol", "CRO"),
            ("persian_name", "کریپتو"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/crypto-com-coin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bitcoin-cash"),
            ("symbol", "BCH"),
            ("persian_name", "بیت کوین کش"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin-cash.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bittorrent"),
            ("symbol", "BTT"),
            ("persian_name", "بیت تورنت"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bittorrent.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "irisnet"),
            ("symbol", "IRIS"),
            ("persian_name", "IRISnet"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/irisnet.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "v.systems"),
            ("symbol", "VSYS"),
            ("persian_name", "وی سیستمز"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/v-systems.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "storj"),
            ("symbol", "STORJ"),
            ("persian_name", "استورج"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/storj.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "diamond"),
            ("symbol", "DMD"),
            ("persian_name", "Diamond"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/diamond.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "polkastarter"),
            ("symbol", "POLS"),
            ("persian_name", "Polkastarter"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/polkastarter.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "turtlecoin"),
            ("symbol", "TRTL"),
            ("persian_name", "TurtleCoin"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/turtlecoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "cybermiles"),
            ("symbol", "CMT"),
            ("persian_name", "سایبر مایلز"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/cybermiles.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "melon"),
            ("symbol", "MLN"),
            ("persian_name", "ملون"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/melon.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "oneswap-dao-token"),
            ("symbol", "ONES"),
            ("persian_name", "OneSwap DAO Token"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/oneswap-dao-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "xaya"),
            ("symbol", "CHI"),
            ("persian_name", "Xaya"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/xaya.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "sumokoin"),
            ("symbol", "SUMO"),
            ("persian_name", "Sumokoin"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/sumokoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "pivx"),
            ("symbol", "PIVX"),
            ("persian_name", "پیو اکس"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/pivx.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "hypercash"),
            ("symbol", "HC"),
            ("persian_name", "هایپر کش"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/hypercash.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "nem"),
            ("symbol", "XEM"),
            ("persian_name", "نم"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/nem.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "cover-protocol"),
            ("symbol", "COVER"),
            ("persian_name", "کاور پروتکل"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/cover-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "lition"),
            ("symbol", "LIT"),
            ("persian_name", "Lition"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/lition.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "cosmos"),
            ("symbol", "ATOM"),
            ("persian_name", "کازماس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/cosmos.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "uniswap"),
            ("symbol", "UNI"),
            ("persian_name", "یونی سواپ"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/uniswap.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "hedera-hashgraph"),
            ("symbol", "HBAR"),
            ("persian_name", "هدرا هش\u200cگراف"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/hedera-hashgraph.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bitkan"),
            ("symbol", "KAN"),
            ("persian_name", "بیت کن"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitkan.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "paxos-standard"),
            ("symbol", "PAX"),
            ("persian_name", "پکسوس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/paxos-standard.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "dero"),
            ("symbol", "DERO"),
            ("persian_name", "Dero"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/dero.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "freecash"),
            ("symbol", "FCH"),
            ("persian_name", "Freecash"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/freecash.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "kleros"),
            ("symbol", "PNK"),
            ("persian_name", "کلروس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/kleros.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "jarvis-network"),
            ("symbol", "JRT"),
            ("persian_name", "Jarvis Network"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/jarvis-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "cream-finance"),
            ("symbol", "CREAM"),
            ("persian_name", "Cream Finance"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/cream-finance.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "shiba-inu"),
            ("symbol", "SHIB"),
            ("persian_name", "شیبا اینو"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/shiba-inu.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "pancakeswap"),
            ("symbol", "CAKE"),
            ("persian_name", "پنکیک سواپ"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/pancakeswap.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "verge"),
            ("symbol", "XVG"),
            ("persian_name", "ورج"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/verge.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "hydro"),
            ("symbol", "HYDRO"),
            ("persian_name", "هایدرو"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/hydro.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "dia"),
            ("symbol", "DIA"),
            ("persian_name", "دیا"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/dia.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "decred"),
            ("symbol", "DCR"),
            ("persian_name", "دیکرد"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/decred.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "perpetual-protocol"),
            ("symbol", "PERP"),
            ("persian_name", "Perpetual Protocol"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/perpetual-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "new-bitshares"),
            ("symbol", "NBS"),
            ("persian_name", "New BitShares"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/new-bitshares.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "anoncoin"),
            ("symbol", "ANC"),
            ("persian_name", "Anoncoin"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/anoncoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "alpha-finance-lab"),
            ("symbol", "ALPHA"),
            ("persian_name", "آلفا فایننس لب"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/alpha-finance-lab.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "haven-protocol"),
            ("symbol", "XHV"),
            ("persian_name", "Haven Protocol"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/haven-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "dash"),
            ("symbol", "DASH"),
            ("persian_name", "دش"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/dash.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "aragon"),
            ("symbol", "ANT"),
            ("persian_name", "آراگون"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/aragon.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "hegic"),
            ("symbol", "HEGIC"),
            ("persian_name", "Hegic"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/hegic.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "daostack"),
            ("symbol", "GEN"),
            ("persian_name", "DAOstack"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/daostack.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ontology-gas"),
            ("symbol", "ONG"),
            ("persian_name", "Ontology Gas"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/ontology-gas.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "curve-dao-token"),
            ("symbol", "CRV"),
            ("persian_name", "کرو دائو توکن"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/curve-dao-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "energi"),
            ("symbol", "NRG"),
            ("persian_name", "انرژی"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/energi.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "badger-dao"),
            ("symbol", "BADGER"),
            ("persian_name", "Badger DAO"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/badger-dao.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "zero"),
            ("symbol", "ZER"),
            ("persian_name", "Zero"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/zero.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bella-protocol"),
            ("symbol", "BEL"),
            ("persian_name", "بلا پروتکل"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bella-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "airswap"),
            ("symbol", "AST"),
            ("persian_name", "ایر سوپ"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/airswap.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "sun"),
            ("symbol", "SUN"),
            ("persian_name", "سان"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/sun.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bitshares"),
            ("symbol", "BTS"),
            ("persian_name", "بیت شیرز"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitshares.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "actinium"),
            ("symbol", "ACM"),
            ("persian_name", "Actinium"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/actinium.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "enjin-coin"),
            ("symbol", "ENJ"),
            ("persian_name", "انجین کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/enjin-coin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "gas"),
            ("symbol", "GAS"),
            ("persian_name", "گس"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/gas.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "komodo"),
            ("symbol", "KMD"),
            ("persian_name", "کومودو"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/komodo.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bluzelle"),
            ("symbol", "BLZ"),
            ("persian_name", "Bluzelle"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bluzelle.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "xdag"),
            ("symbol", "XDAG"),
            ("persian_name", "XDAG"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/xdag.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "holo"),
            ("symbol", "HOT"),
            ("persian_name", "هولو"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/holo.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "phoenixdao"),
            ("symbol", "PHNX"),
            ("persian_name", "PhoenixDAO"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/phoenixdao.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "nkn"),
            ("symbol", "NKN"),
            ("persian_name", "NKN"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/nkn.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "trueusd"),
            ("symbol", "TUSD"),
            ("persian_name", "TrueUSD"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/trueusd.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "cube"),
            ("symbol", "AUTO"),
            ("persian_name", "کیوب"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/cube.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ultiledger"),
            ("symbol", "ULT"),
            ("persian_name", "Ultiledger"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/ultiledger.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bkex-token"),
            ("symbol", "BKK"),
            ("persian_name", "BKEX Token"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bkex-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "handshake-"),
            ("symbol", "HNS"),
            ("persian_name", "هندشیک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/handshake.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "venus"),
            ("symbol", "XVS"),
            ("persian_name", "ونوس"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/venus.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "presearch"),
            ("symbol", "PRE"),
            ("persian_name", "Presearch"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/presearch.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "tokenlon-network-token"),
            ("symbol", "LON"),
            ("persian_name", "Tokenlon Network Token"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/tokenlon-network-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "luna-coin"),
            ("symbol", "LUNA"),
            ("persian_name", "Luna Coin"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/luna-coin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ocean-protocol"),
            ("symbol", "OCEAN"),
            ("persian_name", "اوشن پروتکل"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/ocean-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "algorand"),
            ("symbol", "ALGO"),
            ("persian_name", "الگورند"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/algorand.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "aavegotchi"),
            ("symbol", "GHST"),
            ("persian_name", "Aavegotchi"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/aavegotchi.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "powerpool"),
            ("symbol", "CVP"),
            ("persian_name", "PowerPool"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/powerpool.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "lambda"),
            ("symbol", "LAMB"),
            ("persian_name", "Lambda"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/lambda.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "banano"),
            ("symbol", "BAN"),
            ("persian_name", "Banano"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/banano.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "1inch"),
            ("symbol", "1INCH"),
            ("persian_name", "۱inch"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/1inch.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "keep3rv1"),
            ("symbol", "KP3R"),
            ("persian_name", "Keep3rV1"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/keep3rv1.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "kusama"),
            ("symbol", "KSM"),
            ("persian_name", "کوزاما"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/kusama.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "xdai"),
            ("symbol", "STAKE"),
            ("persian_name", "اکس دای"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/xdai.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "cortex"),
            ("symbol", "CTXC"),
            ("persian_name", "کورتکس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/cortex.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "rarible"),
            ("symbol", "RARI"),
            ("persian_name", "Rarible"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/rarible.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "elastos"),
            ("symbol", "ELA"),
            ("persian_name", "الاستوس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/elastos.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "finnexus"),
            ("symbol", "FNX"),
            ("persian_name", "FinNexus"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/finnexus.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "revv"),
            ("symbol", "REVV"),
            ("persian_name", "REVV"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/revv.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "secret"),
            ("symbol", "SCRT"),
            ("persian_name", "سکرت"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/secret.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "mirror-protocol"),
            ("symbol", "MIR"),
            ("persian_name", "Mirror Protocol"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/mirror-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "darwinia-commitment-token"),
            ("symbol", "KTON"),
            ("persian_name", "Darwinia Commitment Token"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/darwinia-commitment-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "polkadot"),
            ("symbol", "DOT"),
            ("persian_name", "پولکادات"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/polkadot-new.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "sushiswap"),
            ("symbol", "SUSHI"),
            ("persian_name", "سوشی سواپ"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/sushiswap.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "swipe"),
            ("symbol", "SXP"),
            ("persian_name", "سوایپ"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/swipe.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "status"),
            ("symbol", "SNT"),
            ("persian_name", "استاتوس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/status.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bancor"),
            ("symbol", "BNT"),
            ("persian_name", "بنکور"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bancor.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "tether"),
            ("symbol", "USDT"),
            ("persian_name", "تتر"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
            ),
            ("exponent", 2),
        ]
    ),
    OrderedDict(
        [
            ("name", "vechain"),
            ("symbol", "VET"),
            ("persian_name", "وی چین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/vechain.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ergo"),
            ("symbol", "ERG"),
            ("persian_name", "Ergo"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/ergo.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "dodo"),
            ("symbol", "DODO"),
            ("persian_name", "DODO"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/dodo.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bitcoin"),
            ("symbol", "BTC"),
            ("persian_name", "بیت کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin.png",
            ),
            ("exponent", 6),
        ]
    ),
    OrderedDict(
        [
            ("name", "usd-coin"),
            ("symbol", "USDC"),
            ("persian_name", "یو اس دی کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/usd-coin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "dogecoin"),
            ("symbol", "DOGE"),
            ("persian_name", "دوج کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/dogecoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ethereum-classic"),
            ("symbol", "ETC"),
            ("persian_name", "اتریوم کلاسیک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/ethereum-classic.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "synthetix"),
            ("symbol", "SNX"),
            ("persian_name", "سینتتیکس نتوورک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/synthetix-network-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "arweave"),
            ("symbol", "AR"),
            ("persian_name", "Arweave"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/arweave.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "chiliz"),
            ("symbol", "CHZ"),
            ("persian_name", "چیلیز"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/chiliz.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "loopring"),
            ("symbol", "LRC"),
            ("persian_name", "لوپرینگ"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/loopring.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "compound"),
            ("symbol", "COMP"),
            ("persian_name", "کامپاند"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/compound.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "near-protocol"),
            ("symbol", "NEAR"),
            ("persian_name", "نیر پروتکل"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/near-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "decentraland"),
            ("symbol", "MANA"),
            ("persian_name", "دسنترالند"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/decentraland.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "pirate-chain"),
            ("symbol", "ARRR"),
            ("persian_name", "Pirate Chain"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/pirate-chain.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "aave"),
            ("symbol", "AAVE"),
            ("persian_name", "آوی"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/aave.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "helium"),
            ("symbol", "HNT"),
            ("persian_name", "هلیوم"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/helium.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "gala"),
            ("symbol", "GALA"),
            ("persian_name", "گالا"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/gala.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "monero"),
            ("symbol", "XMR"),
            ("persian_name", "مونرو"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/monero.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", ""),
            ("symbol", "AXS"),
            ("persian_name", "اکسی اینفینیتی"),
            ("logo", "axie-infinity"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "bitcoin-sv"),
            ("symbol", "BSV"),
            ("persian_name", "ساتوشی ویژن"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin-sv.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "qtum"),
            ("symbol", "QTUM"),
            ("persian_name", "کوانتوم"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/qtum.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "huobi-token"),
            ("symbol", "HT"),
            ("persian_name", "هیوبی توکن"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/huobi-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "xrp"),
            ("symbol", "XRP"),
            ("persian_name", "ریپل"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/xrp.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "binance-coin"),
            ("symbol", "BNB"),
            ("persian_name", "بایننس کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/binance-coin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "waves"),
            ("symbol", "WAVES"),
            ("persian_name", "ویوز"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/waves.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "stellar"),
            ("symbol", "XLM"),
            ("persian_name", "استلار"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/stellar.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "kava"),
            ("symbol", "KAVA"),
            ("persian_name", "کاوا"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/kava.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "chainlink"),
            ("symbol", "LINK"),
            ("persian_name", "چین لینک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/chainlink.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "litecoin"),
            ("symbol", "LTC"),
            ("persian_name", "لایت کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/litecoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "gnosis"),
            ("symbol", "GNO"),
            ("persian_name", "جنوسیس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/gnosis-gno.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "serum"),
            ("symbol", "SRM"),
            ("persian_name", "سروم"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/serum.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "kadena"),
            ("symbol", "KDA"),
            ("persian_name", "Kadena"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/kadena.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ravencoin"),
            ("symbol", "RVN"),
            ("persian_name", "ریون کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/ravencoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "origin-protocol"),
            ("symbol", "OGN"),
            ("persian_name", "اوریجین پروتکل"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/origin-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "just"),
            ("symbol", "JST"),
            ("persian_name", "جاست"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/just.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "0x"),
            ("symbol", "ZRX"),
            ("persian_name", "زیرو ایکس"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/0x.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "audius"),
            ("symbol", "AUDIO"),
            ("persian_name", "Audius"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/audius.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "icon"),
            ("symbol", "ICX"),
            ("persian_name", "آیکون"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/icon.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "neo"),
            ("symbol", "NEO"),
            ("persian_name", "نئو"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/neo.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "livepeer"),
            ("symbol", "LPT"),
            ("persian_name", "لایو پیر"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/livepeer.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ontology"),
            ("symbol", "ONT"),
            ("persian_name", "آنتولوژی"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/ontology.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "api3"),
            ("symbol", "API3"),
            ("persian_name", "API3"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/api3.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "fantom"),
            ("symbol", "FTM"),
            ("persian_name", "فانتوم"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/fantom.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "kyber-network"),
            ("symbol", "KNC"),
            ("persian_name", "کایبر نتورک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/kyber-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "reserve-rights"),
            ("symbol", "RSR"),
            ("persian_name", "رزرو رایتس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/reserve-rights.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "sandbox"),
            ("symbol", "SAND"),
            ("persian_name", "سندباکس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/the-sandbox.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "toman"),
            ("symbol", "TOMAN"),
            ("persian_name", "تومان"),
            ("logo", "http://s6.picofile.com/file/8376555818/IRR.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "yearn.finance"),
            ("symbol", "YFI"),
            ("persian_name", "یرن فایننس"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/yearn-finance.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "wootrade"),
            ("symbol", "WOO"),
            ("persian_name", "Wootrade"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/wootrade.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "injective-protocol"),
            ("symbol", "INJ"),
            ("persian_name", "اینجکتیو پروتکل"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/injective-protocol.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "horizen"),
            ("symbol", "ZEN"),
            ("persian_name", "هورایزن"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/horizen.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "uma"),
            ("symbol", "UMA"),
            ("persian_name", "اوما"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/uma.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "skale-network"),
            ("symbol", "SKL"),
            ("persian_name", "SKALE Network"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/skale-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "balancer"),
            ("symbol", "BAL"),
            ("persian_name", "بالانسر"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/balancer.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "lisk"),
            ("symbol", "LSK"),
            ("persian_name", "لیسک"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/lisk.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "digibyte"),
            ("symbol", "DGB"),
            ("persian_name", "دیجی بایت"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/digibyte.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "render-token"),
            ("symbol", "RNDR"),
            ("persian_name", "Render Token"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/render-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "nervos-network"),
            ("symbol", "CKB"),
            ("persian_name", "نروس نتورک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/nervos-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "vethor-token"),
            ("symbol", "VTHO"),
            ("persian_name", "VeThor Token"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/vethor-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "numeraire"),
            ("symbol", "NMR"),
            ("persian_name", "Numeraire"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/numeraire.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ardor"),
            ("symbol", "ARDR"),
            ("persian_name", "آردور"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/ardor.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "syscoin"),
            ("symbol", "SYS"),
            ("persian_name", "سیس کوین"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/syscoin.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "tron"),
            ("symbol", "TRX"),
            ("persian_name", "ترون"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/tron.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "tezos"),
            ("symbol", "XTZ"),
            ("persian_name", "تزوس"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/tezos.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ftx-token"),
            ("symbol", "FTT"),
            ("persian_name", "اف\u200cتی\u200cایکس توکن"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/ftx-token.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "cardano"),
            ("symbol", "ADA"),
            ("persian_name", "کاردانو"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/cardano.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "matic-network"),
            ("symbol", "MATIC"),
            ("persian_name", "ماتیک نتورک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/matic-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ren"),
            ("symbol", "REN"),
            ("persian_name", "رِن"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/ren.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "keep-network"),
            ("symbol", "KEEP"),
            ("persian_name", "کیپ نتورک"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/keep-network.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "nano"),
            ("symbol", "NANO"),
            ("persian_name", "نانو"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/nano.png"),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "chromia"),
            ("symbol", "CHR"),
            ("persian_name", "کرومیا"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/chromia.png",
            ),
            ("exponent", 4),
        ]
    ),
    OrderedDict(
        [
            ("name", "ethereum"),
            ("symbol", "ETH"),
            ("persian_name", "اتریوم"),
            (
                "logo",
                "https://cdn.arzdigital.com/uploads/assets/coins/icons/ethereum.png",
            ),
            ("exponent", 3),
        ]
    ),
    OrderedDict(
        [
            ("name", "eos"),
            ("symbol", "EOS"),
            ("persian_name", "ایاس"),
            ("logo", "https://cdn.arzdigital.com/uploads/assets/coins/icons/eos.png"),
            ("exponent", 4),
]
)
]



markets=[
        {
            "name": "1INCHUSDT",
            "base_currency": {
                "name": "1inch",
                "symbol": "1INCH",
                "persian_name": "۱inch",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/1inch.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "MKRUSDT",
            "base_currency": {
                "name": "maker",
                "symbol": "MKR",
                "persian_name": "میکر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/maker.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "KSMUSDT",
            "base_currency": {
                "name": "kusama",
                "symbol": "KSM",
                "persian_name": "کوزاما",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/kusama.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "BTCUSDC",
            "base_currency": {
                "name": "bitcoin",
                "symbol": "BTC",
                "persian_name": "بیت کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin.png",
                "exponent": 6
            },
            "quote_currency": {
                "name": "usd-coin",
                "symbol": "USDC",
                "persian_name": "یو اس دی کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/usd-coin.png",
                "exponent": 4
            }
        },
        {
            "name": "XTZUSDT",
            "base_currency": {
                "name": "tezos",
                "symbol": "XTZ",
                "persian_name": "تزوس",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tezos.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "LINKUSDT",
            "base_currency": {
                "name": "chainlink",
                "symbol": "LINK",
                "persian_name": "چین لینک",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/chainlink.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ETHBTC",
            "base_currency": {
                "name": "ethereum",
                "symbol": "ETH",
                "persian_name": "اتریوم",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/ethereum.png",
                "exponent": 3
            },
            "quote_currency": {
                "name": "bitcoin",
                "symbol": "BTC",
                "persian_name": "بیت کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin.png",
                "exponent": 6
            }
        },
        {
            "name": "DOTUSDT",
            "base_currency": {
                "name": "polkadot",
                "symbol": "DOT",
                "persian_name": "پولکادات",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/polkadot-new.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "DASHUSDT",
            "base_currency": {
                "name": "dash",
                "symbol": "DASH",
                "persian_name": "دش",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/dash.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "LTCUSDT",
            "base_currency": {
                "name": "litecoin",
                "symbol": "LTC",
                "persian_name": "لایت کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/litecoin.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "HOTUSDT",
            "base_currency": {
                "name": "holo",
                "symbol": "HOT",
                "persian_name": "هولو",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/holo.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "BNBBTC",
            "base_currency": {
                "name": "binance-coin",
                "symbol": "BNB",
                "persian_name": "بایننس کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/binance-coin.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "bitcoin",
                "symbol": "BTC",
                "persian_name": "بیت کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin.png",
                "exponent": 6
            }
        },
        {
            "name": "ADABTC",
            "base_currency": {
                "name": "cardano",
                "symbol": "ADA",
                "persian_name": "کاردانو",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/cardano.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "bitcoin",
                "symbol": "BTC",
                "persian_name": "بیت کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin.png",
                "exponent": 6
            }
        },
        {
            "name": "BATUSDT",
            "base_currency": {
                "name": "basic-attention-token",
                "symbol": "BAT",
                "persian_name": "بت",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/basic-attention-token.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ALGOUSDT",
            "base_currency": {
                "name": "algorand",
                "symbol": "ALGO",
                "persian_name": "الگورند",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/algorand.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "BTCUSDT",
            "base_currency": {
                "name": "bitcoin",
                "symbol": "BTC",
                "persian_name": "بیت کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin.png",
                "exponent": 6
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ZECUSDT",
            "base_currency": {
                "name": "zcash",
                "symbol": "ZEC",
                "persian_name": "زی کش",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/zcash.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "NEARUSDT",
            "base_currency": {
                "name": "near-protocol",
                "symbol": "NEAR",
                "persian_name": "نیر پروتکل",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/near-protocol.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ADAUSDT",
            "base_currency": {
                "name": "cardano",
                "symbol": "ADA",
                "persian_name": "کاردانو",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/cardano.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "NEOUSDT",
            "base_currency": {
                "name": "neo",
                "symbol": "NEO",
                "persian_name": "نئو",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/neo.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "AAVEUSDT",
            "base_currency": {
                "name": "aave",
                "symbol": "AAVE",
                "persian_name": "آوی",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/aave.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "FTMUSDT",
            "base_currency": {
                "name": "fantom",
                "symbol": "FTM",
                "persian_name": "فانتوم",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/fantom.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "MATICUSDT",
            "base_currency": {
                "name": "matic-network",
                "symbol": "MATIC",
                "persian_name": "ماتیک نتورک",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/matic-network.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "FILUSDT",
            "base_currency": {
                "name": "filecoin",
                "symbol": "FIL",
                "persian_name": "فایل کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/filecoin.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "WAVESUSDT",
            "base_currency": {
                "name": "waves",
                "symbol": "WAVES",
                "persian_name": "ویوز",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/waves.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "TRXUSDT",
            "base_currency": {
                "name": "tron",
                "symbol": "TRX",
                "persian_name": "ترون",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tron.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "FTTUSDT",
            "base_currency": {
                "name": "ftx-token",
                "symbol": "FTT",
                "persian_name": "اف‌تی‌ایکس توکن",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/ftx-token.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "QTUMUSDT",
            "base_currency": {
                "name": "qtum",
                "symbol": "QTUM",
                "persian_name": "کوانتوم",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/qtum.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ETCUSDT",
            "base_currency": {
                "name": "ethereum-classic",
                "symbol": "ETC",
                "persian_name": "اتریوم کلاسیک",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/ethereum-classic.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ENJUSDT",
            "base_currency": {
                "name": "enjin-coin",
                "symbol": "ENJ",
                "persian_name": "انجین کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/enjin-coin.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ZILUSDT",
            "base_currency": {
                "name": "zilliqa",
                "symbol": "ZIL",
                "persian_name": "زیلیکا",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/zilliqa.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "MANAUSDT",
            "base_currency": {
                "name": "decentraland",
                "symbol": "MANA",
                "persian_name": "دسنترالند",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/decentraland.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "VETUSDT",
            "base_currency": {
                "name": "vechain",
                "symbol": "VET",
                "persian_name": "وی چین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/vechain.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "SOLBTC",
            "base_currency": {
                "name": "solana",
                "symbol": "SOL",
                "persian_name": "سولانا",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/solana.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "bitcoin",
                "symbol": "BTC",
                "persian_name": "بیت کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin.png",
                "exponent": 6
            }
        },
        {
            "name": "CRVUSDT",
            "base_currency": {
                "name": "curve-dao-token",
                "symbol": "CRV",
                "persian_name": "کرو دائو توکن",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/curve-dao-token.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "XRPBTC",
            "base_currency": {
                "name": "xrp",
                "symbol": "XRP",
                "persian_name": "ریپل",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/xrp.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "bitcoin",
                "symbol": "BTC",
                "persian_name": "بیت کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/bitcoin.png",
                "exponent": 6
            }
        },
        {
            "name": "AVAXUSDT",
            "base_currency": {
                "name": "avalanche",
                "symbol": "AVAX",
                "persian_name": "اولنچ",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/avalanche.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "XLMUSDT",
            "base_currency": {
                "name": "stellar",
                "symbol": "XLM",
                "persian_name": "استلار",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/stellar.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ATOMUSDT",
            "base_currency": {
                "name": "cosmos",
                "symbol": "ATOM",
                "persian_name": "کازماس",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/cosmos.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "SOLUSDT",
            "base_currency": {
                "name": "solana",
                "symbol": "SOL",
                "persian_name": "سولانا",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/solana.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ETHUSDT",
            "base_currency": {
                "name": "ethereum",
                "symbol": "ETH",
                "persian_name": "اتریوم",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/ethereum.png",
                "exponent": 3
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "BNBUSDT",
            "base_currency": {
                "name": "binance-coin",
                "symbol": "BNB",
                "persian_name": "بایننس کوین",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/binance-coin.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "UNIUSDT",
            "base_currency": {
                "name": "uniswap",
                "symbol": "UNI",
                "persian_name": "یونی سواپ",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/uniswap.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "EOSUSDT",
            "base_currency": {
                "name": "eos",
                "symbol": "EOS",
                "persian_name": "ایاس",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/eos.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "XMRUSDT",
            "base_currency": {
                "name": "monero",
                "symbol": "XMR",
                "persian_name": "مونرو",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/monero.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "XRPUSDT",
            "base_currency": {
                "name": "xrp",
                "symbol": "XRP",
                "persian_name": "ریپل",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/xrp.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "XEMUSDT",
            "base_currency": {
                "name": "nem",
                "symbol": "XEM",
                "persian_name": "نم",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/nem.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "SHIBUSDT",
            "base_currency": {
                "name": "shiba-inu",
                "symbol": "SHIB",
                "persian_name": "شیبا اینو",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/shiba-inu.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "HNTUSDT",
            "base_currency": {
                "name": "helium",
                "symbol": "HNT",
                "persian_name": "هلیوم",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/helium.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "THETAUSDT",
            "base_currency": {
                "name": "theta",
                "symbol": "THETA",
                "persian_name": "تتا",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/theta-network.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "EGLDUSDT",
            "base_currency": {
                "name": "elrond-egld",
                "symbol": "EGLD",
                "persian_name": "الروند",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/elrond-egld.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "SANDUSDT",
            "base_currency": {
                "name": "sandbox",
                "symbol": "SAND",
                "persian_name": "سندباکس",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/the-sandbox.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "AXSUSDT",
            "base_currency": {
                "name": "",
                "symbol": "AXS",
                "persian_name": "اکسی اینفینیتی",
                "logo": "axie-infinity",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "CAKEUSDT",
            "base_currency": {
                "name": "pancakeswap",
                "symbol": "CAKE",
                "persian_name": "پنکیک سواپ",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/pancakeswap.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "GALAUSDT",
            "base_currency": {
                "name": "gala",
                "symbol": "GALA",
                "persian_name": "گالا",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/gala.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "KAVAUSDT",
            "base_currency": {
                "name": "kava",
                "symbol": "KAVA",
                "persian_name": "کاوا",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/kava.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        },
        {
            "name": "ONEUSDT",
            "base_currency": {
                "name": "harmony",
                "symbol": "ONE",
                "persian_name": "هارمونی",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/harmony.png",
                "exponent": 4
            },
            "quote_currency": {
                "name": "tether",
                "symbol": "USDT",
                "persian_name": "تتر",
                "logo": "https://cdn.arzdigital.com/uploads/assets/coins/icons/tether.png",
                "exponent": 2
            }
        }]

