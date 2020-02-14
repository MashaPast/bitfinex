from config import config_data
from logger import appLogger
from typing import Dict
import os
import json
import requests
import pytest
import time

BITFINEX_API_CONFIG = config_data['Bitfinex']
LIST_OF_ARGVALUES = [("ABSETH"), ("ABSUSD"), ("AGIBTC"), ("AGIETH"), ("AGIUSD"), ("AIDBTC"), ("AIDETH"), ("AIDUSD"), ("AIOBTC"), ("AIOETH"), ("AIOUSD"), ("ALGBTC"), ("ALGUSD"), ("ALGUST"), ("AMPBTC"), ("AMPUSD"), ("AMPUST"), ("ANTBTC"), ("ANTETH"), ("ANTUSD"), ("ASTETH"), ("ASTUSD"), ("ATMBTC"), ("ATMETH"), ("ATMUSD"), ("ATOBTC"), ("ATOETH"), ("ATOUSD"), ("AUCBTC"), ("AUCETH"), ("AUCUSD"), ("AVTBTC"), ("AVTETH"), ("AVTUSD"), ("BABBTC"), ("BABUSD"), ("BABUST"), ("BATBTC"), ("BATETH"), ("BATUSD"), ("BBNETH"), ("BBNUSD"), ("BCIBTC"), ("BCIUSD"), ("BFTBTC"), ("BFTETH"), ("BFTUSD"), ("BNTBTC"), ("BNTETH"), ("BNTUSD"), ("BOXETH"), ("BOXUSD"), ("BSVBTC"), ("BSVUSD"), ("BTC:CNHT"), ("BTCEUR"), ("BTCGBP"), ("BTCJPY"), ("BTCUSD"), ("BTCUST"), ("BTCXCH"), ("BTGBTC"), ("BTGUSD"), ("BTTBTC"), ("BTTUSD"), ("CBTBTC"), ("CBTETH"), ("CBTUSD"), ("CHZUSD"), ("CHZUST"), ("CLOBTC"), ("CLOUSD"), ("CNDBTC"), ("CNDETH"), ("CNDUSD"), ("CNH:CNHT"), ("CNNETH"), ("CNNUSD"), ("CSXETH"), ("CSXUSD"), ("CTXBTC"), ("CTXETH"), ("CTXUSD"), ("DADBTC"), ("DADETH"), ("DADUSD"), ("DAIBTC"), ("DAIETH"), ("DAIUSD"), ("DATBTC"), ("DATETH"), ("DATUSD"), ("DGBBTC"), ("DGBUSD"), ("DGXETH"), ("DGXUSD"), ("DRNETH"), ("DRNUSD"), ("DSHBTC"), ("DSHUSD"), ("DTABTC"), ("DTAETH"), ("DTAUSD"), ("DTHBTC"), ("DTHETH"), ("DTHUSD"), ("DTXUSD"), ("DTXUST"), ("DUSK:BTC"), ("DUSK:USD"), ("EDOBTC"), ("EDOETH"), ("EDOUSD"), ("ELFBTC"), ("ELFETH"), ("ELFUSD"), ("ENJETH"), ("ENJUSD"), ("EOSBTC"), ("EOSETH"), ("EOSEUR"), ("EOSGBP"), ("EOSJPY"), ("EOSUSD"), ("EOSUST"), ("ESSBTC"), ("ESSETH"), ("ESSUSD"), ("ETCBTC"), ("ETCUSD"), ("ETHBTC"), ("ETHEUR"), ("ETHGBP"), ("ETHJPY"), ("ETHUSD"), ("ETHUST"), ("ETPBTC"), ("ETPETH"), ("ETPUSD"), ("EUSETH"), ("EUSUSD"), ("EUTEUR"), ("EUTUSD"), ("EVTUSD"), ("FOAETH"), ("FOAUSD"), ("FSNBTC"), ("FSNETH"), ("FSNUSD"), ("FTTUSD"), ("FTTUST"), ("FUNBTC"), ("FUNETH"), ("FUNUSD"), ("GENETH"), ("GENUSD"), ("GNOETH"), ("GNOUSD"), ("GNTBTC"), ("GNTETH"), ("GNTUSD"), ("GOTETH"), ("GOTEUR"), ("GOTUSD"), ("GSDUSD"), ("GTXUSD"), ("GTXUST"), ("HOTBTC"), ("HOTETH"), ("HOTUSD"), ("IMPETH"), ("IMPUSD"), ("INTETH"), ("INTUSD"), ("IOSBTC"), ("IOSETH"), ("IOSUSD"), ("IOTBTC"), ("IOTETH"), ("IOTEUR"), ("IOTGBP"), ("IOTJPY"), ("IOTUSD"), ("IQXBTC"), ("IQXEOS"), ("IQXUSD"), ("KANUSD"), ("KANUST"), ("KNCBTC"), ("KNCETH"), ("KNCUSD"), ("LEOBTC"), ("LEOEOS"), ("LEOETH"), ("LEOUSD"), ("LEOUST"), ("LOOETH"), ("LOOUSD"), ("LRCBTC"), ("LRCETH"), ("LRCUSD"), ("LTCBTC"), ("LTCUSD"), ("LTCUST"), ("LYMBTC"), ("LYMETH"), ("LYMUSD"), ("MANETH"), ("MANUSD"), ("MGOETH"), ("MGOUSD"), ("MITBTC"), ("MITETH"), ("MITUSD"), ("MKRBTC"), ("MKRDAI"), ("MKRETH"), ("MKRUSD"), ("MLNETH"), ("MLNUSD"), ("MNABTC"), ("MNAETH"), ("MNAUSD"), ("MTNBTC"), ("MTNETH"), ("MTNUSD"), ("NCABTC"), ("NCAETH"), ("NCAUSD"), ("NECBTC"), ("NECETH"), ("NECUSD"), ("NEOBTC"), ("NEOETH"), ("NEOEUR"), ("NEOGBP"), ("NEOJPY"), ("NEOUSD"), ("NIOETH"), ("NIOUSD"), ("ODEBTC"), ("ODEETH"), ("ODEUSD"), ("OKBBTC"), ("OKBETH"), ("OKBUSD"), ("OKBUST"), ("OMGBTC"), ("OMGDAI"), ("OMGETH"), ("OMGUSD"), ("OMNBTC"), ("OMNUSD"), ("ONLETH"), ("ONLUSD"), ("ORSBTC"), ("ORSETH"), ("ORSUSD"), ("PAIBTC"), ("PAIUSD"), ("PASETH"), ("PASUSD"), ("PAXUSD"), ("PAXUST"), ("PNKETH"), ("PNKUSD"), ("POABTC"), ("POAETH"), ("POAUSD"), ("POYBTC"), ("POYETH"), ("POYUSD"), ("QSHBTC"), ("QSHETH"), ("QSHUSD"), ("QTMBTC"), ("QTMETH"), ("QTMUSD"), ("RBTBTC"), ("RBTUSD"), ("RCNBTC"), ("RCNETH"), ("RCNUSD"), ("RDNBTC"), ("RDNETH"), ("RDNUSD"), ("REPBTC"), ("REPETH"), ("REPUSD"), ("REQBTC"), ("REQETH"), ("REQUSD"), ("RIFBTC"), ("RIFUSD"), ("RLCBTC"), ("RLCETH"), ("RLCUSD"), ("RRBUSD"), ("RRBUST"), ("RRTBTC"), ("RRTUSD"), ("RTEETH"), ("RTEUSD"), ("SANBTC"), ("SANETH"), ("SANUSD"), ("SCRETH"), ("SCRUSD"), ("SEEBTC"), ("SEEETH"), ("SEEUSD"), ("SENBTC"), ("SENETH"), ("SENUSD"), ("SNGBTC"), ("SNGETH"), ("SNGUSD"), ("SNTBTC"), ("SNTETH"), ("SNTUSD"), ("SPKBTC"), ("SPKETH"), ("SPKUSD"), ("STJBTC"), ("STJETH"), ("STJUSD"), ("SWMETH"), ("SWMUSD"), ("TKNETH"), ("TKNUSD"), ("TNBBTC"), ("TNBETH"), ("TNBUSD"), ("TRIETH"), ("TRIUSD"), ("TRXBTC"), ("TRXETH"), ("TRXEUR"), ("TRXGBP"), ("TRXJPY"), ("TRXUSD"), ("TSDUSD"), ("TSDUST"), ("UDCUSD"), ("UDCUST"), ("UFRETH"), ("UFRUSD"), ("UOSBTC"), ("UOSUSD"), ("USKBTC"), ("USKEOS"), ("USKETH"), ("USKUSD"), ("USKUST"), ("UST:CNHT"), ("USTUSD"), ("UTKBTC"), ("UTKETH"), ("UTKUSD"), ("UTNETH"), ("UTNUSD"), ("VEEBTC"), ("VEEETH"), ("VEEUSD"), ("VETBTC"), ("VETETH"), ("VETUSD"), ("VLDETH"), ("VLDUSD"), ("VSYBTC"), ("VSYUSD"), ("WAXBTC"), ("WAXETH"), ("WAXUSD"), ("WBTETH"), ("WBTUSD"), ("WLOUSD"), ("WLOXLM"), ("WPRBTC"), ("WPRETH"), ("WPRUSD"), ("WTCETH"), ("WTCUSD"), ("XAUT:BTC"), ("XAUT:USD"), ("XAUT:UST"), ("XCHETH"), ("XCHUSD"), ("XLMBTC"), ("XLMETH"), ("XLMEUR"), ("XLMGBP"), ("XLMJPY"), ("XLMUSD"), ("XMRBTC"), ("XMRUSD"), ("XRAETH"), ("XRAUSD"), ("XRPBTC"), ("XRPUSD"), ("XTZBTC"), ("XTZUSD"), ("XVGBTC"), ("XVGETH"), ("XVGEUR"), ("XVGGBP"), ("XVGJPY"), ("XVGUSD"), ("YGGETH"), ("YGGUSD"), ("YYWBTC"), ("YYWETH"), ("YYWUSD"), ("ZBTUSD"), ("ZBTUST"), ("ZCNBTC"), ("ZCNETH"), ("ZCNUSD"), ("ZECBTC"), ("ZECUSD"), ("ZILBTC"), ("ZILETH"), ("ZILUSD"), ("ZRXBTC"), ("ZRXDAI"), ("ZRXETH"), ("ZRXUSD")]



def make_request(full_url):
    response = requests.get(full_url)
    appLogger.debug("Response status is {}".format(response.status_code))
    return response


def get_response_time(response):
    response_time = response.elapsed.total_seconds()
    appLogger.debug("Request completed in {} ms".format(response_time * 1000))
    return response_time * 1000


def create_endpoint(endpoint_str):
    appLogger.debug('Getting full url for sending request to Bitfinex API')
    full_url = BITFINEX_API_CONFIG['url'].format(endpoint_str)
    return full_url


def get_response_headers(response_for_headers):
    headers_data: Dict = dict(response_for_headers.headers)
    appLogger.debug('Getting response headers from Bitfinex API')
    return headers_data


def get_json_from_asset(file_path):
    with open(file_path, 'r') as f:
        content_type: Dict = json.load(f)
        appLogger.debug('Getting content type from asset')
        return content_type


def get_response_body(response_for_body):
    body: list = response_for_body.json()
    appLogger.debug('Getting response body from Bitfinex API')
    return body


def write_response_to_a_file(response_data, file_name):
    file = open(file_name, "w")
    file.write(response_data.text)
    file.close()

def check_body_types(json_data):
    for i in range(0, len(json_data)):
        field_type = (type(json_data[i]))
        appLogger.info('Check type ' + str(i) + str(field_type))
        return field_type
