import logging

TOKEN = r'7606450820:AAHDRdCWch4KlgwS1ByUZKKDqawBbAVKF98'
TEST_PAYMENT_TOKEN = '381764678:TEST:110469'
PAYMENT_TOKEN = '390540012:LIVE:65386'
admins_list = [6543114652, 468761696]


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


provider_data = {
    "receipt": {
        "customer": {
            "email": "Stepanova_1991@mail.ru",
            "phone": "89655007070"
        },
        "items": [
            {
                "description": "Интенсив GUNA ИЗОБИЛИЯ",
                "quantity": 1,
                "amount": {
                    "value": 100,
                    "currency": "RUB"
                },
                "vat_code": 1,
                "payment_mode": "full_payment",
                "payment_subject": "commodity"
            }
        ],
        "tax_system_code": 1
    }
}
