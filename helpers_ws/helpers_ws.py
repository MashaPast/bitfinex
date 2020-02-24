from logger import appLogger
import websockets
import pytest

LIST_OF_ARGVALUES = [("ABSETH"), ("ABSUSD"), ("AGIBTC"), ("AGIETH"), ("AGIUSD"), ("AIDBTC"), ("AIDETH"), ("AIDUSD"), ("AIOBTC"), ("AIOETH"), ("AIOUSD"), ("ALGBTC"), ("ALGUSD"), ("ALGUST"), ("AMPBTC"), ("AMPUSD"), ("AMPUST"), ("ANTBTC"), ("ANTETH"), ("ANTUSD"), ("ASTETH"), ("ASTUSD"), ("ATMBTC"), ("ATMETH"), ("ATMUSD"), ("ATOBTC"), ("ATOETH"), ("ATOUSD"), ("AUCBTC"), ("AUCETH"), ("AUCUSD"), ("AVTBTC"), ("AVTETH"), ("AVTUSD"), ("BABBTC"), ("BABUSD"), ("BABUST"), ("BATBTC"), ("BATETH"), ("BATUSD"), ("BBNETH"), ("BBNUSD"), ("BCIBTC"), ("BCIUSD"), ("BFTBTC"), ("BFTETH"), ("BFTUSD"), ("BNTBTC"), ("BNTETH"), ("BNTUSD"), ("BOXETH"), ("BOXUSD"), ("BSVBTC"), ("BSVUSD"), ("BTC:CNHT"), ("BTCEUR"), ("BTCGBP"), ("BTCJPY"), ("BTCUSD"), ("BTCUST"), ("BTCXCH"), ("BTGBTC"), ("BTGUSD"), ("BTTBTC"), ("BTTUSD"), ("CBTBTC"), ("CBTETH"), ("CBTUSD"), ("CHZUSD"), ("CHZUST"), ("CLOBTC"), ("CLOUSD"), ("CNDBTC"), ("CNDETH"), ("CNDUSD"), ("CNH:CNHT"), ("CNNETH"), ("CNNUSD"), ("CSXETH"), ("CSXUSD"), ("CTXBTC"), ("CTXETH"), ("CTXUSD"), ("DADBTC"), ("DADETH"), ("DADUSD"), ("DAIBTC"), ("DAIETH"), ("DAIUSD"), ("DATBTC"), ("DATETH"), ("DATUSD"), ("DGBBTC"), ("DGBUSD"), ("DGXETH"), ("DGXUSD"), ("DRNETH"), ("DRNUSD"), ("DSHBTC"), ("DSHUSD"), ("DTABTC"), ("DTAETH"), ("DTAUSD"), ("DTHBTC"), ("DTHETH"), ("DTHUSD"), ("DTXUSD"), ("DTXUST"), ("DUSK:BTC"), ("DUSK:USD"), ("EDOBTC"), ("EDOETH"), ("EDOUSD"), ("ELFBTC"), ("ELFETH"), ("ELFUSD"), ("ENJETH"), ("ENJUSD"), ("EOSBTC"), ("EOSETH"), ("EOSEUR"), ("EOSGBP"), ("EOSJPY"), ("EOSUSD"), ("EOSUST"), ("ESSBTC"), ("ESSETH"), ("ESSUSD"), ("ETCBTC"), ("ETCUSD"), ("ETHBTC"), ("ETHEUR"), ("ETHGBP"), ("ETHJPY"), ("ETHUSD"), ("ETHUST"), ("ETPBTC"), ("ETPETH"), ("ETPUSD"), ("EUSETH"), ("EUSUSD"), ("EUTEUR"), ("EUTUSD"), ("EVTUSD"), ("FOAETH"), ("FOAUSD"), ("FSNBTC"), ("FSNETH"), ("FSNUSD"), ("FTTUSD"), ("FTTUST"), ("FUNBTC"), ("FUNETH"), ("FUNUSD"), ("GENETH"), ("GENUSD"), ("GNOETH"), ("GNOUSD"), ("GNTBTC"), ("GNTETH"), ("GNTUSD"), ("GOTETH"), ("GOTEUR"), ("GOTUSD"), ("GSDUSD"), ("GTXUSD"), ("GTXUST"), ("HOTBTC"), ("HOTETH"), ("HOTUSD"), ("IMPETH"), ("IMPUSD"), ("INTETH"), ("INTUSD"), ("IOSBTC"), ("IOSETH"), ("IOSUSD"), ("IOTBTC"), ("IOTETH"), ("IOTEUR"), ("IOTGBP"), ("IOTJPY"), ("IOTUSD"), ("IQXBTC"), ("IQXEOS"), ("IQXUSD"), ("KANUSD"), ("KANUST"), ("KNCBTC"), ("KNCETH"), ("KNCUSD"), ("LEOBTC"), ("LEOEOS"), ("LEOETH"), ("LEOUSD"), ("LEOUST"), ("LOOETH"), ("LOOUSD"), ("LRCBTC"), ("LRCETH"), ("LRCUSD"), ("LTCBTC"), ("LTCUSD"), ("LTCUST"), ("LYMBTC"), ("LYMETH"), ("LYMUSD"), ("MANETH"), ("MANUSD"), ("MGOETH"), ("MGOUSD"), ("MITBTC"), ("MITETH"), ("MITUSD"), ("MKRBTC"), ("MKRDAI"), ("MKRETH"), ("MKRUSD"), ("MLNETH"), ("MLNUSD"), ("MNABTC"), ("MNAETH"), ("MNAUSD"), ("MTNBTC"), ("MTNETH"), ("MTNUSD"), ("NCABTC"), ("NCAETH"), ("NCAUSD"), ("NECBTC"), ("NECETH"), ("NECUSD"), ("NEOBTC"), ("NEOETH"), ("NEOEUR"), ("NEOGBP"), ("NEOJPY"), ("NEOUSD"), ("NIOETH"), ("NIOUSD"), ("ODEBTC"), ("ODEETH"), ("ODEUSD"), ("OKBBTC"), ("OKBETH"), ("OKBUSD"), ("OKBUST"), ("OMGBTC"), ("OMGDAI"), ("OMGETH"), ("OMGUSD"), ("OMNBTC"), ("OMNUSD"), ("ONLETH"), ("ONLUSD"), ("ORSBTC"), ("ORSETH"), ("ORSUSD"), ("PAIBTC"), ("PAIUSD"), ("PASETH"), ("PASUSD"), ("PAXUSD"), ("PAXUST"), ("PNKETH"), ("PNKUSD"), ("POABTC"), ("POAETH"), ("POAUSD"), ("POYBTC"), ("POYETH"), ("POYUSD"), ("QSHBTC"), ("QSHETH"), ("QSHUSD"), ("QTMBTC"), ("QTMETH"), ("QTMUSD"), ("RBTBTC"), ("RBTUSD"), ("RCNBTC"), ("RCNETH"), ("RCNUSD"), ("RDNBTC"), ("RDNETH"), ("RDNUSD"), ("REPBTC"), ("REPETH"), ("REPUSD"), ("REQBTC"), ("REQETH"), ("REQUSD"), ("RIFBTC"), ("RIFUSD"), ("RLCBTC"), ("RLCETH"), ("RLCUSD"), ("RRBUSD"), ("RRBUST"), ("RRTBTC"), ("RRTUSD"), ("RTEETH"), ("RTEUSD"), ("SANBTC"), ("SANETH"), ("SANUSD"), ("SCRETH"), ("SCRUSD"), ("SEEBTC"), ("SEEETH"), ("SEEUSD"), ("SENBTC"), ("SENETH"), ("SENUSD"), ("SNGBTC"), ("SNGETH"), ("SNGUSD"), ("SNTBTC"), ("SNTETH"), ("SNTUSD"), ("SPKBTC"), ("SPKETH"), ("SPKUSD"), ("STJBTC"), ("STJETH"), ("STJUSD"), ("SWMETH"), ("SWMUSD"), ("TKNETH"), ("TKNUSD"), ("TNBBTC"), ("TNBETH"), ("TNBUSD"), ("TRIETH"), ("TRIUSD"), ("TRXBTC"), ("TRXETH"), ("TRXEUR"), ("TRXGBP"), ("TRXJPY"), ("TRXUSD"), ("TSDUSD"), ("TSDUST"), ("UDCUSD"), ("UDCUST"), ("UFRETH"), ("UFRUSD"), ("UOSBTC"), ("UOSUSD"), ("USKBTC"), ("USKEOS"), ("USKETH"), ("USKUSD"), ("USKUST"), ("UST:CNHT"), ("USTUSD"), ("UTKBTC"), ("UTKETH"), ("UTKUSD"), ("UTNETH"), ("UTNUSD"), ("VEEBTC"), ("VEEETH"), ("VEEUSD"), ("VETBTC"), ("VETETH"), ("VETUSD"), ("VLDETH"), ("VLDUSD"), ("VSYBTC"), ("VSYUSD"), ("WAXBTC"), ("WAXETH"), ("WAXUSD"), ("WBTETH"), ("WBTUSD"), ("WLOUSD"), ("WLOXLM"), ("WPRBTC"), ("WPRETH"), ("WPRUSD"), ("WTCETH"), ("WTCUSD"), ("XAUT:BTC"), ("XAUT:USD"), ("XAUT:UST"), ("XCHETH"), ("XCHUSD"), ("XLMBTC"), ("XLMETH"), ("XLMEUR"), ("XLMGBP"), ("XLMJPY"), ("XLMUSD"), ("XMRBTC"), ("XMRUSD"), ("XRAETH"), ("XRAUSD"), ("XRPBTC"), ("XRPUSD"), ("XTZBTC"), ("XTZUSD"), ("XVGBTC"), ("XVGETH"), ("XVGEUR"), ("XVGGBP"), ("XVGJPY"), ("XVGUSD"), ("YGGETH"), ("YGGUSD"), ("YYWBTC"), ("YYWETH"), ("YYWUSD"), ("ZBTUSD"), ("ZBTUST"), ("ZCNBTC"), ("ZCNETH"), ("ZCNUSD"), ("ZECBTC"), ("ZECUSD"), ("ZILBTC"), ("ZILETH"), ("ZILUSD"), ("ZRXBTC"), ("ZRXDAI"), ("ZRXETH"), ("ZRXUSD")]


URI = "wss://api-pub.bitfinex.com/ws/2"

