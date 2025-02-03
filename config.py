import logging

TOKEN = r'7606450820:AAHDRdCWch4KlgwS1ByUZKKDqawBbAVKF98'
TEST_PAYMENT_TOKEN = '381764678:TEST:110469'
admins_list = [6543114652, ]


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
