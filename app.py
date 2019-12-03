import requests
import time
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.legacy import show_message
from luma.core.legacy.font import CP437_FONT, proportional

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90,
                 rotate=0, blocks_arranged_in_reverse_order=False)


def show(msg):
    show_message(device, msg, fill='white',
                 font=proportional(CP437_FONT), scroll_delay=0.2)
    time.sleep(2)


def showDebug(msg):
    print(msg)
    time.sleep(2)


while True:
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin,ethereum')
    data = response.json()
    print(data)
    bitcoinPrice = data['bitcoin']['usd']
    ethereumPrice = data['ethereum']['usd']
    btcMsg = 'BTC: $%s' % bitcoinPrice
    ethMsg = 'ETH: $%s' % ethereumPrice
    for _ in range(20):
        show(btcMsg)
        show(ethMsg)
