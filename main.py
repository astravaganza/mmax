import config
import requests, uuid
import base64, json
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from loguru import logger


class ManoraMAX(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(config.DEFAULT_HEADERS)

        self.device_uuid = str(uuid.uuid4())

        self.session.headers.update({"x-myplex-tenant-id": self.device_uuid})

        self.device_id = None
        self.payload = None
        self.aes_key = None

    def register_device(self) -> None:
        logger.info("Attempting to register an arbitrary tablet")

        s = self.session.post(url=config.REGISTER_URL, data={
            'payload': base64.b64encode(self.build_payload())
        }).json()

        self.dump_creds(self.process_payload(s["response"]))

    def process_payload(self, payload: str) -> dict:
        """
		Decrypts the registration payload 
		returned.
		"""
        logger.debug("Decrypting response..")

        cipher = AES.new(config.MASTER_AES_KEY, AES.MODE_CBC, iv=bytes([0] * 16))
        plaintext = unpad(cipher.decrypt(base64.b64decode(payload)), 16)

        return json.loads(plaintext)

    def build_payload(self) -> bytes:
        """
		Builds the payload responsible for device
		registration and encrypts it with the 
		master key.
		"""
        payload_str = f"serialNo={self.device_uuid}&os=Android&osVersion=9.0&make=" \
                      f"Apple&model=iPhone16&resolution=3840x2160&profile=work&deviceT" \
                      f"ype=Tablet&clientSecret=ApalyaAndroid&externalToken=null&X-MSISDN" \
                      f"=null"

        cipher = AES.new(config.MASTER_AES_KEY, AES.MODE_CBC, iv=bytes([0] * 16))
        ciphertext = cipher.encrypt(pad(payload_str.encode(), 16))

        return ciphertext

    def dump_creds(self, creds: dict) -> None:
        """
		Dumps the secrets to a JSON file.
		"""
        self.device_id = creds["deviceId"]

        self.aes_key = config.AES_START + self.device_id.split('-')[4][4:].encode() + config.AES_END

        self.payload = AES.new(self.aes_key, AES.MODE_CBC, iv=bytes([0] * 16)).encrypt(pad(config.MANIFEST_PAYLOAD, 16))

        creds.update({
            "aesKey": self.aes_key.decode(),
            "payload": base64.b64encode(self.payload).decode(),
        })

        with open("device.json", 'w') as f:
            json.dump(creds, f, indent=4)

        logger.info("Saved to device.json!")


@logger.catch
def main() -> None:
    logger.info("Welcome to ManoraMAX!")
    manoramax = ManoraMAX()
    manoramax.register_device()


if __name__ == "__main__":
    main()
